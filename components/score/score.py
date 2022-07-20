import os
from pyexpat import model
import pickle
import json
import pandas as pd
import logging


model_directory = os.getenv("AZUREML_MODEL_DIR")
model_file = os.path.join(model_directory, "wachttijden-ebm/model.pkl")

def init():
    global model

    logging.info("Model directory: %s", model_directory)
    logging.info("Model file exists: %s", os.path.isfile(model_file))

    with open(model_file, "rb") as f:
        model = pickle.load(f)

    logging.info("Loaded model from %s", model_directory)

def run(raw_data):
    data = json.loads(raw_data)["data"]
    df = pd.DataFrame([data])

    logging.info("Features: %s", df.columns)

    prediction = model.predict(df.to_numpy())

    return json.dumps({"prediction": prediction.tolist()})