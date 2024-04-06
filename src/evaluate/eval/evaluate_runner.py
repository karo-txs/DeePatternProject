from evaluate.eval.evaluate_runner_object import EvaluateRunnerObject
from evaluate.test_cases.load_test_cases import LoadTestCasesStrategy
from evaluate.models.load_models import LoadModelsStrategy
from deepattern import Strategy, Collection


class EvaluateRunnerStrategy(Strategy):

    def __post_init__(self):
        self.depends_on = [LoadTestCasesStrategy, LoadModelsStrategy]

    def run_strategy(self):
        collection = Collection()

        for eval_model in self.transitional_object.eval_models:
            for eval_test_case in self.transitional_object.eval_test_cases:
                collection.add_item(EvaluateRunnerObject(test_case=eval_test_case["dataset"], 
                                                        test_case_name=eval_test_case["name"], 
                                                        test_case_size=eval_test_case["size"], 
                                                        model=eval_model["model"],
                                                        model_name=eval_model["name"]))
        
        self.transitional_object.create_attr("collection", collection)
