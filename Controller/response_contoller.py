from enum import Enum
from app.app import data_access_manager
from Model.message_obj import MessageObj
from flask import make_response, jsonify


class response_enum(Enum):
    READ = 'read'
    WRITE = 'write'
    DELETE = 'delete'
    GET_ALL = 'get_all'
    GET_ALL_UNREAD = 'get_all_unread'
    PAGE_NOT_FOUND = '404'
    BAD_REQUEST = '400'
    SERVER_ERROR = '500'


class ResponseController(object):

    def generate_response(self, user, request, message=None):
        if request == response_enum.READ.value:
            ans: MessageObj = data_access_manager.read_message(user=user)
            if ans:
                return make_response(jsonify(ans.serialize()), 200)
            else:
                return make_response(jsonify(MessageObj(sender="Server", receiver=user.get_username(),
                                                        subject="Message read", message="No messages to read")
                                             .serialize()), 200)

        elif request == response_enum.WRITE.value:
            if message is not None:
                ans = data_access_manager.write_message(message=message, user=user)
                if ans:
                    return make_response(jsonify({'success': True}), 200)
                else:
                    return make_response(jsonify(MessageObj(sender="Server", receiver=user.get_username(),
                                                            message=message.get_message(),
                                                            subject="Message write Failed").serialize()), 404)
            else:
                return make_response(jsonify(MessageObj("Server", user.get_username(), "error code: 400",
                                                        "Write message failed, message to write "
                                                        "is not with right format").serialize()), 400)

        elif request == response_enum.DELETE.value:
            if message is not None:
                ans = data_access_manager.delete_message(message=message, user=user)
                if ans:
                    return make_response(jsonify({'success': True}), 200)
                else:
                    return make_response(jsonify(MessageObj("Server", user.get_username(), message.get_message(),
                                                            "Message deleted Failed").serialize()), 404)
            else:
                return make_response(jsonify(
                    MessageObj("Server", user.get_username(), "error code: 400", "Delete message failed, message to "
                                                                                 "delete is not with right "
                                                                                 "format").serialize()), 400)

        elif request == response_enum.GET_ALL.value:
            return make_response(jsonify(data_access_manager.get_all_messages(user=user)), 200)

        elif request == response_enum.GET_ALL_UNREAD.value:
            return make_response(jsonify(data_access_manager.get_all_unread_messages(user=user)), 200)

        else:
            status_code = 500
            success = False
            return make_response(jsonify({
                'success': success,
                'code': status_code,
                'error': {
                    'type': 'Server Error',
                    'message': 'unexpected server error 404 error'
                }
            }), status_code)