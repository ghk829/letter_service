from s3_client import S3Client
from db_client import MongoClient

class Message:


    def __init__(self):
        pass

    def send(self):
        from collection.message import Message
        from flask import request
        if request.content_type.startswith("application/json"):
            message = Message(**request.get_json())
        else:
            message = Message(**request.form)
        s3_client = S3Client(request=request)
        try:
            form_name = next(request.files.keys())
            s3_url = s3_client.upload_file(form_name)
            message.set("url",s3_url)
        except StopIteration as e:
            print(e)
        finally:
            MongoClient(collection="message").insert_one(message)
            user = next(MongoClient(collection="user").retrive({"user_id":message.source}))
            user.add_message(message)
            MongoClient(collection="user").update_one({"user_id":message.source},
                                                      {"$set": {"messages": user.messages}})


    def recv(self):
        from flask import request
        source = request.args.get("source")
        return MongoClient(collection="message").retrive({"source":source})