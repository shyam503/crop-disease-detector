import gradio as gr

from src.styles import CSS
from src.config import (
    APP_TITLE,
    DEFAULT_LANGUAGE,
    LANGUAGES,
)

from src.predictor import predict_with_voice
from src.utils import get_example_images


def create_ui():

    with gr.Blocks(css=CSS, title=APP_TITLE) as demo:

        gr.HTML("""
        <div class="hero">
        <link rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/tabler-icons.min.css">

        <h1>🌿 Crop Disease Detector</h1>

        <p>
        AI-powered crop disease diagnosis with treatment guide,
        confidence scores and voice assistance.
        </p>

        </div>
        """)

        with gr.Row(equal_height=True):

            # -----------------------------
            # LEFT PANEL
            # -----------------------------

            with gr.Column(scale=1):

                gr.HTML('<div class="card">')

                image_input = gr.Image(
                    type="pil",
                    label="### 📷 Upload Leaf Photo",
                    sources=["upload", "webcam"],
                    height=420,
                )

                language_radio = gr.Radio(
                    choices=LANGUAGES,
                    value=DEFAULT_LANGUAGE,
                    show_label=False,
                )

                predict_btn = gr.Button(
                    "🔍 Analyse Leaf",
                    variant="primary",
                    elem_classes=["predict-btn"],
                )

                gr.Examples(
                    examples=get_example_images(),
                    inputs=[image_input, language_radio],
                    label="Example Leaves",
                )

                gr.HTML("</div>")

            # -----------------------------
            # RIGHT PANEL
            # -----------------------------

            with gr.Column(scale=1):

                status_md = gr.Markdown(
"""
# 🌱 Ready

Upload a leaf image and click **Analyse Leaf**
"""
                )

                confidence_label = gr.Label(
                    num_top_classes=3,
                    label="📊 Result Analysis",
                )

                remedy_output = gr.Textbox(
                    label="💊 Treatment Guide",
                    lines=8,
                    interactive=False,
                    placeholder="Treatment recommendations will appear here...",
                )

                gr.HTML("""
                <div class="voice-box">

                <strong>
                🔊 आवाज़ में सुनें / Listen to remedy
                </strong>

                <br>

                <small style="color:#555">

                नीचे Play दबाएं — रोग का नाम और उपचार हिन्दी में सुनें

                <br>

                Press Play below to hear the disease name and remedy

                </small>

                </div>
                """)

                audio_output = gr.Audio(
                    label="🔊 Voice Output",
                    type="filepath",
                    autoplay=True,
                )

        # -----------------------------
        # EVENTS
        # -----------------------------

        predict_btn.click(
            fn=predict_with_voice,
            inputs=[
                image_input,
                language_radio,
            ],
            outputs=[
                confidence_label,
                remedy_output,
                status_md,
                audio_output,
            ],
        )

        language_radio.change(
            fn=predict_with_voice,
            inputs=[
                image_input,
                language_radio,
            ],
            outputs=[
                confidence_label,
                remedy_output,
                status_md,
                audio_output,
            ],
        )

        # -----------------------------
        # HELP
        # -----------------------------

        with gr.Accordion(
            "ℹ️ कैसे उपयोग करें / How to use",
            open=False,
        ):

            gr.Markdown("""

**For Farmers**

1. Upload a leaf

2. Click Analyse

3. Listen to voice

4. Read treatment

""")

        gr.HTML("""

<div style="
text-align:center;
padding:25px;
margin-top:25px;
color:#6B7280;
font-size:13px;
border-top:1px solid #E5E7EB;
">

<strong>🌿 Crop Disease Detector</strong>

<br>

AI-powered crop diagnosis

<br>

EfficientNet-B0

</div>

""")

    return demo