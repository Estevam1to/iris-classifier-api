from pydantic import BaseModel, model_validator


class Request(BaseModel):
    SepalLengthCm: float
    SepalWidthCm: float
    PetalLengthCm: float
    PetalWidthCm: float

    @model_validator(mode="after")
    def check_values(cls, values):
        if values.SepalLengthCm < 0:
            raise ValueError("SepalLengthCm must be greater than 0")
        if values.SepalWidthCm < 0:
            raise ValueError("SepalWidthCm must be greater than 0")
        if values.PetalLengthCm < 0:
            raise ValueError("PetalLengthCm must be greater than 0")
        if values.PetalWidthCm < 0:
            raise ValueError("PetalWidthCm must be greater than 0")

        return values


class UserSchema(BaseModel):
    username: str
    email: str
    password: str


class UserPublic(BaseModel):
    username: str
    email: str


class Response(BaseModel):
    category: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
