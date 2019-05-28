class Shard:
    def __init__(self, low, high):
        assert low < high
        self.low = low
        self.high = high

