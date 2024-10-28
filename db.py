import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

USERNAME = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")

uri = f"mongodb+srv://{USERNAME}:{PASSWORD}@dhaageenacluster.fxpsk58.mongodb.net/?retryWrites=true&w=majority&appName=DhaageenaCluster"

class IbayListingsDB:
    def __init__(self):
        self.client = MongoClient(uri, server_api=ServerApi('1'))
        self.database = self.client["ibay"]
        self.collection = self.database["ibay"]

    def get_listings(self):
        listings = self.collection.find({}) 
        
        return [{
            "name": each["name"],
            "price": each["price"],
            "description": each["description"],
            "link": each["link"],
            "image": each["image"],
            "category": each["category"],
            "location": each["location"],
            "info": each["info"]
        } for each in listings]

    def get_number_of_listings(self):
        listings = self.collection.find({})
        return len(list(listings))

if __name__ == "__main__":
    db = IbayListingsDB()