from Strategies.base_strategy import BaseStrategy

class LongSaddle(BaseStrategy):
    def __init__(self, name='LongSaddle'):
        super().__init__(name)
        self.name = name