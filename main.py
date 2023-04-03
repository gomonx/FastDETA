# FastAPI on DETA python 3.9

# - commands
# edit python Interpreter
# pip install fastapi
# pip install "uvicorn[standard]"

# - make requirements.txt
# pip install pipreqs
# pipreqs

# - develop serve
# > uvicorn main:app --reload

# - deploy on Deta cloud.
# Sing up & create default project first!
# read > https://fastapi.tiangolo.com/deployment/deta/

from typing import Union

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()


# example: response html code
@app.get("/", response_class=HTMLResponse)  # home
def root():
    return """
    <html>
        <head>
            <title>Fast DETA</title>
        </head>
        <body>
            <h1>Welcome to Fast SPACE!</h1>
            <h2>deploy on <a href="https://deta.space/" target="_blank">Deta cloud</a></h2>
            <h3><a href="/docs">read Docs..</a></h3>
        </body>
    </html>
    """


# example: response json data
@app.get("/v")  # check Version
def version():
    return {"version": "1.0"}


class Item(BaseModel):
    name: str
    desc: Union[str, None] = None  # python 3.6 -> 3.9 use Union
    price: float


# example: post request
@app.post("/items")
def create_item(item: Item):
    return item
