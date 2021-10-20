from pytest import fail
from causal.best_matches.options import Options
from causal.best_matches.best_matches import best_matches
from causal.best_matches.parameters import Parameters
import pytest
import pandas as pd

# Weather data fixture
@pytest.fixture
def example_weather_data():
    return pd.read_csv('data/weather.csv')

def test_ensure_dtw_emphasis_value_0():
    optns = Options(dtw_emphasis=-1)
    assert optns.dtw_emphasis == 0

def test_ensure_dtw_emphasis_value_1():
    optns = Options(dtw_emphasis=3000)
    assert optns.dtw_emphasis == 1

def test_output_market_split_message():
    optns = Options(suggest_market_splits=True, markets=None)
    assert "The suggest_market_splits parameter has been turned off since markets_to_be_matched is not None\nSet markets_to_be_matched to None if you want optimized pairs \n"


def test_normalizing_matches_none_markets_none_suggest_split_false(example_weather_data):
    params = Parameters("Area", "Date", "Mean_TemperatureF","2021-01-17", "2021-08-14")
    options=Options(matches=None, markets=None, suggest_market_splits=False)
    assert options.normalize_matches(example_weather_data, params) == 5

def test_normalizing_matches_none_markets_none_suggest_split_true(example_weather_data):
    params = Parameters("Area", "Date", "Mean_TemperatureF","2021-01-17", "2021-08-14")
    options=Options(matches=None, markets=None, suggest_market_splits=True)
    assert options.normalize_matches(example_weather_data, params) == len(example_weather_data[params.id_variable].unique())

def test_normalizing_matches_not_none_markets_none_suggest_split_true(example_weather_data):
    params = Parameters("Area", "Date", "Mean_TemperatureF","2021-01-17", "2021-08-14")
    options=Options(matches=18, markets=None, suggest_market_splits=True)
    assert options.normalize_matches(example_weather_data, params) == len(example_weather_data[params.id_variable].unique())

def test_normalizing_matches_not_none_markets_not_none_suggest_split_true(example_weather_data):
    params = Parameters("Area", "Date", "Mean_TemperatureF","2021-01-17", "2021-08-14")
    options=Options(matches=8, markets=['SFO', 'ATL'], suggest_market_splits=True)
    assert options.normalize_matches(example_weather_data, params) == 8

def test_normalizing_matches_not_none_markets_not_none_suggest_split_false(example_weather_data):
    params = Parameters("Area", "Date", "Mean_TemperatureF","2021-01-17", "2021-08-14")
    options=Options(matches=8, markets=['SFO', 'ATL'], suggest_market_splits=False)
    assert options.normalize_matches(example_weather_data, params) == 8