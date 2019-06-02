
class Register:

    def __init__(self):
        self.get_user()


    def get_user(self):
        from collection.user import User
        from flask import request
        json = request.get_json()
        if json:
            user = User(**json)
            self.user = user

    def insert_one(self):

        if hasattr(self,"user"):
            from db_client import MongoClient
            client = MongoClient(collection="user")
            client.insert_one(self.user)


    def insert_after(self,user_obj):
        from db_client import MongoClient
        client = MongoClient(collection="user")
        client.insert_one(user_obj)