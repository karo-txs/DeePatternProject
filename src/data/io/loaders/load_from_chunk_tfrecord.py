from data.io.loaders.load_from_tfrecord import LoaderFromTFRecordStrategy
import json


class LoaderFromChunkTFRecordStrategy(LoaderFromTFRecordStrategy):

    def load(self):
        info_file_path = f'{self.cfg.exporter_dataset_path}/info.json'

        with open(info_file_path, 'r') as json_file:
            info_data = json.load(json_file)
        
        datasets = []
        dataset_size_sum = 0
        
        for chunk in info_data.keys():
            continue

        data = datasets[0]
        for dataset in datasets[1:]:
            data = data.concatenate(dataset)

        self.transitional_object.create_attr(f"dataset", data).create_attr(f"dataset_size_all", dataset_size_sum)
        self.transitional_object.create_attr("split_name", "all")
