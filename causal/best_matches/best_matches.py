from .data import Data
from .options import Options
from .parameters import Parameters
from .market_matching.market_matching import match_markets
import pandas as pd

def normalize_matches(df, id_variable, markets, suggest_market_splits):
    #TODO Review the conditioon depedning on `suggest_market_split` implementation
    if markets is not None and suggest_market_splits is True:
        matches = len(df[id_variable].unique())
        return matches
    else:
        matches =5
        return matches

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
    options.matches = normalize_matches(df, id_variable=params.id_variable, markets=options.markets, suggest_market_splits=options.suggest_market_splits)
    
    # Construct the data
    data = Data(df, params)
    
    # Match the markets and output the results
    results = match_markets(data, params, options)
    return results

df_params = Data(pd.read_csv("data/weather.csv"), Parameters(id_variable="Area", date_variable="Date", matching_variable="Mean_TemperatureF", start_match_period="2014-01-01", end_match_period="2014-10-01"))
df = df_params.df
print(df.columns)