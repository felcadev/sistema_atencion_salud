from src.context.users.features.register_user.application.ports.register_user_port import RegisterUserService
from src.context.users.features.register_user.domain.dtos.register_user_input_dto import RegisterUserInputDto

class RegisterUserUseCase:
    def __init__(self, register_user_port: RegisterUserService):
        self.register_user_port = register_user_port

    def execute(self, register_user_input_dto: RegisterUserInputDto) -> str:
        return self.register_user_port.register_user(register_user_input_dto)