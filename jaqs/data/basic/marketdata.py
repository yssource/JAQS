# encoding: utf-8


class Bar(object):
    def __init__(self):
        self.open = 0.
        self.close = 0.
        self.high = 0.
        self.low = 0.
        self.volume = 0
        self.oi = 0
        self.vwap = 0.
        
        self.trade_date = 0
        self.time = 0
        self._bar_keys = ['open', 'close', 'high', 'low', 'vwap',
                          'volume', 'oi',
                          'trade_date', 'time']
    
    @classmethod
    def create_from_df(cls, df):
        bar_list = []
        for _, row in df.iterrows():
            bar = cls()
            dic = row.to_dict()
            bar.__dict__.update(dic)
            bar_list.append(bar)
        return bar_list

    @classmethod
    def create_from_dict(cls, dic):
        bar = cls()
        bar.__dict__.update(dic)
        return bar

    def __repr__(self):
        return "{0.trade_date:8d}-{0.time:6d} " \
               "{0.volume:13.2f} of " \
               "{0.symbol:10s}@{0.close:.3f}".format(self)

    def __str__(self):
        return self.__repr__()
