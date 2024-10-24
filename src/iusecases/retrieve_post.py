from pydantic import BaseModel

from src.entities.post import Post


class Input(BaseModel):
  post_id: int


class Output(BaseModel):
  post: Post | None
