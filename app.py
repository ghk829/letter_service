from flask import Flask, request
import boto3
from constant import *
from s3_client import S3Client
from db_client import MongoClient
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app, resources={
  r"/register/*": {"origin": "*"},
  r"/sendmessage/*": {"origin": "*"},
})

@app.route('/')
def index():
    return '''<form method=POST enctype=multipart/form-data action="sendmessage">
    <input name="target" value="아빠에게"> <br>
    <input name="message" value="아빠 사랑해요"> <br>
    <input type=file name=myfile> <br>
    <input type=submit>
    </form>
    
    <form method=POST enctype=multipart/form-data action="sendmessage">
    <input name="target" value="아빠에게"> <br>
    <input name="message" value="아빠 사랑해요"> <br>
    <input type=file name=myfile> <br>
    <input type=submit>
    </form>
    
    
    '''

@app.route('/register', methods=['POST'])
def register():
    try:
        from service.register import Register
        service = Register()
        service.insert_one()
    except Exception as e:
        print(e)
    return ""


@app.route('/sendmessage', methods=['POST'])
def sendmessage():
    from service.message import Message
    service = Message()
    service.send()
    return ""

@app.route('/viewmessage', methods=['GET'])
def viewmessage():
    from service.message import Message
    service = Message()
    result = service.recv()
    import json
    return json.dumps(result,ensure_ascii=False)


@app.route('/updatemessage', methods=['POST'])
def updatemessage():
    pass


@app.route('/deletemessage', methods=['DELETE'])
def deletemessage():
    pass

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
