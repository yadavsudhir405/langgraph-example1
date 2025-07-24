from .chatbot_interaction import start_chatbot
from .chatbot_interaction_v1 import ChatBot
from .state import State



def build_message(message: str):
    return {"role": "user", "content": message}