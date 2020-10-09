from flask import Blueprint, request, jsonify, make_response
from flask_login import logout_user, login_user, current_user
from Model.user_obj import UserObj
from Model.message_obj import MessageObj
from app.app import data_access_manager

auth = Blueprint('auth', __name__)
is_logged_helper = {}

@auth.route('/login', methods=['POST'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    user = UserObj(user_name=username, password=password)
    if username in is_logged_helper.keys():
        return jsonify(MessageObj("Server", request.args.get('username'), "login failed", "user already logged in").serialize()), 400
    if data_access_manager.check_auth_user(user):
        is_logged_helper[username] = True
        login_user(user)
        return jsonify(MessageObj("Server", str(username), "login success", "login complete").serialize()), 200
    else:
        return jsonify(MessageObj("Server", str(username), "login failed", "wrong password or username").serialize()), 400


@auth.route('/signup', methods=['POST'])
def signup():
    username = request.args.get('username')
    password = request.args.get('password')
    user = UserObj(user_name=username, password=password)
    if data_access_manager.register_user(user):
        return make_response(
            jsonify(MessageObj("Server", username, "Registration complete", "user has registered successfully").serialize()), \
               200)
    else:
        return make_response(jsonify(
            MessageObj("Server", username, "Registration failed", "this username already exist").serialize()
        )
            , 400)


@auth.route('/logout', methods=['POST'])
def logout():
    username = request.args.get('username')
    if username not in is_logged_helper:
        return make_response(
            jsonify(MessageObj("Server", username, "logout failed", "user is not logged in").serialize()), 400
        )
    else:
        del is_logged_helper[username]
        logout_user()
        return make_response(
            jsonify(MessageObj("Server", username, "logout complete", "you are logged out").serialize()),
            200)
