# Crop Disease Detector

An AI-powered web application that detects crop diseases from leaf images using a deep learning model. The application helps farmers, students, and researchers quickly identify plant diseases by providing disease predictions, confidence scores, disease descriptions, and AI-generated remedies. It also supports bilingual interaction (English and Hindi) with voice output for improved accessibility.

## Features

* Upload a leaf image for disease detection.
* AI-powered crop disease classification using a deep learning model.
* Supports multiple crop species and disease categories.
* Detects both healthy and diseased leaves.
* Displays prediction confidence scores.
* Provides disease descriptions and AI-generated remedies.
* Text-to-Speech (Voice Output) for prediction results and remedies.
* Bilingual support (English and Hindi) for disease information and voice responses.
* Clean, responsive, and user-friendly Gradio interface.

## Dataset

This project is trained using the **PlantVillage Dataset**, a publicly available benchmark dataset for plant disease classification. The dataset contains **54,306** labeled images of healthy and diseased plant leaves spanning **14 crop species** and **38 classes** (healthy and disease categories). It is one of the most widely used datasets for developing and evaluating deep learning models for plant disease detection.

**Dataset Repository:**
https://github.com/spmohanty/plantvillage-dataset


## Model

The disease classification model is built using **EfficientNet-B0** with transfer learning. The model is trained on the PlantVillage dataset to classify healthy and diseased crop leaves with high accuracy.

## Installation

### Clone the repository

```bash
git clone https://github.com/shyam503/Crop-Disease-Detector.git
cd Crop-Disease-Detector
```

## Run the Application

```bash
python app.py
```

Open the local Gradio URL displayed in the terminal to access the application in your web browser.

## How to Use

1. Launch the application.
2. Upload a crop leaf image.
3. Click **Analyze**.
4. View the predicted crop, disease, confidence score, and disease description.
5. Review the AI-generated remedy.
6. Listen to the result using the voice output feature.
7. Switch between English and Hindi as needed.
