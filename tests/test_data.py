from pytest import fail
from causal.best_matches.data import Data
import pytest 
import pandas as pd

from causal.best_matches.parameters import Parameters
from causal.best_matches.data import Data

# Weather data fixture
@pytest.fixture
def example_weather_data_columns():
    return pd.DataFrame(columns=["Area", "Date", "Mean_TemperatureF"])

@pytest.fixture
def example_weather_data():
    return pd.read_csv('data/weather.csv')

def test_all_column_names_present(example_weather_data_columns):
    df_params = Data(example_weather_data_columns, Parameters(id_variable="Area", date_variable="Date", matching_variable="Mean_TemperatureF", start_match_period="2014-01-01", end_match_period="2014-10-01"))
    assert df_params.check_df == True

def test_for_missing_columns(example_weather_data_columns):
    df_params = Data(example_weather_data_columns, Parameters(id_variable="", date_variable="Date", matching_variable="Mean_TemperatureF", start_match_period="2014-01-01", end_match_period="2014-10-01"))
    assert df_params.check_df == False

def test_cols_are_renamed(example_weather_data_columns):
    df_params = Data(example_weather_data_columns, Parameters(id_variable="Area", date_variable="Date", matching_variable="Mean_TemperatureF", start_match_period="2014-01-01", end_match_period="2014-10-01"))
    df = df_params.df
    new_cols = df.columns
    return new_cols == ['date_var', 'id_var',  'match_var']

def test_duplicates_in_data(example_weather_data):
    # Mock a duplicate Row 
    weather_subset= example_weather_data[example_weather_data["Mean_TemperatureF"]<=50]
    duplicate_weather_df = pd.concat([example_weather_data, weather_subset], ignore_index=True)
    data= Data(duplicate_weather_df, Parameters(id_variable="Area", date_variable="Date", matching_variable="Mean_TemperatureF", start_match_period="2014-01-01", end_match_period="2014-10-01"))
    assert "There are date/market duplicates in the data"


