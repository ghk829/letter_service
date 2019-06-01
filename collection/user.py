class User:
    user_id = ""
    user_name = ""
    phone = ""
    password = ""
    messages = []

    def __init__(self,**kwargs):
        for k,v in  kwargs.items():
            setattr(self,k,v)

    def set(self,key,value):
        setattr(self,key,value)

    def add_message(self,message):
        self.messages.append(message)
