from pymongo import MongoClient

import config


class ConectDb:
    def __init__(self):
        self.client = MongoClient(config.MONGO_URL)
        self.db = self.client[config.MONGO_DB]

    def addDocument(self, **kwargs):

        try:
            tutorial = self.db[config.MONGO_COLLECTIONS]
            result = tutorial.insert_one(kwargs)
            print(f"Document insert in: {result}")
        except Exception as e:
            print(e)

    def changeconfiguration(self, loadingConfig):
        tutorial = self.db[config.MONGO_CONFIG_COLLECTION]
        myquery = {"_id": 1}
        documents = tutorial.count_documents(myquery)
        if documents == 0:
            print("add new Document")
            tutorial.insert_one({"_id": 1, "isLoading": loadingConfig})
        else:
            newvalues = {"$set": {"isLoading": loadingConfig}}
            update = tutorial.update_one(myquery, newvalues)
            print("set configuration")
        return update.raw_result['ok']
