import traceback
from typing import TypedDict

from fastapi import APIRouter, HTTPException, Response
from fastapi.responses import JSONResponse

from src.handlers._shared import PostJson
from src.iservices import IServices
from src.iusecases.create_post import Input
from src.usecases.create_post import create_usecase


def create_router(services: IServices) -> APIRouter:
  usecase = create_usecase(services)
  router = APIRouter()

  class RequestJson(TypedDict):
    user_id: int
    title: str
    content: str

  class ResponseJson(TypedDict):
    post: PostJson

  @router.post("/posts")
  async def handle(body: RequestJson) -> Response:
    input = Input(
      user_id=body["user_id"],
      title=body["title"],
      content=body["content"],
    )
    try:
      output = await usecase.run(input)
    except Exception as err:
      traceback.print_exc()
      print(err)
      raise HTTPException(400, "Bad Request")

    resJson: ResponseJson = {
      "post": {
        "id": output.post.id,
        "user_id": output.post.user_id,
        "title": output.post.title,
        "content": output.post.content,
      },
    }
    return JSONResponse(resJson)

  return router
