def test():
    import pymongo

    conn = pymongo.MongoClient("mongodb://colten:1q2w3e4r5t@ds231207.mlab.com:31207/heroku_21zzgr5h")
    db = conn['heroku_21zzgr5h']
    collection = db['test']
    import datetime
    test = {
        "user_id":"abc",
        "message":"hello world",
        "date":datetime.datetime.utcnow()
    }
    test_id = collection.insert_one(test).inserted_id
    print(test_id)
if __name__ == '__main__':
    test()