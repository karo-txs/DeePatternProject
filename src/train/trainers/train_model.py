from train.customizations.set_callbacks import SetCallbacksStrategy
from deepattern import Strategy


class TrainStrategy(Strategy):

    def __post_init__(self):
        self.depends_on = [SetCallbacksStrategy]

    def run_strategy(self):
        pass
