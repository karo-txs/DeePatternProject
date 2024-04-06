from deepattern import Model


class TFModel(Model):
    def __init__(self) -> None:
        self.parts = []

    def add(self, part) -> None:
        if isinstance(part, list):
            self.parts.extend(part)
        else:
            self.parts.append(part)
    
    def compile(self, optimizer, loss, metrics):
        inputs = self.parts[0]
        outputs = inputs
        
        for layer in self.parts[1:]:
           outputs = layer(outputs)
        
        self.model = any

        self.model.compile(
            optimizer=optimizer,
            loss=loss,
            metrics=metrics,
        )

    def get_model(self) -> any:
        return self.model

