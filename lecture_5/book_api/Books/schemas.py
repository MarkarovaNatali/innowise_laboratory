from pydantic import BaseModel

class New_Book(BaseModel):
    "id": int
    "title": str
    "author": str
    "year": int
    "pages": int
