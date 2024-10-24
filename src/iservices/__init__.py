from src.iservices.post_repo import IPostRepo
from src.iservices.user_repo import IUserRepo


class IServices:
  user_repo: IUserRepo
  post_repo: IPostRepo
