from pytest import fail
from causal.best_matches.options import Options


def test_ensure_dtw_emphasis_value_0():
    optns = Options(dtw_emphasis=-1)
    assert optns.dtw_emphasis == 0

def test_ensure_dtw_emphasis_value_1():
    optns = Options(dtw_emphasis=3000)
    assert optns.dtw_emphasis == 1

def test_output_market_split_message():
    optns = Options(suggest_market_splits=True, markets=None)
    assert "The suggest_market_splits parameter has been turned off since markets_to_be_matched is not NULL\nSet markets_to_be_matched to NULL if you want optimized pairs \n"

    