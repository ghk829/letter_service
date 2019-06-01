class MongoClient:


    def __init__(self,**kwargs):

        self.URL = kwargs.get("db_url","mongodb://colten:1q2w3e4r5t@ds231207.mlab.com:31207/heroku_21zzgr5h")
        self.DATABASE = kwargs.get("database","heroku_21zzgr5h")
        self.collection = kwargs.get("collection","test")
        self.conn = self.get_session()

    def get_session(self):
        import pymongo
        conn = pymongo.MongoClient(self.URL)
        db = conn[self.DATABASE]
        return db[self.collection]

    def create(self):
        pass

    def retrive(self,query):
        result = []
        cursor = self.conn.find(query)

        try:
            while True:
                tmp = cursor.next()
                tmp.pop("_id")
                result.append(tmp)

        except StopIteration as e:
            print(e)

        finally:
            return result



    def insert_one(self,data):
        if hasattr(data,"__dict__"):
            result_id = self.conn.insert_one(data.__dict__).inserted_id
        elif type(data) == dict:
            result_id = self.conn.insert_one(data).inserted_id
        print(result_id)

    def delete(self):
        pass

if __name__ == '__main__':
    conn = MongoClient(collection="message")
    result = conn.retrive({})
    print(result)
    print(len(result))