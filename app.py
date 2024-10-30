from fastapi import FastAPI

from src.routes import predict, auth, user
from src.config.database import create_all

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    create_all()


app.include_router(predict.router)
app.include_router(auth.router)
app.include_router(user.router)
