import numpy as np
from fastapi import APIRouter, Depends, HTTPException
from http import HTTPStatus

from schemas.schemas import Request, Response
from utils.prediction import Prediction
from config.security import get_current_user
from domain.models_db import User

router = APIRouter(prefix="/api/predict", tags=["Predict"])

prediction = Prediction()


@router.post(path="/", status_code=200, response_model=Response)
async def predict_endpoint(
    request: Request,
    user_id: int,
    current_user: User = Depends(get_current_user),
) -> Response:
    if current_user.id != user_id:
        raise HTTPException(status_code=HTTPStatus.FORBIDDEN, detail="Unauthorized")

    try:
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
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))
