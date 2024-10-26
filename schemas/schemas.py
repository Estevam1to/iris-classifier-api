from pydantic import BaseModel


class Request(BaseModel):
    SepalLengthCm: float
    SepalWidthCm: float
    PetalLengthCm: float
    PetalWidthCm: float


class Response(BaseModel):
    category: str
