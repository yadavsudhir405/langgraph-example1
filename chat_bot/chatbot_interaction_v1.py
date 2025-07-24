from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langgraph.graph import StateGraph
from langgraph.constants import START, END

from state import State


class ChatBot:
    __graph: StateGraph = None
    __llm = None

    def __init__(self):
        load_dotenv()
        self.__llm = init_chat_model('google_genai:gemini-2.0-flash')
        self.__graph = None

    def __chat_model(self, state: State) -> State:
        return {'messages': [self.__llm.invoke(state['messages'])]}

    def __build_graph(self):
        builder = StateGraph(State)
        builder.add_node('chatbot_node', self.__chat_model)
        builder.add_edge(START, 'chatbot_node')
        builder.add_edge('chatbot_node', END)
        self.__graph = builder.compile()


    @staticmethod
    def __build_message(message: str):
        return {"role": "user", "content": message}

    def run(self):
        if self.__graph is None:
            self.__build_graph()

        state = None;
        while True:
            in_message = input("Your Question\n");
            if in_message in ['exit', 'quiet']:
                break;
            elif state is None:
                state = {'messages': [ChatBot.__build_message(in_message)]}
            else:
                state['messages'].append(ChatBot.__build_message(in_message))

            result = self.__graph.invoke(state)
            print("Bot: ", result['messages'][-1].content)


