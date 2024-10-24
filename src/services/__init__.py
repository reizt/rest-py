from src.iservices import IServices
from src.iservices.post_repo import IPostRepo
from src.iservices.user_repo import IUserRepo
from src.services.post_repo import PostRepo
from src.services.user_repo import UserRepo


class Services(IServices):
  user_repo: IUserRepo
  post_repo: IPostRepo

  def __init__(self) -> None:
    self.user_repo = UserRepo()
    self.post_repo = PostRepo()
