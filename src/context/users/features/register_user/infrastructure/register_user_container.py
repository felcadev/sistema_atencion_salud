from dependency_injector import containers, providers
from .register_user_sql_service import RegisterUserSqlService
from src.context.users.features.register_user.application.register_user_use_case import RegisterUserUseCase


class RegisterUserContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
          'src.context.users.features.register_user.infrastructure.register_user_controller',
        ]
    )

    register_user_port = providers.Singleton(RegisterUserSqlService)

    register_user_use_case = providers.Factory(
        RegisterUserUseCase,
        register_user_port=register_user_port
    )