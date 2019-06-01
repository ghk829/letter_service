BUCKET_NAME = 'letterservice'
ACCESS_KEY_ID = "AKIA2UVP3YJ46MD3BZ2Z"
ACCESS_KEY_PASSWD = "rT8PBBDw32ASlGkAKq1j96I5dLy7I981Jl8ahffE"

def test():
    from boto3.session import Session
    session = Session(aws_access_key_id=ACCESS_KEY_ID,
                      aws_secret_access_key=ACCESS_KEY_PASSWD,region_name="us-east-1")
    s3 = session.resource("s3")
    bucket = s3.Bucket('letterservice')
    with open("README.md","r") as f:
        df = bucket.put_object(Key="test/README.md",Body=f.read())
        print(df)

if __name__ == '__main__':
    test()