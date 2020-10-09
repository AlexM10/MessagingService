from flask import Blueprint, request, jsonify, make_response

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(404)
def handle_unexpected_error(error):
    status_code = 404
    success = False
    return make_response(jsonify({
        'success': success,
        'code': status_code,
        'error': {
            'type': 'Page Not Found',
            'message': 'Page Not Found 404 error'
        }
    }), status_code)


@errors.app_errorhandler(TypeError)
def handle_unexpected_error(error):
    status_code = 400
    success = False
    return make_response(jsonify({
        'success': success,
        'code': status_code,
        'error': {
            'type': 'Bad Request',
            'message': 'Bad Request Check Request again'
        }
    }), status_code)


@errors.app_errorhandler(Exception)
def handle_unexpected_error(error):
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
