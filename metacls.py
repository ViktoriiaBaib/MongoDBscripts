from pymongo import MongoClient
from pprint import pprint

SynDev_client = MongoClient(

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

