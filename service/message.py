from s3_client import S3Client
from db_client import MongoClient

class Message:


    def __init__(self):
        pass

    def send(self):
        from collection.message import Message
        from flask import request

        message = Message(**request.form)

        s3_client = S3Client(request=request)
        try:
            form_name = next(request.files.keys())
            s3_url = s3_client.upload_file(form_name)
            message.set("url",s3_url)
        except StopIteration as e:
            print(e)
        finally:
            MongoClient().insert_one(message)



    def recv(self):
        pass