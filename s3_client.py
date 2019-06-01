class S3Client:

    def __init__(self,**kwargs):
        self.ACCESS_KEY_ID = kwargs.get("access_key_id","AKIA2UVP3YJ46MD3BZ2Z")
        self.ACCESS_KEY_PASSWD = kwargs.get("access_key_passwd", "rT8PBBDw32ASlGkAKq1j96I5dLy7I981Jl8ahffE")
        self.BUCKET_NAME = kwargs.get("bucket_name", "glassletter")
        self.request = kwargs.get("request")

    def upload_file(self):
        try:
            from boto3.session import Session
            session = Session(aws_access_key_id=self.ACCESS_KEY_ID,
                              aws_secret_access_key=self.ACCESS_KEY_PASSWD, region_name=self.REGION_NAME)
            s3 = session.resource("s3")
            bucket = s3.Bucket(self.BUCKET_NAME)

            filename = ""

            """
            key 명명 규칙은 source/target/filename
            """

            bucket.put_object(Key=filename, Body=self.request.files)

        except Exception as e:
            print(e)