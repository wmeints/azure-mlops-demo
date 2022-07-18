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

    parser.add_argument('--model-file',
                        type=str,
                        required=True,
                        help='The output file to write the model to')

    args = parser.parse_args()

    mlflow.start_run()

    df_input = pd.read_csv(args.training_data)
    df_features = df_input.drop(['WACHTTIJD'])
    df_output = df_input['WACHTTIJD']

    df_features_train, df_features_test, df_output_train, df_output_test = \
        train_test_split(df_features, df_output, test_size=0.2)

    model = ExplainableBoostingRegressor(feature_names=df_features.columns)
    model.fit(df_features_train.to_numpy(), df_output_train.to_numpy())

    score = model.score(df_features_test.to_numpy(), df_output_test.to_numpy())

    mlflow.log_metric('R2', score)

    mlflow.sklearn.save_model(model, args.model_file)

    mlflow.end_run()


if __name__ == "__main__":
    main()
