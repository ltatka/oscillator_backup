from os.path import join
import pymongo
from bson.json_util import dumps


astr = "mongodb+srv://data:VuRWQ@networks.wqx1t.mongodb.net"
client = pymongo.MongoClient(astr)
database_names = client.list_database_names()
db = client['networks']
db = client.networks
collection = db['networks']
cur = collection.find({})

def backup_db(backup_db_dir):
    collections = db.collection_names()
    for i, collection_name in enumerate(collections):
        col = getattr(db, collections[i])
        collection_ = col.find()
        jsonpath = collection_name + ".json"
        jsonpath = join(backup_db_dir, jsonpath)
        with open(jsonpath, 'wb') as jsonfile:
            jsonfile.write(dumps(collection_).encode())

backup_db('.')