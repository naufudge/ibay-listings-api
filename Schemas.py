from pydantic import BaseModel
from typing import Dict
import bson 


class Listing(BaseModel):
    _id: bson.BSON
    name: str
    price: float
    description: str
    link: str
    image: str
    category: str
    location: str
    info: Dict[str, str]