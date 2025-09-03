from pymongo import MongoClient
import pandas as pd
import os

class ConnexionMongo:
    @staticmethod
    def connexion_mongo():
        client = MongoClient(os.getenv("connectMongoDB"))
        db = client["test"]
        collection = db["restaurants"]
        df = pd.DataFrame(list(collection.find()))
        return df