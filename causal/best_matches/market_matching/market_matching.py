from .market_splits import MarketSplits
from .result import Result


def create_markets_set(df, markets):
    markets


# loop through markets and compute distances
def calculate_shortest_distances(df, markets_set, params):
    []


def match_markets(data, params):
    markets_set = create_markets_set(data.df, params.markets)
    shortest_distances = calculate_shortest_distances(data.df, markets_set, params)
    market_splits = MarketSplits() if params.suggest_market_splits else None
    return Result(data, params, shortest_distances, market_splits)