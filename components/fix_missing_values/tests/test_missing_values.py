import pytest
import pandas as pd
from components.fix_missing_values.component import drop_missing_wachttijden, fill_missing_zorg_instelling


@pytest.fixture()
def df_missing_wachttijden():
    data = [
        {'WACHTTIJD': None, 'TYPE_ZORGINSTELLING': 'Kliniek'},
        {'WACHTTIJD': '80', 'TYPE_ZORGINSTELLING': 'Kliniek'},
        {'WACHTTIJD': '1', 'TYPE_ZORGINSTELLING': 'Kliniek'},
    ]

    return pd.DataFrame(data)


@pytest.fixture()
def df_missing_zorginstelling():
    data = [
        {'WACHTTIJD': '20', 'TYPE_ZORGINSTELLING': None},
        {'WACHTTIJD': '80', 'TYPE_ZORGINSTELLING': 'Kliniek'},
        {'WACHTTIJD': '1', 'TYPE_ZORGINSTELLING': 'Kliniek'},
    ]

    return pd.DataFrame(data)


def test_drop_missing_wachttijden(df_missing_wachttijden):
    df_result = drop_missing_wachttijden(df_missing_wachttijden)

    assert len(df_result) == 2


def test_fill_missing_zorg_instelling(df_missing_zorginstelling):
    df_result = fill_missing_zorg_instelling(df_missing_zorginstelling)

    assert len(df_result) == 3
    assert len(df_result[df_result['TYPE_ZORGINSTELLING'] == 'Kliniek']) == 3
