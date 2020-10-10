from Model.user_repository import UserRepo
from Model.message_repository import MessageRepository
from Model.message_obj import MessageObj
from Model.user_obj import UserObj


class MessageHandlerRepository(object):

    def __init__(self):
        self.__user_repo = UserRepo()
        self.__message_repo = MessageRepository()

    def read_message(self, user: UserObj):
        ans: MessageObj = self.__message_repo.get_message(user.get_username())
        if ans is not None:
            self.__message_repo.edit_message_is_read(ans.id)
        return ans

    def write_message(self, message: MessageObj, user: UserObj):
        if (self.__user_repo.is_username_exist(message.get_sender())) and \
                (self.__user_repo.is_username_exist(message.get_receiver())) and \
                (user.get_username() == message.get_sender()):
            self.__message_repo.add_message(message=message)
            return True
        else:
            return False

    def get_all_messages(self, user: UserObj):
        return self.__message_repo.get_all_messages(user_name=user.get_username())

    def get_all_unread_messages(self, user: UserObj):
        return self.__message_repo.get_all_unread_messages(user_name=user.get_username())

    def delete_message(self, message: MessageObj, user: UserObj):
        return self.__message_repo.delete_message(user_name=user.get_username(), message=message)

    def check_auth_user(self, user):
        return self.__user_repo.validate_user(user)

    def check_username(self, username):
        return self.__user_repo.is_username_exist(user_name=username)

    def register_user(self, user: UserObj):
        if not self.check_username(username=user.get_username()):
            return self.__user_repo.add_user(user=user)
        else:
            return False

    def get_user(self, user_name):
        return self.__user_repo.get_user(user_name=user_name)
