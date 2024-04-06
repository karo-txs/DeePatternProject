from train.customizations.set_callbacks import SetCallbacksStrategy
from deepattern import Strategy


class TunerStrategy(Strategy):

    def __post_init__(self):
        self.depends_on = [SetCallbacksStrategy]

    def run_strategy(self):
        pass
