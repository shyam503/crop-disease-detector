import torch
from PIL import Image

from src.config import DEVICE, INFER_TRANSFORM
from src.model_loader import load_model
from src.speech import (
    get_remedy,
    speak_result,
)
from src.utils import (
    is_hindi,
    build_result,
    build_label_dict,
    build_status_html,
)

# Load model only once
MODEL, CLASS_NAMES = load_model()
NUM_CLASSES = len(CLASS_NAMES)


def predict_with_voice(image, language):
    if image is None:
        msg = (
            "कृपया पत्ती की फोटो अपलोड करें।"
            if is_hindi(language)
            else "Please upload a leaf image."
        )

        return {}, msg, "Upload a leaf image to begin", None

    hindi = is_hindi(language)

    # Convert image
    if not isinstance(image, Image.Image):
        image = Image.fromarray(image)

    tensor = (
        INFER_TRANSFORM(image.convert("RGB"))
        .unsqueeze(0)
        .to(DEVICE)
    )

    with torch.no_grad():
        outputs = MODEL(tensor)
        probs = torch.softmax(outputs, dim=1)[0]

    top_probs, top_idxs = torch.topk(
        probs,
        k=min(3, NUM_CLASSES),
    )

    results = []

    for prob, idx in zip(
        top_probs.cpu().tolist(),
        top_idxs.cpu().tolist(),
    ):
        results.append(
            build_result(
                CLASS_NAMES[idx],
                prob,
            )
        )

    top = results[0]

    label_dict = build_label_dict(results)

    remedy = get_remedy(
        top["class_name"],
        "hi" if hindi else "en",
    )

    status = build_status_html(
        top,
        hindi,
    )

    audio = speak_result(
        top["class_name"],
        language,
    )

    return (
        label_dict,
        remedy,
        status,
        audio,
    )