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
        matches=5, 
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

    def normalize_matches(self, df, params):
        if self.matches is None:
        #TODO Review the condition depending on `suggest_market_split` implementation
            if self.markets is None and self.suggest_market_splits is True:
                self.matches = len(df[params.id_variable].unique())
                return self.matches
            else:
                self.matches = 5
                return self.matches
        else:
            if self.markets is None and self.suggest_market_splits == True:
                self.matches = len(df[params.id_variable].unique())
                print("The matches parameter has been overwritten for splitting to conduct a full search for optimized pairs\n")
                return self.matches
            else:
                return self.matches
