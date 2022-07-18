import argparse
import pandas as pd
import mlflow


def drop_missing_wachttijden(df):
    """
    Drop rows with missing wachttijden
    """
    return df.dropna(subset=['WACHTTIJD'])


def fill_missing_zorg_instelling(df):
    """
    Fill missing zorg_instelling with the type Kliniek.
    """
    df['TYPE_ZORGINSTELLING'] = df['TYPE_ZORGINSTELLING'].fillna('Kliniek')
    return df


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

    args = parser.parse_args()

    mlflow.start_run()

    mlflow.log_param('features', args.features)

    df = pd.read_csv(args.input_file)

    df = drop_missing_wachttijden(df)
    df = fill_missing_zorg_instelling(df)

    mlflow.log_metric('num_samples', len(df))

    df.to_csv(args.output_file, index=False)

    mlflow.end_run()


if __name__ == "__main__":
    main()
