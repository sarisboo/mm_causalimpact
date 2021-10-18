def check_data_inputs(df, id_var, matching_var, date_var):
    if all([item in df.columns for item in [id_var,matching_var, date_var]]):
        return True
    else:
        return False
    

def assert_duplicates(df, id_variable, date_variable):
    pass


def reduce_df_width(df, id_variable, date_variable):
    pass


def filter_dates(df, id_variable, date_variable, start_match_period, end_match_period):
    pass


class Data(object):
    def __init__(self, df, params):
        self.df = df
        # Check Inputs
        self.check_df = check_data_inputs(df, params.id_variable, params.matching_variable, params.date_variable)
        #if self.check_df:
            #assert_duplicates(df, params.id_variable, params.date_variable)
            #normalized_df = reduce_df_width(df, params.id_variable, params.date_variable)
            #filtered_df = filter_dates(df)
            # TODO: assert there is data left
            