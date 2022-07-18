import os
import pytest
import pandas as pd
from components.select_features.component import select_features


@pytest.fixture()
def input_file(tmp_path):
    filename = tmp_path / 'input.csv'

    data = [
        {
            'WACHTTIJD': '20',
            'TYPE_ZORGINSTELLING': 'Kliniek'
        },
        {
            'WACHTTIJD': '20',
            'TYPE_ZORGINSTELLING': 'Kliniek'
        },
        {
            'WACHTTIJD': '20',
            'TYPE_ZORGINSTELLING': 'Kliniek'
        },
    ]

    df = pd.DataFrame(data)

    df.to_csv(filename, index=False)

    yield filename

    os.remove(filename)


@pytest.fixture()
def output_file(tmp_path):
    filename = tmp_path / 'output.csv'

    yield filename

    os.remove(filename)


def test_select_features(input_file, output_file):
    features = ['WACHTTIJD']

    select_features(input_file, output_file, features)

    df = pd.read_csv(output_file)

    assert len(df) == 3
    assert len(df.columns) == 1
