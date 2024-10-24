from pydantic import BaseModel

from src.entities.post import Post


class Input(BaseModel):
  user_id: int | None = None


class Output(BaseModel):
  posts: list[Post]
