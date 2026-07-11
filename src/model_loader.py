import json
import os

import torch
import torch.nn as nn
import torchvision.models as models

from src.config import DEVICE, MODEL_PATH
from src.remedy import REMEDY_MAP


def _load_class_names():
    # if os.path.exists(MODEL_PATH):
    #     checkpoint = torch.load(MODEL_PATH, map_location=DEVICE)
    #     return checkpoint["class_names"], checkpoint["num_classes"]

    # if os.path.exists("class_names.json"):
    #     with open("class_names.json", "r") as f:
    #         class_names = json.load(f)
    #     return class_names, len(class_names)

    class_names = sorted(REMEDY_MAP.keys())
    return class_names, len(class_names)


def load_model():
    class_names, num_classes = _load_class_names()

    model = models.efficientnet_b0(weights=None)

    model.classifier[1] = nn.Linear(
        model.classifier[1].in_features,
        num_classes,
    )

    if os.path.exists(MODEL_PATH):
        checkpoint = torch.load(
            MODEL_PATH,
            map_location=DEVICE,
        )

        model.load_state_dict(
            checkpoint
        )

    model.to(DEVICE)
    model.eval()

    return model, class_names