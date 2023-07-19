from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None): # Union: 리스트 안에 들어간 type은 모두 받을 수 있음
    return {"item_id": item_id, "q": q}