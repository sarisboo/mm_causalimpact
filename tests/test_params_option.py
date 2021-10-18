from pytest import fail
from causal.best_matches.options import Options


def test_dtw_emphasis_negative():
    optns = Options(dtw_emphasis=-1)
    assert optns.dtw_emphasis == 0

def test_dtw_emphasis_big_num():
    optns = Options(dtw_emphasis=3000)
    assert optns.dtw_emphasis == 1