from abc import ABC, abstractmethod
from src.context.users.features.register_user.domain.dtos.register_user_input_dto import RegisterUserInputDto

class RegisterUserService(ABC):
    @abstractmethod
    def register_user(self, register_user_input_dto: RegisterUserInputDto) -> str:
        pass
