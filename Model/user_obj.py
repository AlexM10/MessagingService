from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class UserObj(UserMixin):

    def __init__(self, user_name, password):
        self.__user_name = user_name
        self.__password = password


    def set_password_hash(self):
        return generate_password_hash(self.__password, method='sha256')

    def check_password(self, password):
        return check_password_hash(password, self.__password)


    def get_username(self):
        return self.__user_name

    def get_password(self):
        return self.__password

    def get_id(self):
        return self.__user_name
