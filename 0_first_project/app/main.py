from fastapi import FastAPI
from .controllers.hello_controller import router as hello_router
from .controllers.item_controller import router as item_router

app = FastAPI()
app.include_router(hello_router, prefix="/hello", tags=["hello"])
app.include_router(item_router, prefix="/items", tags=["items"])
