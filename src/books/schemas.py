from pydantic import BaseModel
from datetime import datetime
import uuid

class Book(BaseModel):
    uid : uuid.UUID
    title : str
    author : str
    publisher : str
    publish_date : str
    page_count : int
    language : str
    created_at : datetime
    update_at : datetime

class BookCreateModel(BaseModel):
    title : str
    autjor : str
    publisher : str
    published_date : str
    page_count : int
    language : str

class BookUpdateModel(BaseModel):
    title : str
    author : str
    publisher : str
    page_count : int
    language : str