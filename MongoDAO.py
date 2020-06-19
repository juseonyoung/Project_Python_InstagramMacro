from pymongo import MongoClient


class MongoDAO :
    reply_list = []

    def __init__(self):

        self.client = MongoClient('127.0.0.1',27017)
        self.db = self.client['local']
        self.collection = self.db.get_collection('test_0619')

    def mongo_write(self, data):
        print('MongoDB Write Data')
        self.collection.insert(data)

    def mongo_select_all(self):
        for one in self.collection.find({}, {'_id':0,'content':1,'score':1}):
            self.reply_list.append([one['title'], one['content'],one['score']])
        return self.reply_list