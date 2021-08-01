import sys
from pathlib import Path

THIS_DIR = Path(__file__).parent
par_dir = THIS_DIR.parent

sys.path.append(str(par_dir))

from conftest import *
from src.app import main as app_main


pytestmark = pytest.mark.filterwarnings('ignore:subset and superset warning')


def test_input(input_path):
    assert os.path.isdir(input_path)


def test_promo_type(promotion_type):
    assert promotion_type


def test_output(output_path):
    assert os.path.isfile(output_path)


@pytest.mark.mandatory
def test_columns(df):
    dt.validate(
        df.columns,
        {'organ', 'cash', 'price', 'bonus_ratio'},
    )


def test_organ(df):
    dt.validate.superset(df['organ'], ['liver', 'lung', 'heart'])


def test_cash(df):
    dt.validate(df['cash'], int)


def test_price(df):
    dt.validate(df['price'], int)


def test_bonus_ratio(df):
    dt.validate(df['bonus_ratio'], int)


def test_main(capfd):
    app_main("tests", "rebate_scheme", "tests/output/test_output.csv")
    out, err = capfd.readouterr()
    assert out == 'heart 0,liver 2,lung 1\nheart 4,liver 0,lung 0\nheart 2,liver 2,lung 8\n'
