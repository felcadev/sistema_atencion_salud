from flask import Blueprint, request
from dependency_injector.wiring import inject, Provide
from src.context.users.features.register_user.application.register_user_use_case import RegisterUserUseCase
from src.context.users.features.register_user.infrastructure.register_user_container import RegisterUserContainer
from src.context.users.features.register_user.infrastructure.dtos.register_user_body_dto import RegisterUserBodyDtoSchema


register_user_controller_bp = Blueprint('register_user_controller_bp', __name__)

@register_user_controller_bp.route('/register-user', methods=['POST'])
@inject
def register_user(register_user_use_case: RegisterUserUseCase = Provide[RegisterUserContainer.register_user_use_case]):
    schema = RegisterUserBodyDtoSchema()
    try:
        user_dto = schema.load(request.json)
    except Exception as e:
        return {'error': str(e)}, 400

    return register_user_use_case.execute(user_dto)