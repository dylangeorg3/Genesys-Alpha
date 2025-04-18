
class BaseStategy():
    def __init__(self, name = 'BaseStrategy'):
        self.name = name

    def generate_signals(self, data):
        """
        Generate signals based on the strategy logic.
        This method should be overridden by subclasses.
        """
        raise NotImplementedError("generate_signals method must be implemented in subclasses.")


