from flask import Flask, request
import boto3
from constant import *
from s3_client import S3Client
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
    s3_client = S3Client(request=request)
    s3_client.upload_file()
    return '<h1>File saved to S3</h1>'


@app.route('/sendmessage', methods=['POST'])
def register():
    s3_client = S3Client(request=request)
    s3_client.upload_file("myfile")
    return '<h1>File saved to S3</h1>'

@app.route('/viewmessage', methods=['GET'])
def register():
    s3_client = S3Client(request=request)
    s3_client.upload_file()
    return '<h1>File saved to S3</h1>'


if __name__ == '__main__':
    app.run(debug=True)