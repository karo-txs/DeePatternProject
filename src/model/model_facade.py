import os
import sys

current_directory = os.path.dirname(os.path.abspath(__file__))
src_directory = os.path.join(current_directory, '../../', 'src')
sys.path.append(src_directory)

from deepattern import Director, ConfigSingleton, TransitionalObject
from model import *


def config_setup():
    ConfigSingleton().load_config(filepath="../assets/configs/model_config.toml")

def load_model(setup: bool = True) -> TFModel:
    if setup:
        config_setup()
        
    cfg = ConfigSingleton()

    if cfg.model_type in MODELS:
        model_class = MODELS[cfg.model_type]
        model_builder = model_class()

    director = Director()
    director.builder = model_builder
    director.build_basic_model()

    TransitionalObject().create_attr("model", model_builder.model.model)

if __name__ == "__main__":
    model = load_model()
    print(model)
