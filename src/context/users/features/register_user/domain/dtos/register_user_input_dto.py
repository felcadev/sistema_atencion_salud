from dataclasses import dataclass

@dataclass
class RegisterUserInputDto:
    name: str
    email: str
    password: str
