from flask import request
class S3Client:

    def __init__(self,**kwargs):
        self.ACCESS_KEY_ID = kwargs.get("access_key_id","AKIAZQQLHJM3VYTL2LWR")
        self.ACCESS_KEY_PASSWD = kwargs.get("access_key_passwd", "PMLUCrm67HGygjGEOqD0uFna14UlvXOOGTNOM5h1")
        self.BUCKET_NAME = kwargs.get("bucket_name", "glassletter")
        self.REGION_NAME = kwargs.get("region_name","ap-northeast-2")
        self.request = kwargs.get("request")

    def upload_file(self,formname):
        try:
            from boto3.session import Session
            session = Session(aws_access_key_id=self.ACCESS_KEY_ID,
                              aws_secret_access_key=self.ACCESS_KEY_PASSWD, region_name=self.REGION_NAME)
            s3 = session.resource("s3")
            bucket = s3.Bucket(self.BUCKET_NAME)

            filename = request.files[formname].filename

            """
            key 명명 규칙은 source/target/filename
            """

            s3_object = bucket.put_object(Key=filename, Body=request.files[formname])
            end_point = s3_object.meta.client._endpoint.host[s3_object.meta.client._endpoint.host.find("s3"):]
            s3_url = f"htts://{self.BUCKET_NAME}.{end_point}/{filename}"
            print(s3_url)
            return s3_url
        except Exception as e:
            print(e)