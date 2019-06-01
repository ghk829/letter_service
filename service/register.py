
class Register:

    def __init__(self):
        self.get_user()


    def get_user(self):
        from collection.user import User
        from flask import request
        json = request.form
        user = User(**json)
        self.user = user

    def insert_one(self):

        if hasattr(self,"user"):
            from db_client import MongoClient
            client = MongoClient()
            client.insert_one(self.user)