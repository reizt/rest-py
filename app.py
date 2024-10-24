from typing import Any

from fastapi import FastAPI

from src.handlers import (
  create_post,
  create_user,
  list_posts,
  list_users,
  retrieve_post,
  retrieve_user,
)
from src.services import Services


def create_app() -> FastAPI:
  app = FastAPI()

  services = Services()

  @app.get("/")
  def read_root() -> dict[str, Any]:
    return {"Hello": "World"}

  app.include_router(list_users.create_router(services))
  app.include_router(retrieve_user.create_router(services))
  app.include_router(create_user.create_router(services))
  app.include_router(list_posts.create_router(services))
  app.include_router(create_post.create_router(services))
  app.include_router(retrieve_post.create_router(services))

  return app
