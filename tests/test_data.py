from pytest import fail
from causal.best_matches.data import Data, filter_dates
import pytest 
import pandas as pd
import numpy as np
from causal.best_matches.parameters import Parameters
from causal.best_matches.data import Data

# Weather data fixture
@pytest.fixture
def example_weather_data_columns():
    return pd.DataFrame(columns=["Area", "Date", "Mean_TemperatureF"])

@pytest.fixture
def example_weather_data():
    return pd.read_csv('data/weather.csv')

def test_for_missing_columns(example_weather_data_columns):
    with pytest.raises(ValueError) as err:
        data = Data(example_weather_data_columns, Parameters(id_variable="", date_variable="Date", matching_variable="Mean_TemperatureF", start_match_period="2014-01-01", end_match_period="2014-10-01"))
    assert str(err.value) == "There are columns missing in the dataframe"

def test_cols_are_renamed(example_weather_data):
    data = Data(example_weather_data, Parameters(id_variable="Area", date_variable="Date", matching_variable="Mean_TemperatureF", start_match_period="2014-01-01", end_match_period="2014-10-01"))
    assert data.df.columns.tolist() == ['id_var', 'date_var', 'match_var']

def test_duplicates_in_data(example_weather_data):
    # Mock a duplicate Row 
    weather_subset= example_weather_data[example_weather_data["Mean_TemperatureF"]== 49]
    duplicate_weather_df = pd.concat([example_weather_data, weather_subset], ignore_index=True)
    
    with pytest.raises(ValueError) as err:
        data= Data(duplicate_weather_df, Parameters(id_variable="Area", date_variable="Date", matching_variable="Mean_TemperatureF", start_match_period="2014-01-01", end_match_period="2014-08-01"))
    assert str(err.value) == "There are date/market duplicates in the data"


def test_all_entities_present(example_weather_data):
    data= Data(example_weather_data, Parameters(id_variable="Area", date_variable="Date", matching_variable="Mean_TemperatureF", start_match_period="2014-01-01", end_match_period="2014-08-01"))
    assert data.history == []

def assert_no_entity_history(example_weather_data):
    with pytest.raises(ValueError) as err:
        data= Data(example_weather_data[example_weather_data["Area"] =="SFO"], Parameters(id_variable="Area", date_variable="Date", matching_variable="Mean_TemperatureF", start_match_period="2014-01-01", end_match_period="2014-08-01"))
    assert str(err) == "Only one entity found with history for the provided dates"
    
def assert_no_entity_history(example_weather_data):
    with pytest.raises(ValueError) as err:
        data= Data(example_weather_data[example_weather_data["Area"]=="Nuthin"][example_weather_data["Area"] =="SFO"], Parameters(id_variable="Area", date_variable="Date", matching_variable="Mean_TemperatureF", start_match_period="2014-01-01", end_match_period="2014-08-01"))
    assert str(err) == "0 entitie(s) found with history for the provided dates"