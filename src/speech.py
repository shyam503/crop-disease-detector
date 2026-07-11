import tempfile

from src.remedy import REMEDY_MAP, DEFAULT_REMEDY


def get_remedy(class_name: str, lang: str = "en") -> str:
    entry = REMEDY_MAP.get(class_name, DEFAULT_REMEDY)
    return entry.get(lang, entry["en"])


def speak_gtts(text: str, lang_code: str = "hi"):
    try:
        from gtts import gTTS

        tts = gTTS(
            text=text,
            lang=lang_code,
            slow=False,
        )

        tmp = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp3",
            prefix="crop_voice_",
        )

        tts.save(tmp.name)

        return tmp.name

    except Exception as e:
        print(f"[gTTS] {e}")
        return None


def speak_pyttsx3(text: str):
    try:
        import pyttsx3

        engine = pyttsx3.init()

        engine.setProperty("rate", 130)
        engine.setProperty("volume", 1.0)

        tmp = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".wav",
            prefix="crop_voice_",
        )

        engine.save_to_file(text, tmp.name)
        engine.runAndWait()

        return tmp.name

    except Exception as e:
        print(f"[pyttsx3] {e}")
        return None


def _build_spoken_message(
    class_name: str,
    language: str,
):

    is_hindi = language.startswith("हिन्दी")

    remedy = get_remedy(
        class_name,
        lang="hi" if is_hindi else "en",
    )

    parts = class_name.split("___")

    plant = parts[0].replace("_", " ")

    disease = (
        parts[1].replace("_", " ")
        if len(parts) > 1
        else "Unknown"
    )

    healthy = "healthy" in disease.lower()

    if is_hindi:

        if healthy:
            return (
                f"{plant} का पौधा स्वस्थ है। "
                f"{remedy}"
            )

        return (
            f"ध्यान दें। "
            f"{plant} में {disease} रोग पाया गया। "
            f"उपचार सुनें। "
            f"{remedy}"
        )

    if healthy:

        return (
            f"Good news. "
            f"Your {plant} plant is healthy. "
            f"{remedy}"
        )

    return (
        f"Attention. "
        f"{disease} detected on your "
        f"{plant} plant. "
        f"Treatment: {remedy}"
    )


def speak_result(
    class_name: str,
    language: str,
):

    is_hindi = language.startswith("हिन्दी")

    spoken_text = _build_spoken_message(
        class_name,
        language,
    )

    audio = speak_gtts(
        spoken_text,
        "hi" if is_hindi else "en",
    )

    if audio:
        return audio

    return speak_pyttsx3(spoken_text)