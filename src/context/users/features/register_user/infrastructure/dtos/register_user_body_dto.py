from marshmallow import Schema, fields, post_load, validates, ValidationError
from src.context.users.features.register_user.domain.dtos.register_user_input_dto import RegisterUserInputDto

class RegisterUserBodyDtoSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)

    @post_load
    def make_object(self, data, **kwargs) -> RegisterUserInputDto:
        self.validate(data)
        return RegisterUserInputDto(**data)
    
    @validates('name')
    def validate_name(self, value):
        if len(value) < 3:
            raise ValidationError('Name must be at least 3 characters long')

    @validates('password')
    def validate_password(self, value):
        if len(value) < 6:
            raise ValidationError('Password must be at least 6 characters long')
