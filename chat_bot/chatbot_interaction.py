from typing import TypedDict, Annotated
from langchain.chat_models import init_chat_model
from langgraph.constants import START, END
from langgraph.graph import add_messages, StateGraph
from dotenv import load_dotenv

class State(TypedDict):
    message: Annotated[list, add_messages]


def start_chatbot():
    load_dotenv()
    llm = init_chat_model('google_genai:gemini-2.0-flash')

    def chat_model(state: State) -> State:
        return {'message': [llm.invoke(state['message'])]}

    builder = StateGraph(State)

    builder.add_node('chat_model', chat_model)

    builder.add_edge(START, 'chat_model')
    builder.add_edge('chat_model', END)

    graph = builder.compile()

    state = None

    while True:
        in_message = input('Your Question\n')
        if in_message.lower() in ['exit', 'quiet']:
            break

        if state is None:
            state: State = {"message": [{"role": "user", "content": in_message}]}

        else:
            state['message'].append({'role': 'user', 'content': in_message})

        result = graph.invoke(state)
        print("Bot: ", result['message'][-1].content)
