import numpy as np
from fastapi import APIRouter

from schemas.schemas import Response, Request
from model.prediction import Prediction

router = APIRouter(prefix="/api/predict", tags=["Predict"])

prediction = Prediction()


@router.post(path="/", status_code=200, response_model=Response)
async def predict_endpoint(request: Request) -> Response:
    values = np.array(
        [
            request.SepalLengthCm,
            request.SepalWidthCm,
            request.PetalLengthCm,
            request.PetalWidthCm,
        ]
    )

    category = prediction.predict(values)

    return Response(category=category)
