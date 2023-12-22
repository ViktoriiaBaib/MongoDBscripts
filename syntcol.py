from pymongo import MongoClient
import configparser
from bson import ObjectId
config = configparser.ConfigParser()
config.read('config.ini')

print("Connecting to DB...")

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

print("Reading IDs...")
with open(f"meta_synt_ids.txt","r") as file:
    line = file.readline()
sections = [ObjectId(word) for word in line.split(', ')]

print("Reading Class")

documents = [doc for section in sections for doc in collection.find({"_id":section})]