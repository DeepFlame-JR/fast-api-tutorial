from typing import Annotated, Union
from fastapi import APIRouter
from fastapi.params import Body, Path, Query

from ..models.item import Item
from ..models.user import User

router = APIRouter()

@router.post("/")
async def create_item(item: Item) -> Item:
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax":price_with_tax})
    return item_dict

# String Validation
@router.get("/")
async def read_items(q: Annotated[str | None, Query( # 주석
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
            deprecated=True,
        ),] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Integer Validation
@router.get("/{item_id}", response_model=Item)
async def read_item(
    *,  # 원래는 기본값이 없는 매개변수를 앞에 둬야하나, *를 통해서 그 순서를 상관하지 않아도 됨
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)] , # Path 매개변수 (0 <= item_id <= 1000)
    q: str,
    size: float = Query(gt=0, lt=10.5),  # Query 매개변수 (0 < size < 10.5)
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

# Get Multiple Body
"""
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    },
    "importance": 5
}
"""
@router.put("/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Annotated[Item, Body(
        examples=[
            {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            },
            {
                "name": "Bar",
                "price": "35.4",
            },
            {
                "name": "Baz",
                "price": "thirty five point four",
            },
        ]        
    )
    ],
    user: User,
    importance: Annotated[int, Body(gt=0)],
    q: str | None = None,
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results