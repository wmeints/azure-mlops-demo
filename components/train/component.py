import os
import mlflow
from mlflow.models.signature import infer_signature
import pandas as pd
import argparse
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import FeatureUnion, Pipeline


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--training-data',
                        type=str,
                        required=True,
                        help='The input file containing the training data')

    args = parser.parse_args()

    mlflow.start_run()

    df_input = pd.read_csv(args.training_data)

    df_train, df_test = train_test_split(df_input, test_size=0.2)
    df_train_output = df_train[['WACHTTIJD']]
    df_train_inputs = df_train.drop(['WACHTTIJD'], axis=1)

    df_test_output = df_test[['WACHTTIJD']]
    df_test_inputs = df_test.drop(['WACHTTIJD'], axis=1)

    feature_names = [
        'TYPE_WACHTTIJD',
        'SPECIALISME',
        'ROAZ_REGIO',
        'TYPE_ZORGINSTELLING'
    ]

    num_estimators = 100

    mlflow.log_param('features', feature_names)
    mlflow.log_param('num_estimators', num_estimators)

    encoders = [(feature_name, OneHotEncoder()) for feature_name in feature_names]

    model = Pipeline([
        ("combine_features",FeatureUnion(encoders)),
        ("estimator",RandomForestRegressor(n_estimators=num_estimators))
    ])

    model.fit(df_train_inputs.to_numpy(), df_train_output.values.reshape(-1,1))
    model_signature = infer_signature(df_train_inputs, model.predict(df_test_inputs.to_numpy()))

    score = model.score(df_test_inputs.to_numpy(), df_test_output.values.reshape(-1,1))
    mlflow.log_metric('R2', score)

    mlflow.sklearn.log_model(model, artifact_path="wachttijden-random-forest", signature=model_signature)

    mlflow.register_model(f"runs:/{mlflow.active_run().info.run_id}/wachttijden-random-forest", "wachttijden")

    mlflow.end_run()


if __name__ == "__main__":
    main()
