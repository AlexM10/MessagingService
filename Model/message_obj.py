from datetime import datetime


class MessageObj(object):

    def __init__(self, sender, receiver, subject, message, time_stamp=datetime.now()
                 , message_id=None):
        self.id = message_id
        self.__sender = sender
        self.__receiver = receiver
        self.__subject = subject
        self.__message = message
        self.__time_stamp: datetime = datetime.strptime(time_stamp, '%a, %d %b %Y %H:%M:%S %Z') if (type(time_stamp) is str) else time_stamp
    ''
    def get_sender(self):
        return self.__sender

    def get_receiver(self):
        return self.__receiver

    def get_subject(self):
        return self.__subject

    def get_message(self):
        return self.__message

    def get_time_stamp(self):
        return self.__time_stamp

    def serialize(self):
        return {
            'sender': self.__sender,
            'receiver': self.__receiver,
            'subject': self.__subject,
            'message': self.__message,
            'timestamp': self.__time_stamp,
        }
