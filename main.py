from fastapi import FastAPI
from enum import Enum
from typing import Optional
from router import blog_get, item_get

app = FastAPI()

app.include_router(blog_get.router)
app.include_router(item_get.router)

@app.get("/")
def index():
    return "Hello...!"

