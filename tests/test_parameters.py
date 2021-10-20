from pytest import fail
from causal.best_matches.parameters import Parameters

def test_match_periods_are_valid():
    try:
        Parameters("", "", "", "2021-01-17", "2021-08-14")
    except ValueError:
        fail()

def test_start_date_superior_end_date():
    params_1 = Parameters("", "", "","2021-01-17","2021-08-14")
    if params_1.start_match_period >= params_1.end_match_period:
        raise ValueError("The Start matching date is superior or equal to the end matching date")

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