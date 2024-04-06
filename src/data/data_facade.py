import os
import sys
from deepattern import StrategyHandler, ConfigSingleton

current_directory = os.path.dirname(os.path.abspath(__file__))
src_directory = os.path.join(current_directory, '../../', 'src')
sys.path.append(src_directory)

from data import *


def config_setup():
    cfg = ConfigSingleton().load_config(filepath="../assets/configs/data_config.toml")
    data_splits = file_util.create_dict_datasets(cfg.setup_data_path)
    
    cfg.create_attr("data_splits", data_splits)
    set_dataset_path(cfg.loader_data_name, cfg.loader_data_subname)
    
def set_dataset_path(data_name: str, data_subname: str):
    cfg = ConfigSingleton()
    split = cfg.data_splits.get(data_name)
    cfg.create_attr("dataset_path", f"{cfg.setup_data_path}/{split}/{data_name}/data/{data_subname}")
    cfg.create_attr("exporter_dataset_path", f"{cfg.setup_data_path}/{split}/{data_name}/tfrecord/{data_subname}")

def run_chain(handler):
    while handler.handle():
        continue
    
def load_dataset():
    handler = StrategyHandler.builder([LoaderFromTFRecordStrategy()])
    run_chain(handler)

def frames_capture():
    handler = StrategyHandler.builder(VideoToFramesConverterStrategy())
    run_chain(handler)

def run_dataset_preparation():
    config_setup()
    cfg = ConfigSingleton()
    if cfg.setup_pipeline_type == "landmark":
        sub_strategies = [CaptureImagesStrategy(),
                            CreateTFDatasetStrategy(),
                            NormalizerImageStrategy(),
                            Embedder(),
                            ExporterTFRecordStrategy(),
                            ]
    else:
        raise Exception("No pipelines selected!")

    basic_strategies = [LoaderFromFolderStrategy(),
                       ChunkExecutorStrategy().set_sub_strategies(sub_strategies=sub_strategies, chunk=cfg.loader_chunk_size),
                       ]

    if cfg.data_splits.get(cfg.loader_data_name) == "train":
        basic_strategies.extend([LoaderFromChunkTFRecordStrategy(),
                                 TrainValSpliterStrategy()])
    else:
        basic_strategies.extend([LoaderFromChunkTFRecordStrategy(),
                                 ExporterTFRecordStrategy()])
        
    handler = StrategyHandler.builder(basic_strategies)

    run_chain(handler)

if __name__ == "__main__":
    run_dataset_preparation()
