from deepattern import TransitionalObject
from dataclasses import dataclass
from tqdm import tqdm
import numpy as np
import time


@dataclass
class EvaluateRunnerObject:
    model: any
    model_name: str
    test_case: any
    test_case_name: str
    test_case_size: int

    def __post_init__(self):
        self.transitional_object = TransitionalObject() 

    def evaluate(self):
        y_true = []
        y_pred = []
        total_inference_time = 0
        total_samples = 0

        for inputs, labels in tqdm(self.test_case, desc="Evaluating dataset", total=self.test_case_size):
            start_time = time.time()
            batch_predictions = self.model.predict(inputs, verbose=0)
            total_inference_time += time.time() - start_time
            total_samples += 1

            batch_pred_labels = np.argmax(batch_predictions, axis=1)
            labels_indices = np.argmax(labels, axis=0)
            y_true.extend([labels_indices])
            y_pred.extend(batch_pred_labels)
        
        average_inference_time = total_inference_time / total_samples
        throughput = total_samples / total_inference_time

        self.transitional_object.create_attr(f"y_true", np.array(y_true))\
                .create_attr(f"y_pred", np.array(y_pred))\
                .create_attr(f"average_inference_time", average_inference_time)\
                .create_attr(f"throughput", throughput)
