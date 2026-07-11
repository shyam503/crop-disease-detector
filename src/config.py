import os
import torch
import torchvision.transforms as transforms

# Device Configuration
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Model Configuration
MODEL_PATH = "efficientnet_plant_disease.pth"

# Image Preprocessing
INFER_TRANSFORM = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225],
    ),
])


# Example Images
EXAMPLES_DIR = os.path.join(
    os.getcwd(),
    "example_images"
)

SUPPORTED_IMAGE_EXTENSIONS = (
    ".jpg",
    ".jpeg",
    ".png",
)


# UI Settings
APP_TITLE = "🌿 Crop Disease Detector"

DEFAULT_LANGUAGE = "English"

LANGUAGES = [
    "English",
    "हिन्दी (Hindi)",
]