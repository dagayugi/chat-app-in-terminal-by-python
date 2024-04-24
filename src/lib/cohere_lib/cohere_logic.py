import cohere
import os

from src.lib.cohere_lib.chat import ChatModel
from src.lib.cohere_lib.chat_history import ChatHistoryModel

class CohereLogic:

    def __init__(self) -> None:
        
        self.co = cohere.Client(os.getenv('COHERE_API'))

    def create_chat(self, chat: ChatModel, history_chat: ChatHistoryModel):

        print(history_chat.model_dump())
        return self.co.chat(
            chat_history=history_chat.model_dump().get('chat_history', []),
            message=chat.message,
)