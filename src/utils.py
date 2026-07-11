import os

from src.config import (
    EXAMPLES_DIR,
    SUPPORTED_IMAGE_EXTENSIONS,
)


def is_hindi(language: str) -> bool:
    return language.startswith("हिन्दी")


def parse_class_name(class_name: str) -> dict:
    parts = class_name.split("___")

    plant = parts[0].replace("_", " ").title()

    disease = (
        parts[1].replace("_", " ").title()
        if len(parts) > 1
        else "Unknown"
    )

    return {
        "plant": plant,
        "disease": disease,
        "is_healthy": "healthy" in disease.lower(),
    }


def build_result(
    class_name: str,
    confidence: float,
):

    info = parse_class_name(class_name)

    return {
        "class_name": class_name,
        "plant": info["plant"],
        "disease": info["disease"],
        "confidence": round(confidence * 100, 1),
        "is_healthy": info["is_healthy"],
    }


def build_label_dict(results):
    return {
        f"{r['plant']} — {r['disease']}":
        r["confidence"] / 100
        for r in results
    }


def build_status_html(
    prediction: dict,
    hindi: bool,
):

    if prediction["is_healthy"]:

        title = "पौधा स्वस्थ है" if hindi else "Plant is Healthy!"

        return f"""
<div style="color:black;">
<h2>✅ {title}</h2>

<b>{"पौधा" if hindi else "Plant"}:</b>
{prediction["plant"]}<br>

<b>{"विश्वास" if hindi else "Confidence"}:</b>
{prediction["confidence"]}%

</div>
"""

    title = "रोग पाया गया" if hindi else "Disease Detected"

    return f"""
<div style="color:black;">
<h2>⚠️ {title}</h2>

<b>{"पौधा" if hindi else "Plant"}:</b>
{prediction["plant"]}<br>

<b>{"रोग" if hindi else "Disease"}:</b>
{prediction["disease"]}<br>

<b>{"विश्वास" if hindi else "Confidence"}:</b>
{prediction["confidence"]}%

</div>
"""


def get_example_images():

    os.makedirs(EXAMPLES_DIR, exist_ok=True)

    files = sorted(
        f
        for f in os.listdir(EXAMPLES_DIR)
        if f.lower().endswith(
            SUPPORTED_IMAGE_EXTENSIONS
        )
    )

    return [
        [os.path.join(EXAMPLES_DIR, f), "English"]
        for f in files
    ]