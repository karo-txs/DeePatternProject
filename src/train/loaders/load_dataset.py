from data.data_facade import load_dataset, set_dataset_path, config_setup
from deepattern import Strategy


class LoadDatasetStrategy(Strategy):

    def run_strategy(self):
        config_setup()
        self.cfg.exporter_dataset_path = f"{self.cfg.setup_data_path}{self.cfg.train_dataset_data_name}/tfrecord/{self.cfg.train_dataset_data_subname}"
        set_dataset_path(self.cfg.train_dataset_data_name, self.cfg.train_dataset_data_subname)
        load_dataset()
