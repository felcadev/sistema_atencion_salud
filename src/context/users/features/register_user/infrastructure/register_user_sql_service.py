from src.context.users.features.register_user.application.ports.register_user_port import RegisterUserService
from src.context.users.features.register_user.domain.dtos.register_user_input_dto import RegisterUserInputDto

class RegisterUserSqlService(RegisterUserService):
    def register_user(self, register_user_input_dto: RegisterUserInputDto) -> str:
        # TODO: Implement register_user method
        return register_user_input_dto.name