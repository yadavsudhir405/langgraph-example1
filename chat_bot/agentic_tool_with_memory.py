from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver

from .util import  build_message
from .state import State


@tool
def get_stock_price(symbol: str) -> float:
    '''Return the current price of a stock given the stock symbol
       :param symbol: stock symbol
       :return: current price of the stock
       '''
    return {
        "MSFT": 100.24,
        "AAPL": 101.24,
        "GOOGLE": 102.24,
        "AMZN": 103.24,
    }.get(symbol, 0.0)


class AgenticToolWithMemory:
    __llm_with_tools = None
    __graph = None
    __tools = [get_stock_price]
    __memory_saver = MemorySaver()

    def __init__(self):
        load_dotenv()
        llm = init_chat_model('google_genai:gemini-2.0-flash')
        self.__llm_with_tools = llm.bind_tools(self.__tools)


    def __chat_model(self, state: State) -> State:
        return {'messages': self.__llm_with_tools.invoke(state['messages'])}


    def __build_graph(self):
        graph_builder = StateGraph(State)

        graph_builder.add_node('chatbot', self.__chat_model)
        graph_builder.add_node('tools', ToolNode(self.__tools))

        graph_builder.add_edge(START, 'chatbot')
        graph_builder.add_conditional_edges('chatbot', tools_condition)
        graph_builder.add_edge('tools', 'chatbot')
        graph_builder.add_edge('chatbot', END)
        self.__graph = graph_builder.compile(checkpointer=self.__memory_saver)


    def run(self):
        self.__build_graph()
        state = None
        config = { 'configurable': {'thread_id': '1'}}
        while True:
            in_message = input("Your Question\n")
            if in_message in ['exit', 'quiet']:
                break;
            elif state is None:
                state = {'messages': [build_message(in_message)]}
            else:
                state['messages'].append(build_message(in_message))

            result = self.__graph.invoke(state, config=config)
            print("Bot: ", result['messages'][-1].content)