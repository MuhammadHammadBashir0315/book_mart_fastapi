from fastapi import FastAPI
from typing import Optional
from src.books.routes import book_router
from contextlib import asynccontextmanager
from src.db.main import init_db

@asynccontextmanager
async def life_span(app:FastAPI):
    print(f"Server is starting ")
    await init_db()
    yield
    print(f"Server is stopped")

version = "V1"

app = FastAPI(
    title="Booky",
    description="A REST API for book review web service",
    version=version,
    lifespan=life_span
)

app.include_router(book_router , prefix=f"/api/{version}/books", tags=['Books'])

@app.get('/')
async def read_root():
    return {'message':'Welcome to the fastapi'}

@app.get('/greet/{name}')
async def greet_name(name: str) -> dict:
    return {"greeting" : f"Welcome {name} "}

#without the optional keyword and default value the query parameter will be mendatory but with optional keyword and default value it will be optional
@app.get('/greet')
async def greet_query_name(name: Optional[str] = "User", age: int = 0) -> dict:
    return {'greeting' : f"Welcome {name}", "age":age}

