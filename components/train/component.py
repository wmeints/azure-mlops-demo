import os
import mlflow
import pandas as pd
import argparse
from sklearn.model_selection import train_test_split
from interpret.glassbox import ExplainableBoostingRegressor


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
    df_train_inputs = df_train.drop(['WACHTTIJD','NAAM_INSTELLING'], axis=1)

    df_test_output = df_test[['WACHTTIJD']]
    df_test_inputs = df_test.drop(['WACHTTIJD','NAAM_INSTELLING'], axis=1)

    model = ExplainableBoostingRegressor(feature_names=df_train_inputs.columns)
    
    model.fit(df_train_inputs.to_numpy(), df_train_output.to_numpy())
    score = model.score(df_test_inputs.to_numpy(), df_test_output.to_numpy())

    mlflow.log_metric('R2', score)

    mlflow.sklearn.log_model(model, artifact_path='wachttijden-ebm')

    mlflow.register_model(f'runs:/{mlflow.active_run().info.run_id}/wachttijden-ebm', "wachttijden")

    mlflow.end_run()


if __name__ == "__main__":
    main()
