# MessagingService
A messaging service which recive, return and save messages
## requirements:
    pip3 install -r requirements.txt
## how to run
to use the service a user needs tor register 
and then to login by
   POST: register https://messagehandlerservice.herokuapp.com//signup?username=<username>&password=<password>
   POST: login https://messagehandlerservice.herokuapp.com//login?username=<username>&password=<password>
after finishing the session a user can log out with this request
   POST: logout https://messagehandlerservice.herokuapp.com//logout?username=<username>&password=<password>
to use the messages api:
    write: the writing user must be the sender of the message and a reciever must be registered in the 
           system.
           url: POST https://messagehandlerservice.herokuapp.com//message?username=<username>&password=<password>&request=write
           message: {
                    "message": "message body three",
                    "receiver": "user2",
                    "sender": "user1",
                    "subject": "message subject three",
                    "timestamp": "Fri, 09 Oct 2020 23:01:26 GMT"
                    }
                
    read: GET https://messagehandlerservice.herokuapp.com//message?username=<username>&password=<password>&request=read
    delete: to delete a user must an owner of the message and send the message that he wants to delete from the service.
           url: POST https://messagehandlerservice.herokuapp.com//message?username=<username>&password=<password>&request=delete
           message: {
                    "message": "message body three",
                    "receiver": "user2",
                    "sender": "user1",
                    "subject": "message subject three",
                    "timestamp": "Fri, 09 Oct 2020 23:01:26 GMT"
                    }
    get all message: retuens all the messages of a specific user.
                    url: GET https://messagehandlerservice.herokuapp.com//messages?username=<username>&password=<password>&request=get_all
     
    get all unread messages: returns all the message of the user that he didn't read yet.
                    url: GET https://messagehandlerservice.herokuapp.com//messages?username=<username>&password=<password>&request=get_all_unread
