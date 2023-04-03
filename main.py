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

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


# example: response html code
@app.get("/", response_class=HTMLResponse)  # home
def root(request: Request):
    return templates.TemplateResponse('home.html', {'request': request, 'msg': 'FAST SPACE!'})


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
