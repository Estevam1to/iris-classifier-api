from fastapi import FastAPI

from routes import predict

app = FastAPI(predict.router)
