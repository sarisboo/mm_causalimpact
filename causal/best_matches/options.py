def clean_emphasis(dtw_emphasis):
    if dtw_emphasis == None:
        dtw_emphasis =1
    elif dtw_emphasis > 1:
        dtw_emphasis = 1
    else:
        dtw_emphasis =0

    return dtw_emphasis




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
            self.matches = matches
            self.dtw_emphasis = clean_emphasis(dtw_emphasis)
            self.suggest_market_splits = suggest_market_splits
            self.splibins = splitbins
            self.log_for_splitting = log_for_splitting

            # Check suggest_market_split
            if markets is not None and suggest_market_splits is True:
                print("The suggest_market_splits parameter has been turned off since markets_to_be_matched is not None\nSet markets_to_be_matched to None if you want optimized pairs\n")   