import pickle
import numpy as np


class PreProcessor:
    def __init__(self):
        with open("model/scaler.pkl", "rb") as file:
            self.scaler = pickle.load(file)

    def preprocess(self, data: np.array) -> np.array:
        data = self.scaler.transform(data)
        return data
