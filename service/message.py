from s3_client import S3Client
from db_client import MongoClient

class Message:


    def __init__(self):
        pass

    def send(self):
        from collection.message import Message
        from flask import request
        json = request.get_json()
        message = Message(json)

        s3_client = S3Client(request=request)
        form_name = next(request.files.keys())
        if form_name:
            s3_client.upload_file(form_name)
        MongoClient().insert_one(message)


    def recv(self):
        pass