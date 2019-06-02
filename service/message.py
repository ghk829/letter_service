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
            message = Message(**request.form.to_dict())
        s3_client = S3Client(request=request)
        try:
            form_name = next(request.files.keys())
            s3_url = s3_client.upload_file(form_name)
            message.set("url",s3_url)
            message.set("type",request.files[form_name].content_type)
        except StopIteration as e:
            print(e)
        finally:
            object_id = MongoClient(collection="message").insert_one(message)
            user_query = MongoClient(collection="user").retrive({"user_id": message.source})
            if len(user_query) > 0:
                user = user_query.pop(0)
                from collection.user import User
                user = User(**user)
                user.add_message(object_id)
                MongoClient(collection="user").update({"user_id":message.source},
                                                      {"$set": {"messages": user.messages}})
            else:
                from service.register import Register
                from collection.user import User
                user = User()
                user.set("user_id",message.source)
                user.add_message(object_id)
                Register().insert_after(user)

    def recv(self):
        from flask import request
        source = request.args.get("user_id")
        return MongoClient(collection="message").retrive({"source": source})


    def update(self):
        from collection.message import Message
        from flask import request
        json = request.get_json()
        from bson.objectid import ObjectId
        message_id = json['id']
        message_id = ObjectId(message_id)
        message = MongoClient(collection="message").retrive({"_id": message_id})
        if "text" in json:
            object_id = MongoClient(collection="message").update({"_id": message_id},
                                              {"$set": {"text": json['text']}})
        return object_id

    def delete(self):
        from collection.message import Message
        from flask import request
        json = request.get_json()
        from bson.objectid import ObjectId
        message_id = json['id']
        message_id = ObjectId(message_id)
        message = MongoClient(collection="message").delete({"_id": message_id})

