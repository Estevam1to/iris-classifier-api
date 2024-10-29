import pickle
import numpy as np
import pandas as pd

from config.settings import Settings
from sqlalchemy.orm import Session
from model.predictions import PredictionModel


class PredictionService:
    def __init__(self) -> None:
        with open(Settings().PATH_MODEL, "rb") as file:
            self.model = pickle.load(file)

        self.mapped_category = {
            0: "Iris-setosa",
            1: "Iris-versicolor",
            2: "Iris-virginica",
        }

        self.feature_names = [
            "SepalLengthCm",
            "SepalWidthCm",
            "PetalLengthCm",
            "PetalWidthCm",
        ]

    def __create_prediction(self, data: np.array) -> str:
        data_df = pd.DataFrame(data.reshape(1, -1), columns=self.feature_names)
        value = self.model.predict(data_df)[0]
        pred = self.mapped_category[value]
        return pred

    def __save_prediction(self, user_id: int, session: Session, predict: str) -> str:
        try:
            prediction = PredictionModel(user_id=user_id, predict=predict)
            session.add(prediction)
            session.commit()
            return predict
        except Exception as e:
            session.rollback()
            raise Exception(f"Erro ao salvar a previsão: {e}")

    def predict(self, data: np.array, user_id: int, session: Session) -> str:
        pred = self.__create_prediction(data)
        pred_db = self.__save_prediction(user_id, session, pred)
        return pred_db
