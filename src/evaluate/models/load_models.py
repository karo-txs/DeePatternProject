from train.train_facade import load_trained_model
from deepattern import Strategy


class LoadModelsStrategy(Strategy):

    def run_strategy(self):
        self.transitional_object.create_attr("eval_models", [])

        for model_name in self.cfg.model_names:
            best_model_path_splited = self.cfg.save_model_dir.split("/")
            best_model_path_splited[-1] = model_name
            self.cfg.save_model_dir = "/".join(best_model_path_splited)

            load_trained_model(setup=False)
            self.transitional_object.eval_models.append({"name": model_name, "model": self.transitional_object.keras_model})
