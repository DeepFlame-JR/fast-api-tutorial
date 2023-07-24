from fastapi import FastAPI
from .controllers.hello_controller import router as hello_router
from .controllers.item_controller import router as item_router
from .controllers.user_controller import router as user_router

app = FastAPI()
app.include_router(hello_router, prefix="/hello", tags=["hello"])
app.include_router(item_router, prefix="/items", tags=["items"])
app.include_router(user_router, prefix="/items", tags=["users"])

