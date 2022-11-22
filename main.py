# FastAPI on DETA

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


class Item(BaseModel):
    name: str
    desc: Union[str, None] = None
    price: float


@app.get("/", response_class=HTMLResponse)  # home
def root():
    return """
    <html>
        <head>
            <title>Fast DETA</title>
        </head>
        <body>
            <h1>Welcome to Fast DETA!</h1>
            <h2>deploy on <a href="https://www.deta.sh" target="_blank">Deta cloud</a></h2>
            <h3><a href="/docs">read Docs..</a></h3>
        </body>
    </html>
    """


@app.get("/v")  # check Version
def version():
    return {"version": "1.0"}


@app.post("/items")
def create_item(item: Item):
    return item
