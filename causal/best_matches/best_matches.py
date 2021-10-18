from .data import Data
from .options import Options
from .parameters import Parameters
from .market_matching.market_matching import match_markets


def best_matches(
    df, 
    id_variable, 
    date_variable, 
    matching_variable,
    start_match_period, 
    end_match_period,
    options = Options()
):
    params = Parameters(
        id_variable,
        date_variable,
        matching_variable,
        start_match_period,
        end_match_period,
    )
    data = Data(df, params)
    results = match_markets(data, params, options)
    return results