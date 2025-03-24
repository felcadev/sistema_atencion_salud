from flask import Blueprint, request
from dependency_injector.wiring import inject, Provide
from flasgger import swag_from
from src.context.users.features.register_user.application.register_user_use_case import RegisterUserUseCase
from src.context.users.features.register_user.infrastructure.register_user_container import RegisterUserContainer
from src.context.users.features.register_user.infrastructure.dtos.register_user_body_dto import RegisterUserBodyDtoSchema


register_user_controller_bp = Blueprint('register_user_controller_bp', __name__)

@register_user_controller_bp.route('/register-user', methods=['POST'])
@inject
@swag_from({
    'tags': ['Users'],
    'summary': 'Register user',
    'description': 'Register user',
    'parameters': [
        {
            'in': 'body',
            'name': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'},
                    'email': {'type': 'string'},
                    'password': {'type': 'string'}
                },
                'required': ['name', 'email', 'password']
            }
        }
    ],
    'responses': {
        200: {},
        400: {
            'description': 'Validation error',
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {'type': 'string'}
                }
            }
        }
    }
})
def register_user(register_user_use_case: RegisterUserUseCase = Provide[RegisterUserContainer.register_user_use_case]):
    schema = RegisterUserBodyDtoSchema()
    try:
        user_dto = schema.load(request.json)
    except Exception as e:
        return {'error': str(e)}, 400

    return register_user_use_case.execute(user_dto)