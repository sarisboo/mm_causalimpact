def assert_valid_dates(start_date, end_date):
    assert start_date is not None
    assert end_date is not None

    if start_date >= end_date:
        raise ValueError("The Start matching date is superior or equal to the end matching date")

class Parameters(object):
    def __init__(
        self,
        id_variable, 
        date_variable, 
        matching_variable,
        start_match_period, 
        end_match_period,
    ):
        assert id_variable is not None
        assert date_variable is not None
        assert matching_variable is not None
        assert_valid_dates(start_match_period, end_match_period)
        # Check length of id_variable -- Need at least 2
        # Check for nulls/nas in id_variable
        # Check for nas in matching  variable 

        self.id_variable = id_variable
        self.date_variable = date_variable
        self.matching_variable = matching_variable
        self.start_match_period = start_match_period
        self.end_match_period = end_match_period
