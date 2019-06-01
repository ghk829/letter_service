class User:
    user_id = ""
    user_name = ""
    password = ""
    messages = []

    def __init__(self,**kwargs):
        for k,v in kwargs:
            setattr(self,k,v)

    def add_message(self,message):
        self.messages.append(message)
