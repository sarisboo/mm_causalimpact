def clean_emphasis(dtw_emphasis):
    if dtw_emphasis == None:
        dtw_emphasis =1
    elif dtw_emphasis > 1:
        dtw_emphasis = 1
    else:
        dtw_emphasis =0

    return dtw_emphasis

def check_markets(markets, suggest_market_splits):
    pass

def normalize_matches(markets, matches, suggest_market_splits):
    0


class Options(object):
    def __init__(
        self,
        # markets is markets_to_be_matched in R
        markets=None,
        warping_limit=1, 
        matches=None, 
        dtw_emphasis=1, 
        suggest_market_splits=False, 
        splitbins=10, 
        log_for_splitting=False):
            self.markets = markets
            self.warping_limit = warping_limit
            self.matches = normalize_matches(
                markets,
                matches,
                suggest_market_splits
            )
            self.dtw_emphasis = clean_emphasis(dtw_emphasis)
            self.suggest_market_splits = suggest_market_splits
            self.splibins = splitbins
            self.log_for_splitting = log_for_splitting
                     