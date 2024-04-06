from deepattern import ModelBuilder, ConfigSingleton
from model.core.tf_model import TFModel
from model.layers import *


class FullyConnectedModelBuilder(ModelBuilder):

    def __init__(self) -> None:
        self.reset()
        self.cfg = ConfigSingleton()

    def reset(self) -> None:
        self._model = TFModel()

    @property
    def model(self) -> TFModel:
        model = self._model
        self.reset()
        return model

    def include_input(self) -> None:
        self._model.add(input_embbeder())

    def include_hidden(self) -> None:
        for i in range(0, self.cfg.arch_layers):
            self._model.add(hidden_dense())

    def include_output(self) -> None:
        self._model.add(output_softmax())

    def compile(self) -> None:
        self._model.compile()
