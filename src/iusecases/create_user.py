from pydantic import BaseModel

from src.entities.user import User


class Input(BaseModel):
  name: str


class Output(BaseModel):
  user: User
