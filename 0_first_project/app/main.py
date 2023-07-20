from fastapi import FastAPI
from controllers.hello_controller import router as hello_router

app = FastAPI()
app.include_router(hello_router, prefix="/hello", tags=["hello"])
