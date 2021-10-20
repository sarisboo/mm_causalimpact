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
    ddup_df = df.drop_duplicates(inplace=False)
    if ddup_df.shape[0] < df.shape[0]:
        raise ValueError("There are date/market duplicates in the data")



def reduce_df_width(df, id_variable, date_variable):
    # First order by id_var and date_var
    sortedby_id_date = df.sort_values([id_variable, date_variable])
    return sortedby_id_date
    


def filter_dates(df, id_variable, date_variable, start_match_period, end_match_period):
    # Find if data for each test store is present for start_match_period and end_match_period interval
    # If not, assign it to a no_history list
    # return the no_history list
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
            
            #reduce_df_width(self.df, params.id_variable, params.date_variable)
            
            #filter_dates(self.df)
            
            # TODO: assert there is data left
        
        else : 
            raise ValueError("There are columns missing in the dataframe") 

