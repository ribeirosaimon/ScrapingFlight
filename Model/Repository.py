from pymongo import MongoClient
import config


class ConectDb:
    def __init__(self):
        self.client = MongoClient(config.MONGO_URL)

    def addDocument(self, **kwargs):
        db = self.client[config.MONGO_DB]
        tutorial = db[config.MONGO_COLLECTIONS]
        try:
            result = tutorial.insert_one(kwargs)
            print(f"Document insert in: {result}")
        except Exception as e:
            print(e)
