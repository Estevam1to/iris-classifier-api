import pickle

import numpy as np
from fastapi import APIRouter

from schemas.schemas import Response, Request

router = APIRouter(prefix="/api/predict", tags=["Predict"])


async def predict(values: np.array) -> Response:
    with open("path/modelo.pkl", "rb") as file:
        model = pickle.load(file)

    pred = model.predict(values.reshape(1, -1))[0]

    return Response(category=pred)


@router.post(path="/", status_code=200, response_model=Response)
async def predict_endpoint(request: Request) -> Response:
    values = np.array(
        [
            request.SepalLengthCm,
            request.SepalWidthCm,
            request.PetalLengthCm,
            request.PetalWidthCm
         ]
    )

    response = await predict(values)
    return response
