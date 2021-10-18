from causal.best_matches.best_matches import best_matches
import pandas as pd
import pytest

# Weather data fixture
@pytest.fixture
def example_weather_data():
    return pd.read_csv('data/weather.csv')

