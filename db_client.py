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
                message_id = tmp.pop("_id")
                tmp['id'] = str(message_id)
                result.append(tmp)

        except StopIteration as e:
            print(e)

        finally:
            return result

    def update(self,filter,update_query):
        object_id = self.conn.update_one(filter=filter,update=update_query)
        return str(object_id)

    def insert_one(self,data):
        if hasattr(data,"__dict__"):
            object_id = self.conn.insert_one(data.__dict__).inserted_id
        elif type(data) == dict:
            result_id = self.conn.insert_one(data).inserted_id
        print(object_id)
        return str(object_id)

    def delete(self,filter):
        try:
            self.conn.delete_one(filter)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    conn = MongoClient(collection="message")
    result = conn.retrive({})
    print(result)
    print(len(result))