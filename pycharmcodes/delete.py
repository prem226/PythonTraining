import sys
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def main():
        myclient = MongoClient("mongodb://%s:%s@127.0.0.1" % ("premchand", "root"))
        print("Connection successfull", myclient)

        #myquery = {'name'='prem', 'roll_number' = 29}


if __name__ == '__main__':
    main()
