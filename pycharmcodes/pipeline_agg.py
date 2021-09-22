import sys
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

myclient = MongoClient("mongodb://%s:%s@127.0.0.1" % ("premchand","root"))
mydb = myclient['database']
mycollection = mydb['test1']

data = [
    # {"x":1, "tags":["dog","cat"]},
    # {"x":2, "tags":["cat"]},
    # {"x":2, "tags":["mouse","cat", "dog"]},
    # {"x":3, "tags":["Horse","Monkey"]}
    # {"x":4, "tags":["Horse", "Lion"]},
    {"x":5, "tags":["Monkey","Tiger"]}
]

result = mycollection.insert_many(data)

from bson.son import SON

pipeline = [
    {"$unwind":"$tags"},  #1 make flat hierarchy
    {
        "$group":{"_id":"$tags", "count":{"$sum":1}}  #2 actual aggregation
    },
    {
        "$sort":SON([("count",-1),("_id",-1)])  #3 display
    }
]

import pprint
pprint.pprint((list(mycollection.aggregate(pipeline))))
