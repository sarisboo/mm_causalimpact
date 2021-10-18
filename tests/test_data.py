from pytest import fail
from causal.best_matches.data import Data
import pytest 
import pandas as pd

from causal.best_matches.parameters import Parameters

# Weather data fixture
@pytest.fixture
def example_weather_data():
    return pd.read_csv('data/weather.csv')

def test_columns_exist(example_weather_data):
    df_params = Data(example_weather_data, Parameters(id_variable="Area", date_variable="Date", matching_variable="Mean_TemperatureF", start_match_period="2014-01-01", end_match_period="2014-10-01"))
    assert df_params.check_df == True

def test_1_column_absent(example_weather_data):
    df_params = Data(example_weather_data, Parameters(id_variable="", date_variable="Date", matching_variable="Mean_TemperatureF", start_match_period="2014-01-01", end_match_period="2014-10-01"))
    assert df_params.check_df == False