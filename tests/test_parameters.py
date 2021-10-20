from pytest import fail
import pytest
from causal.best_matches.parameters import Parameters

def test_match_periods_are_valid():
    try:
        Parameters("", "", "", "2021-01-17", "2021-08-14")
    except ValueError:
        fail()

def test_start_date_superior_end_date():
    with pytest.raises(ValueError) as err:
        params = Parameters("", "", "", "2021-08-14", "2021-01-17")
    assert str(err.value) == "The Start matching date is superior or equal to the end matching date"

def test_no_start_date_value():
    try:
        Parameters("","", "", str(None), "2021-08-14")
    except ValueError: 
        print("No value provided for the start date")

def test_no_end_date_value():
    try:
        Parameters("","", "", "2021-01-17", str(None))
    except ValueError: 
        print("No value provided for the end date")