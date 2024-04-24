from pydantic import BaseModel
from typing import List
from .chat import ChatModel

class ChatHistoryModel(BaseModel):
    chat_history: List[ChatModel] = []

    def add_chat(self, chat: ChatModel):
        self.chat_history.append(chat)
