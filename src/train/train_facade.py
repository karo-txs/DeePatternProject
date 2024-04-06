import os
import sys
from deepattern import StrategyHandler, ConfigSingleton

current_directory = os.path.dirname(os.path.abspath(__file__))
src_directory = os.path.join(current_directory, '../../', 'src')
sys.path.append(src_directory)

from train import *

def config_setup():
    cfg = ConfigSingleton().load_config(filepath="../assets/configs/train_config.toml")
    cfg.create_attr("save_model_dir", f"{cfg.experiment_save_dir}/{cfg.experiment_name}")

def run_chain(handler, setup: bool = True):
    if setup:
        config_setup()
    while handler.handle():
        continue
    
def hyperparameter_tuner():
    handler = StrategyHandler.builder([LoadDatasetStrategy(),
                                       LoadModelArchitectureStrategy(),
                                       SetCallbacksStrategy(),
                                       TunerStrategy(),
                                       ])
    run_chain(handler)

def cross_validation_train():
    pass

def base_train():
    handler = StrategyHandler.builder([LoadDatasetStrategy(),
                                       LoadModelArchitectureStrategy(),
                                       SetCallbacksStrategy(),
                                       TrainStrategy(),
                                       ])
    run_chain(handler)

def load_trained_model(setup: bool = True):
    handler = StrategyHandler.builder([LoadTrainedModelStrategy()])
    run_chain(handler, setup)

def load_trained_model_by_epoch(epoch: int, setup: bool = True):
    pass

if __name__ == "__main__":
    hyperparameter_tuner()
