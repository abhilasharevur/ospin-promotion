import os
import pytest
import pandas as pd
import datatest as dt
from pathlib import Path

THIS_DIR = Path(__file__).parent
my_data_path = os.path.join(THIS_DIR, os.pardir)


def pytest_addoption(parser):
    parser.addoption(
        "--input-path",
        help="Absolute path to input directory where .csv files reside",
        required=True
    )
    parser.addoption(
        "--promotion-type",
        default=None,
        help="The type of promotion scheme",
        required=True
    )
    parser.addoption(
        "--output-path",
        help="Absolute path to output directory to store results",
        default="tests/output/test_output.csv"
    )


@pytest.fixture
def input_path(request):
    return request.config.getoption("--input-path")


@pytest.fixture
def promotion_type(request):
    return request.config.getoption("--promotion-type")


@pytest.fixture
def output_path(request):
    return request.config.getoption("--output-path")


@pytest.fixture(scope='module')
@dt.working_directory(__file__)
def df():
    return pd.read_csv('test_orders.csv')
