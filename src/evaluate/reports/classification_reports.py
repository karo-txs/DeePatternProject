from evaluate.test_cases.load_test_cases import LoadTestCasesStrategy
from evaluate.models.load_models import LoadModelsStrategy
from sklearn.metrics import classification_report
from evaluate.reports import utils
from deepattern import Strategy
import pandas as pd


class ClassificationReportStrategy(Strategy):

    def __post_init__(self):
        self.depends_on = [LoadTestCasesStrategy, LoadModelsStrategy]

    def run_strategy(self):

        report_dicts = []
        
        for evaluate_runner in  self.transitional_object.collection:
            evaluate_runner.evaluate()
            report = classification_report(self.transitional_object.y_true, 
                                           self.transitional_object.y_pred, 
                                           output_dict=True)
            report_dict = {
                "test_case": evaluate_runner.test_case_name,
                "accuracy": report["accuracy"],
                "recall_macro_avg": report["macro avg"]["recall"],
                "precision_macro_avg": report["macro avg"]["precision"],
                "f1_macro_avg": report["macro avg"]["f1-score"],
                "recall_weighted": report["weighted avg"]["recall"],
                "precision_weighted": report["weighted avg"]["precision"],
                "f1_weighted": report["weighted avg"]["f1-score"],
                'average_inference_time': self.transitional_object.average_inference_time,
                'throughput': self.transitional_object.throughput
            }

            df_temp = pd.DataFrame(report_dict, index=[evaluate_runner.model_name])
            report_dicts.append(df_temp)

            dfs = []
            for label, metrics in report.items():
                if label not in ("accuracy", "macro avg", "weighted avg"):
                    metrics["model_name"] = evaluate_runner.model_name
                    metrics["test_case"] = evaluate_runner.test_case_name
                    df_temp = pd.DataFrame(metrics, index=[label])
                    dfs.append(df_temp)

            df_classes = pd.concat(dfs)
            df_classes.reset_index(inplace=True)
            df_classes.rename(columns={"index": "class"}, inplace=True)

            utils.add_new_results(self.cfg, df_classes, "report_classes")
        
        df_report = pd.concat(report_dicts)
        df_report.reset_index(inplace=True)
        df_report.rename(columns={"index": "model_name"}, inplace=True)
        utils.add_new_results(self.cfg, df_report)
