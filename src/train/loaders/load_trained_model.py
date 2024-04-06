from deepattern import Strategy
import os


class LoadTrainedModelStrategy(Strategy):

    def run_strategy(self):
        best_model_path = os.path.join(self.cfg.save_model_dir, 'best_model.keras')
        model = load_model(best_model_path)
        self.transitional_object.create_attr("keras_model", model)