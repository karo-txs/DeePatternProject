from deepattern import load_classes_in_package
from model.core.tf_model import TFModel
from model import builder

MODELS = load_classes_in_package(builder, "ModelBuilder")