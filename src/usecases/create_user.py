from src.iservices import IServices
from src.iservices.user_repo import IUserRepo
from src.iusecases._utils import UseCase
from src.iusecases.create_user import Input, Output


def create_usecase(ctx: IServices) -> UseCase[Input, Output]:
  async def run(input: Input) -> Output:
    create_data = IUserRepo.CreateData(
      name=input.name,
    )
    user = await ctx.user_repo.create(create_data)

    return Output(user=user.to_entity())

  return UseCase(run)
