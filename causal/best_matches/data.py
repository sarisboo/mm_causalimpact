import pandas as pd


def check_data_inputs(df, id_var, matching_var, date_var):
    if all([item in df.columns for item in [id_var,matching_var, date_var]]):
        return True
    else:
        return False
    
def rename_cols_to_match_r(df, date_variable, id_variable, matching_variable):
    df_copy = df.copy()
    col_map = {date_variable: 'date_var', id_variable: 'id_var', matching_variable: 'match_var'}
    df_copy = df_copy.rename(columns=col_map)
    return df_copy
    
def assert_duplicates(df, id_variable, date_variable):
    ddup_df = df.drop_duplicates()
    try:
        ddup_df.shape[0] < df.shape[0]
    except:
        raise ValueError("There are date/market duplicates in the data")


def reduce_df_width(df, id_variable, date_variable):
    pass


def filter_dates(df, id_variable, date_variable, start_match_period, end_match_period):
    pass


class Data(object):
    def __init__(self, df, params):

        self.df = df
        
        # Check Inputs
        self.check_df = check_data_inputs(df, params.id_variable, params.matching_variable, params.date_variable)
        
        if self.check_df:
            #copy df and rename
            self.df = rename_cols_to_match_r(self.df, params.date_variable, params.id_variable, params.matching_variable)
            
            #check for duplicates and raise error if so
            assert_duplicates(df, params.id_variable, params.date_variable)
            
            #normalized_df = reduce_df_width(df, params.id_variable, params.date_variable)
            
            #filtered_df = filter_dates(df)
            
            # TODO: assert there is data left
        
        # else : raise ValueError 

