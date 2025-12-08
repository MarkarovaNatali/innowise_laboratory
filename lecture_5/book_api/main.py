from fastapi import FastAPI
from  Books.views import router as books_router

app = FastAPI()
app.include_router(books_router)


