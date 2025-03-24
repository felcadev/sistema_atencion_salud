from flask import Flask
from flasgger import Swagger
from src.context.users.features.register_user.infrastructure.register_user_controller import register_user_controller_bp
from src.context.users.features.register_user.infrastructure.register_user_container import RegisterUserContainer


def create_app() -> Flask:
    app = Flask(__name__)

    # Initialize dependency injection container
    register_user_container = RegisterUserContainer()
    app.registerUserContainer = register_user_container

    app.register_blueprint(register_user_controller_bp, url_prefix='/api/users')

    swagger = Swagger(app)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)