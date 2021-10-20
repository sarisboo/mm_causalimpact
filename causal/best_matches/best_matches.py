from .data import Data
from .options import Options
from .parameters import Parameters
from .market_matching.market_matching import match_markets
import pandas as pd

def best_matches(
    df, 
    id_variable, 
    date_variable, 
    matching_variable,
    start_match_period, 
    end_match_period,
    options = Options()
):
    # Check df input values before passing to constructor
    assert df is not None
    # Initializing param instance -- Do I need to initialize options instance ?
    params = Parameters(
        id_variable,
        date_variable,
        matching_variable,
        start_match_period,
        end_match_period,
    )
    # Normalize the matches parameter    
    options.normalize_matches(df, params)
    
    # Construct the data
    data = Data(df, params)
    
    # Match the markets and output the results
    #results = match_markets(data, params, options)
    #return results
