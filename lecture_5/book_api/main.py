from fastapi import FastAPI

from books.models import Base
from books.database import engine

from books.crud import router as books_crud
from books.routers.books_views import router as books_router

app = FastAPI()
app.include_router(books_crud, tags=["books"])
app.include_router(books_router, tags=["books"])

Base.metadata.create_all(bind=engine)
