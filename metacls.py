from pymongo import MongoClient
import configparser
config = configparser.ConfigParser()
config.read('config.ini')

mongo_config = config['SynDev']
server = mongo_config['server']
username = mongo_config['username']
password = mongo_config['password']
authSource = mongo_config['authSource']
authMechanism = mongo_config['authMechanism']

SynDev_client = MongoClient(
    server,
    username=username,
    password=password,
    authSource=authSource,
    authMechanism=authMechanism
)

syndev_db = SynDev_client.SynDev
collection = syndev_db.ElsevierParagraphs
new_collection = syndev_db.ElsevierParagraphsMeta

query = {"classification": {"$regex": "synthesis", "$options": "i"}}
syntdocs = [doc for doc in new_collection.find(query)]
syntids =[str(doc["_id"]) for doc in syntdocs]
syntcls =[str(doc["classification"]) for doc in syntdocs]

with open("meta_synt_ids.txt","w") as f:
    f.write(", ".join(syntids))
with open("meta_synt_cls.txt","w") as f:
    f.write(", ".join(syntcls))

