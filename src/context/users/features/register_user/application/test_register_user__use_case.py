import pytest
from unittest.mock import Mock
from src.context.users.features.register_user.application.register_user_use_case import RegisterUserUseCase
from src.context.users.features.register_user.domain.dtos.register_user_input_dto import RegisterUserInputDto
from src.context.users.features.register_user.application.ports.register_user_port import RegisterUserService

class TestRegisterUserUseCase:
    def setup_method(self):
        self.register_user_port_mock = Mock(spec=RegisterUserService)
        self.register_user_use_case = RegisterUserUseCase(self.register_user_port_mock)
        
    def test_should_call_register_user_port_with_correct_input(self):
        # Arrange
        expected_dto = RegisterUserInputDto(
            name="John Doe",
            email="john.doe@example.com",
            password="securePassword123"
        )
        
        # Act
        self.register_user_use_case.execute(expected_dto)
        
        # Assert
        self.register_user_port_mock.register_user.assert_called_once_with(expected_dto)