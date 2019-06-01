from flask import Flask, request
import boto3
from constant import *
from s3_client import S3Client
from db_client import MongoClient
app = Flask(__name__)

@app.route('/')
def index():
    return '''<form method=POST enctype=multipart/form-data action="register">
    <input name="say" value="Hi">
    <input name="to" value="Mom">
    <input type=file name=myfile>
    <input type=submit>
    </form>'''

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
    s3_client = S3Client(request=request)
    s3_client.upload_file()
    return ""


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
