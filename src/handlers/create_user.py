from typing import TypedDict

from fastapi import APIRouter, HTTPException, Response
from fastapi.responses import JSONResponse

from src.handlers._shared import UserJson
from src.iservices import IServices
from src.iusecases.create_user import Input
from src.usecases.create_user import create_usecase


def create_router(services: IServices) -> APIRouter:
  usecase = create_usecase(services)
  router = APIRouter()

  class RequestJson(TypedDict):
    name: str

  class ResponseJson(TypedDict):
    user: UserJson

  @router.post("/users")
  async def handle(reqJson: RequestJson) -> Response:
    input = Input(name=reqJson["name"])
    try:
      output = await usecase.run(input)
    except Exception as err:
      print(err)
      raise HTTPException(400, "Bad Request")

    resJson: ResponseJson = {
      "user": {
        "id": output.user.id,
        "name": output.user.name,
      },
    }
    return JSONResponse(resJson)

  return router
