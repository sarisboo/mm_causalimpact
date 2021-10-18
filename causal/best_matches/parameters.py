def assert_dates(start_date, end_date):
    if start_date >= end_date:
        raise ValueError("The Start matching date is superior or equal to the end matching date")

def assert_none(start_date, end_date):
    if start_date is "None":
        raise ValueError("No value provided for the start date")
    elif end_date is "None":
        raise ValueError("No value provided for the end date ")


class Parameters(object):
    def __init__(
        self,
        id_variable, 
        date_variable, 
        matching_variable,
        start_match_period, 
        end_match_period,
    ):
        self.id_variable = id_variable
        self.date_variable = date_variable
        self.matching_variable = matching_variable
        self.start_match_period = str(start_match_period)
        self.end_match_period = str(end_match_period)

        # Checking the dates
        assert_dates(start_match_period, end_match_period)
        assert_none(start_match_period, end_match_period)

