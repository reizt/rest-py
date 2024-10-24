from src.iservices import IServices
from src.iservices.post_repo import IPostRepo
from src.iusecases._utils import UseCase
from src.iusecases.retrieve_post import Input, Output


def create_usecase(ctx: IServices) -> UseCase[Input, Output]:
  async def run(input: Input) -> Output:
    where = IPostRepo.Where(id=input.post_id)
    post = await ctx.post_repo.pick(where=where)

    if post is None:
      return Output(post=None)

    return Output(post=post.to_entity())

  return UseCase(run)
