from model.model_facade import load_model, config_setup
from deepattern import Strategy


class LoadModelArchitectureStrategy(Strategy):

    def run_strategy(self):
        config_setup()
        self.cfg.input_size = self.cfg.features_embedding_size
        load_model(setup=False)