from fastapi import FastAPI
from db import IbayListingsDB

app = FastAPI()

DB = IbayListingsDB()

@app.get("/")
async def root():
    return {"Number of Listings": DB.get_number_of_listings()}

@app.get("/listings")
async def get_listings():
    return DB.get_listings()

