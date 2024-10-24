from src.iservices import IServices
from src.iservices.post_repo import IPostRepo
from src.iusecases._utils import UseCase
from src.iusecases.create_post import Input, Output


def create_usecase(ctx: IServices) -> UseCase[Input, Output]:
  async def run(input: Input) -> Output:
    create_data = IPostRepo.CreateData(
      user_id=input.user_id,
      title=input.title,
      content=input.content,
    )
    post = await ctx.post_repo.create(create_data)

    return Output(post=post.to_entity())

  return UseCase(run)
