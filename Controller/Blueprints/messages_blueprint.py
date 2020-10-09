from flask import Blueprint, request, jsonify
from flask_login import logout_user, login_user, current_user, login_required
from Model.user_obj import UserObj
from Model.message_obj import MessageObj
from Controller.response_contoller import ResponseController
from Controller.Blueprints.login_blueprint import is_logged_helper

messages = Blueprint('messages', __name__)
response_controller = ResponseController()


def create_message(json_message):
    try:
        sender = json_message['sender']
        receiver = json_message['receiver']
        subject = json_message['subject']
        message = json_message['message']
        time_stamp = json_message['timestamp']
        if sender and receiver and subject and message is not None:
            return MessageObj(sender=sender, receiver=receiver, subject=subject
                              , message=message, time_stamp=time_stamp)
        else:
            return None
    except TypeError as e:
        return None


@messages.route('/messages', methods=['POST', 'GET'])
@login_required
def messages_handler():
    username = request.args.get('username')
    password = request.args.get('password')
    if username not in is_logged_helper.keys():
        return jsonify(MessageObj("Server", username, "permission denied", "user is not logged in").serialize())
    else:
        user = UserObj(user_name=username, password=password)
        user_request = request.args.get('request')
        return response_controller.generate_response(user=user, request=user_request)


@messages.route('/message', methods=['POST', 'GET'])
@login_required
def message_handler():
    username = request.args.get('username')
    password = request.args.get('password')
    if username not in is_logged_helper.keys():
        return jsonify(MessageObj("Server", username, "permission denied", "user is not logged in").serialize())
    else:
        user = UserObj(user_name=username, password=password)
        user_request = request.args.get('request')
        if request.method == 'GET':
            return response_controller.generate_response(user=user, request='read')
        elif request.method == 'POST':
            message = create_message(request.get_json())
            return response_controller.generate_response(user=user, request=user_request, message=message)
