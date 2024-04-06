from abc import ABC, abstractmethod
from deepattern import Strategy


class LoadProcessedData(Strategy, ABC):

    @abstractmethod
    def load(self):
        pass

    def run_strategy(self):
        self.load()


class LoadRawData(Strategy, ABC):

    @abstractmethod
    def load(self):
        pass

    def run_strategy(self):
        self.load()


class ExportProcessedData(Strategy, ABC):

    def __post_init__(self):
        self.depends_on = [CreationStructure]

    @abstractmethod
    def export(self):
        pass

    def run_strategy(self):
        self.export()

class CaptureOfData(Strategy, ABC):

    def __post_init__(self):
        self.depends_on = [LoadRawData]

    @abstractmethod
    def capture(self):
        pass

    def run_strategy(self):
        self.capture()

class CreationStructure(Strategy, ABC):

    def __post_init__(self):
        self.depends_on = [CaptureOfData]

    @abstractmethod
    def create(self):
        pass

    def run_strategy(self):
        self.create()

class Split(Strategy, ABC):

    def __post_init__(self):
        self.depends_on = [CreationStructure]

    @abstractmethod
    def split(self):
        pass

    def run_strategy(self):
        self.split()

class Normalizer(Strategy, ABC):

    def __post_init__(self):
        self.depends_on = [CreationStructure]

    @abstractmethod
    def normalize(self):
        pass

    def run_strategy(self):
        self.normalize()

class Embedder(Strategy, ABC):

    def __post_init__(self):
        self.depends_on = [CreationStructure, Normalizer]

    @abstractmethod
    def apply(self):
        pass

    def run_strategy(self):
        self.apply()

class Augmentation(Strategy, ABC):

    def __post_init__(self):
        self.depends_on = [CreationStructure, Normalizer]

    @abstractmethod
    def apply(self):
        pass

    def run_strategy(self):
        self.apply()

class Transform(Strategy, ABC):

    def __post_init__(self):
        self.depends_on = [CreationStructure, Normalizer, Embedder]

    @abstractmethod
    def transform(self):
        pass

    def run_strategy(self):
        self.transform()
