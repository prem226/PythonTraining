
import sys
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

myclient = MongoClient("mongodb://%s:%s@127.0.0.1"%("premchand","root"))

mydb = myclient['database']
mycollection = mydb['myTable']

profiles = [
    {"user":"ram", "title":"python"},
    {"user":"prem", "title":"js"},
    {"user":"shivba", "title":"c++"},
    {"user":"vikrant", "title":"Mongodb"},
    {"user":"sanju", "title":"perl"}
]

#mycollection.insert_many(profiles)
#print("Successful!")
agg_result  = mycollection.aggregate(
    [
        {
            "$group":
                {
                    "_id":"$title",
                    "num_lang":{"$sum":1}
                }
        }
    ]
)
print("result: \n")
for i in agg_result:
    print(i)