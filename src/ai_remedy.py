import os
from google import genai
from google.genai import types
from dotenv import load_dotenv


load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_dynamic_remedy(disease_name, confidence_score, lang):

    if confidence_score < 0.60:
        return f" Please consult your local Krishi Vigyan Kendra (KVK) for advice."

    if "Healthy" in disease_name:
        return f" Great news! your plant is healthy. Keep up your current watering and sunlight routine!"

    # The hidden instructions for the LLM
    prompt = f"""
    You are an expert agricultural botanist and plant pathologist.
    A user has uploaded an image of a crop leaf. Our Computer Vision AI has diagnosed
    the leaf with '{disease_name}' with a confidence of {confidence_score*100:.1f}%.

    Please provide a short and concise, highly structured treatment plan using Markdown.
    Include the following sections exactly:
    1. One-liner explanation of what this disease is.
    2. Remedies/Treatment (2 bullet points, one liner each).

    Please provide answer based on language '{lang}'. If '{lang}' is "hi", kindly provide answer
    in hindi.

    Keep the tone professional, urgent but reassuring, and easy for a home gardener to understand.
    Do not mention that you are an AI.
    """

    try:
        # set temperature to 0.2 to make the AI factual and prevent hallucinations
        response = client.models.generate_content(
            model='gemini-3.5-flash',
            contents=types.Part.from_text(text=prompt),
            config=types.GenerateContentConfig(
                temperature=0.2,
    ),
)
        return response.text
    except Exception as e:
        print(e)
        return None