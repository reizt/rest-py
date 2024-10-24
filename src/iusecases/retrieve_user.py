from pydantic import BaseModel

from src.entities.user import User


class Input(BaseModel):
  user_id: int


class Output(BaseModel):
  user: User | None
