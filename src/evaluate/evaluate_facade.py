import os
import sys
from deepattern import StrategyHandler, ConfigSingleton

current_directory = os.path.dirname(os.path.abspath(__file__))
src_directory = os.path.join(current_directory, '../../', 'src')
sys.path.append(src_directory)

from evaluate import *
from train import train_facade
from data import data_facade

def config_setup():
    cfg = ConfigSingleton().load_config(filepath="../assets/configs/evaluate_config.toml")
    if not os.path.exists(cfg.save_path):
        os.makedirs(cfg.save_path)
    data_facade.config_setup()
    train_facade.config_setup()

def run_chain(handler):
    config_setup()
    while handler.handle():
        continue

def evaluate_models():
    basic_strategies = [LoadTestCasesStrategy(),
                        LoadModelsStrategy(),
                        EvaluateRunnerStrategy(),
                        ClassificationReportStrategy()
                        ]
    handler = StrategyHandler.builder(basic_strategies)

    run_chain(handler)


if __name__ == "__main__":
    evaluate_models()
