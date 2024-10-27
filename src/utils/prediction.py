import pickle

import numpy as np

from utils.pre_processor import PreProcessor


class Prediction:
    def __init__(self) -> None:
        self.preprocessor = PreProcessor()
        with open("model/Iris.pkl", "rb") as file:
            self.model = pickle.load(file)

        self.mapped_category = {
            0: "Iris-setosa",
            1: "Iris-versicolor",
            2: "Iris-virginica",
        }

    def predict(self, data: np.array) -> str:
        data = data.reshape(1, -1)
        data = self.preprocessor.preprocess(data)
        value = self.model.predict(data)[0]
        pred = self.mapped_category[value]
        return pred
