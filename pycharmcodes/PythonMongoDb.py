
import sys
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


def main():
        try:
                myclient = MongoClient("mongodb://%s:%s@127.0.0.1" % ('premchand', 'root'))
                print("connection successful", myclient)

                # list down the databases
                list_of_db = myclient.list_database_names()
                print("databases available in mongodb", list_of_db)

                mydb = myclient['Prac']
                mycol = mydb['myTable']

                # myDict = {"Name":"Prem", "Roll":29}
                # n = mycol.insert_one(myDict)
                # print(n.inserted_id)

                # myList = [
                #     {"Name":"Prem", "Roll":29},
                #     {"Name":"Shivba", "Roll":40},
                #     {"Name":"Vikrant", "Roll":26},
                #     {"Name":"Sanju", "Roll":11}
                # ]
                # x = mycol.insert_many(myList)
                # print(x.inserted_ids)

                myQuery = {"Name":"Prem"}
                for record in mycol.find():
                    print(record)





               #  mydb = myclient['Student']
               #  print("Database created!")
               #  collection = mydb['student']
               #  record = {
               #       "_id":0,
               #       "name": "Prem",
               #       "roll_number": 29,
               #       "branch": "IT",
               #       "marks": 65
               #  }
               #  record_1 = collection.insert_one(record)
               # print("records: ", record_1)







        except ConnectionFailure as e:
                print("\n\t Error :=", e)


if __name__ == '__main__':
    main()
