import argparse
import pandas as pd
import mlflow


def select_features(input_file, output_file, features):
    """
    Selects features from the input file and writes them to the output file.
    """
    df = pd.read_csv(input_file)
    df = df[features]

    df.to_csv(output_file, index=False)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-file",
                        type=str,
                        required=True,
                        help="Path to input file")

    parser.add_argument("--output-file",
                        type=str,
                        required=True,
                        help="Path to output file")

    parser.add_argument("--features",
                        nargs="+",
                        type=str,
                        required=True,
                        help="List of features to select")

    args = parser.parse_args()

    mlflow.start_run()

    mlflow.log_param('features', args.features)

    select_features(args.input_file, args.output_file, args.features)

    mlflow.end_run()


if __name__ == "__main__":
    main()
