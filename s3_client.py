from flask import request
class S3Client:

    def __init__(self,**kwargs):
        self.ACCESS_KEY_ID = kwargs.get("access_key_id","AKIAZQQLHJM3VYTL2LWR")
        self.ACCESS_KEY_PASSWD = kwargs.get("access_key_passwd", "PMLUCrm67HGygjGEOqD0uFna14UlvXOOGTNOM5h1")
        self.BUCKET_NAME = kwargs.get("bucket_name", "glassletter")
        self.REGION_NAME = kwargs.get("region_name","ap-northeast-2")
        self.request = kwargs.get("request")

    def upload_file(self,form_name):
        try:
            from boto3.session import Session
            session = Session(aws_access_key_id=self.ACCESS_KEY_ID,
                              aws_secret_access_key=self.ACCESS_KEY_PASSWD, region_name=self.REGION_NAME)
            s3 = session.resource("s3")
            bucket = s3.Bucket(self.BUCKET_NAME)

            filename = "{source}/{target}/{base_file}".format(source=self.request.form['source'],
                                                             target=list(self.request.form['target'].values()).pop(0),
                                                             base_file=self.request.files[form_name].filename)

            """
            key 명명 규칙은 source/target/filename
            """

            s3_object = bucket.put_object(Key=filename, Body=request.files[form_name])
            end_point = s3_object.meta.client._endpoint.host[s3_object.meta.client._endpoint.host.find("s3"):]
            s3_url = f"https://{self.BUCKET_NAME}.{end_point}/{filename}"
            print(s3_url)
            return s3_url
        except Exception as e:
            print(e)

if __name__ == '__main__':
    s3 = S3Client()
    import boto3
    from boto3.session import Session

    session = Session(aws_access_key_id=s3.ACCESS_KEY_ID,
                      aws_secret_access_key= s3.ACCESS_KEY_PASSWD, region_name= s3.REGION_NAME)
    s3_client = session.resource("s3")
    bucket = s3_client.Bucket(s3.BUCKET_NAME)
    bucket.download_file(bucket=s3.BUCKET_NAME,filename="tester/01029209599/kira.png")
