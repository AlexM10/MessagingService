from Model.models import Message
from Model.database_setup import session
from Model.message_obj import MessageObj
from sqlalchemy import or_, and_


class MessageRepository(object):

    def create_message_obj(self, message: Message):
        return MessageObj(sender=message.sender, receiver=message.receiver,
                          subject=message.subject, message=message.message,
                          time_stamp=message.timestamp, message_id=message.id)

    def add_message(self, message: MessageObj):
        message = Message(receiver=message.get_receiver(), sender=message.get_sender(),
                          subject=message.get_subject(), message=message.get_message(),
                          timestamp=message.get_time_stamp())
        session.add(message)
        session.commit()

    def get_all_messages(self, user_name):
        messages = session.query(Message).filter(or_(Message.receiver == user_name, Message.sender == user_name)).all()
        messages_list = []
        for message in messages:
            messages_list.append(self.create_message_obj(message).serialize())
        return messages_list

    def get_all_unread_messages(self, user_name):
        messages = session.query(Message).filter(and_(Message.is_read == False, Message.receiver == user_name)).all()
        messages_list = []
        for message in messages:
            messages_list.append(self.create_message_obj(message).serialize())
        return messages_list

    def get_message(self, user_name):
        message = session.query(Message).filter(Message.receiver == user_name).first()
        if message is not None:
            return self.create_message_obj(message=message)
        else:
            return None

    def delete_message(self, user_name, message):
        ret_message = session.query(Message).filter(
            (or_(Message.sender == user_name, Message.receiver == user_name))).filter(Message.message == message.get_message()).first()
        if ret_message is not None:
            session.delete(ret_message)
            return True
        else:
            return False

    def edit_message_is_read(self, message_id):
        session.query(Message) \
            .filter(Message.id == message_id) \
            .update({Message.is_read: True})
