from Model.Models import User
from Model.database_setup import session
from Model.user_obj import UserObj


class UserRepo(object):

    def validate_user(self, user: UserObj):
        user_q = session.query(User).get(user.get_username())
        if user_q is None:
            return False
        elif (user_q.username == user.get_username()) and (user.check_password(user_q.password_hash)):
            return True
        else:
            return False

    def is_username_exist(self, user_name):
        user = session.query(User).get(user_name)
        if user is None:
            return False
        else:
            return True

    def add_user(self, user: UserObj):
        user_data = User(username=user.get_username(), password_hash=user.set_password_hash())
        session.add(user_data)
        session.commit()
        return True

    def get_user(self, user_name):
        user = session.query(User).get(user_name)
        if user is not None:
            return UserObj(user_name=user.username, password=user.password_hash)
        else:
            return None
