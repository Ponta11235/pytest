import pandas as pd
from pandas._testing import assert_frame_equal


def test_f(datadir):
    df1 = pd.read_excel(datadir / 'input.xlsx')
    df2 = pd.read_excel(datadir / 'expected.xlsx')
    assert_frame_equal(df1, df2)
