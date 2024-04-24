from pydantic import BaseModel, Field

class ChatModel(BaseModel):
    role: str = Field(..., description="roleが有効な値ではありません。", pattern="^(USER|CHATBOT|SYSTEM)$")
    message: str
