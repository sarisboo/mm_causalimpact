from causal.best_matches.best_matches import best_matches
import pandas as pd
import pytest
from causal.best_matches.best_matches import best_matches
from causal.best_matches.options import Options

# Weather data fixture
@pytest.fixture
def example_weather_data():
    return pd.read_csv('data/weather.csv')


    