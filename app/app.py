from flask import Flask
from flask_login import LoginManager
from Model.data_base_handler import data_access_manager
from Controller.Blueprints.login_blueprint import auth
from Controller.Blueprints.messages_blueprint import messages
from Controller.Blueprints.errors import errors


def create_app():
    app = Flask(__name__)
    login = LoginManager(app)
    app.register_blueprint(auth)
    app.register_blueprint(messages)
    app.register_blueprint(errors)
    app.debug = 1
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    @login.user_loader
    def load_user(user_name):  # not sure if need to add self here
        user = data_access_manager.get_user(user_name=user_name)
        return user

    return app
