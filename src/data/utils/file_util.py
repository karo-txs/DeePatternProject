import os

def save_data(path: str):
    pass

def create_dict_datasets(base_path):
    splits = ["train", "test", "val"]
    dataset_dict = {}

    for split in splits:
        split_path = os.path.join(base_path, split)

        if os.path.exists(split_path) and os.path.isdir(split_path):
            for data_folder in os.listdir(split_path):
                caminho_arquivo = os.path.join(split_path, data_folder)

                if not os.path.isfile(caminho_arquivo):
                    dataset_dict[data_folder] = split

    return dataset_dict