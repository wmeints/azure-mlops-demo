import os
from pyexpat import model
import pickle
import json
import pandas as pd
import logging

model_directory = os.getenv("AZUREML_MODEL_DIR", default="./models")
model_file = os.path.join(model_directory,
                          "wachttijden-random-forest/model.pkl")


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

    # Note: You'll have to leave the features in this order for the model to work correctly.
    # If you change the order, the model will mix up the one-hot encoding resulting in the wrong prediction.
    input_features = [
        'TYPE_WACHTTIJD', 'SPECIALISME', 'ROAZ_REGIO', 'TYPE_ZORGINSTELLING'
    ]

    prediction = model.predict(df[input_features].to_numpy())

    return json.dumps({"prediction": prediction.tolist()})


if __name__ == "__main__":
    sample_data = json.dumps({
        "data": {
            "TYPE_WACHTTIJD": "Behandeling",
            "SPECIALISME": "KNO (302)",
            "ROAZ_REGIO": "Noord-NL",
            "TYPE_ZORGINSTELLING": "Ziekenhuis"
        }
    })

    init()
    print(run(sample_data))