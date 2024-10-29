from http import HTTPStatus

import numpy as np
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from config.database import get_session
from config.security import get_current_user
from model.models import UserModel
from schemas.schemas import Request, Response
from utils.prediction import PredictionService

router = APIRouter(prefix="/api/predict", tags=["Predict"])

prediction = PredictionService()


@router.post(path="/", status_code=200, response_model=Response)
async def predict_endpoint(
    request: Request,
    user_id: int,
    current_user: UserModel = Depends(get_current_user),
    session: Session = Depends(get_session),
) -> Response:
    try:
        values = np.array(
            [
                request.SepalLengthCm,
                request.SepalWidthCm,
                request.PetalLengthCm,
                request.PetalWidthCm,
            ]
        )
        category = prediction.predict(values, user_id, session)

        return Response(category=category)
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))
