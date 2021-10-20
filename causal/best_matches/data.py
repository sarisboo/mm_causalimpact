import pandas as pd
import numpy as np

def check_data_inputs(df, id_var, matching_var, date_var):
    if not all([item in df.columns for item in [id_var, matching_var, date_var]]):
        raise ValueError("There are columns missing in the dataframe")
    
def rename_cols_to_match_r(df, date_variable, id_variable, matching_variable):
    df_copy = df.copy()
    col_map = {id_variable: 'id_var', date_variable: 'date_var', matching_variable: 'match_var'}
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
    


def filter_dates(df, date_variable, id_variable, start_match_period, end_match_period):

    # Find if data for each test store is present for start_match_period and end_match_period interval
    df_subset = df[(df[date_variable] >= start_match_period) &  (df[date_variable] <= end_match_period)]
    
    entities_with_no_history = list(np.setdiff1d(df[id_variable].unique(), df_subset[id_variable].unique()))

    # If all entities have history
    if len(entities_with_no_history) == 0:
        print("All entities have history")
        return entities_with_no_history

    elif len(df_subset[id_variable].unique()) == 1:
        raise ValueError("Only one entity found with history for the provided dates")

    elif len(df_subset[id_variable].unique()) >=2 and len(df_subset[id_variable].unique()) < len(df[id_variable].unique()):
        print("Some test entities do not have history for the dates provided")
        return entities_with_no_history
    else:
        raise ValueError("0 entitie(s) found with history for the provided dates")
    


class Data(object):
    def __init__(self, df, params):

        self.df = df
        
        # Check Inputs
        check_data_inputs(df, params.id_variable, params.matching_variable, params.date_variable)
        
        #copy df and rename
        self.df = rename_cols_to_match_r(self.df, params.date_variable, params.id_variable, params.matching_variable)
            
        #check for duplicates and raise error if so
        assert_duplicates(self.df, params.id_variable, params.date_variable)
            
        #starting here, column names have changed to "id_var", "date_var" and "matching_var"
        self.df = reduce_df_width(self.df, "id_var", "date_var")
            
        # filtering for dates
        self.history = filter_dates(self.df,"date_var", "id_var", params.start_match_period, params.end_match_period)
        
        

