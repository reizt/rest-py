from typing import TypedDict

from fastapi import APIRouter, HTTPException, Response
from fastapi.responses import JSONResponse

from src.handlers._shared import PostJson
from src.iservices import IServices
from src.iusecases.list_posts import Input
from src.usecases.list_posts import create_usecase


def create_router(services: IServices) -> APIRouter:
  usecase = create_usecase(services)
  router = APIRouter()

  class ResponseJson(TypedDict):
    posts: list[PostJson]

  @router.get("/posts")
  async def handle(user_id: int | None = None) -> Response:
    input = Input(user_id=user_id)
    try:
      output = await usecase.run(input)
    except Exception as err:
      print(err)
      raise HTTPException(400, "Bad Request")

    body: ResponseJson = {
      "posts": [
        {
          "id": post.id,
          "user_id": post.user_id,
          "title": post.title,
          "content": post.content,
        }
        for post in output.posts
      ],
    }
    return JSONResponse(body)

  return router
