from regex import P
from data.data_facade import load_dataset
from deepattern import Strategy


class LoadTestCasesStrategy(Strategy):

    def run_strategy(self):
        self.transitional_object.create_attr("eval_test_cases", [])

        for test_name in self.cfg.test_cases_names:
            dataset_path_splited = self.cfg.exporter_dataset_path.split("/")
            dataset_path_splited[-3] = test_name
            dataset_path_splited[-1] = self.cfg.test_cases_subname
            self.cfg.exporter_dataset_path = "/".join(dataset_path_splited)
            print(self.cfg.exporter_dataset_path)

            load_dataset()
            self.transitional_object.eval_test_cases.append({"name": test_name, "dataset": self.transitional_object.dataset_all, "size": self.transitional_object.dataset_size_all})
