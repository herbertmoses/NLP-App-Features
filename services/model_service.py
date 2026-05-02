import pickle
import numpy as np


class ModelService:
    def __init__(self, model_path):
        with open(model_path, "rb") as f:
            self.model = pickle.load(f)

    def predict(self, features):
        arr = np.array([features])
        return self.model.predict(arr)