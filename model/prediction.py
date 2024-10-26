import pickle
import numpy as np


class Prediction:
    def __init__(self) -> None:
        with open("model/model.pkl", "rb") as file:
            self.model = pickle.load(file)

    def predict(self, values: np.array) -> str:
        values = values.reshape(1, -1)
        pred: str = self.model.predict(values)[0]
        return pred
