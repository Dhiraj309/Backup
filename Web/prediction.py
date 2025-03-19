# prediction.py
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Load model and tokenizer
model_dir = "Model/Text/my_model_v2/"  # Path to your model directory
tokenizer = AutoTokenizer.from_pretrained(model_dir)
model = AutoModelForSequenceClassification.from_pretrained(model_dir)

# Move the model to GPU if available, else stay on CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

label_map = {
    'Artificial Intelligence': 0,
    'Robotics': 1,
    'Cybersecurity': 2,
    'Software Development': 3,
    'Hardware and Devices': 4,
    'Cloud Computing': 5,
    'Blockchain__Cryptocurrencies': 6,
    'Virtual_Reality_VR_Augmented_Reality_AR': 7,
    'Data Science Analytics': 8,
    'Quantum Computing': 9,
    'Internet of Things IoT': 10,
    'Machine Learning': 11,
    '3D Printing': 12,
    'Tech Startups': 13,
    'Biotechnology': 14,
    'Mobile Technology': 15,
    'Wearables': 16,
    'Ecommerce Technology': 17,
    'Social Media Platforms': 18,
    'Emerging Technologies': 19,
    'Tech Innovations': 20,
    'Smart Homes': 21,
    'Big Data': 22,
    'Tech Ethics': 23,
    'Tech Policy Regulation': 24
}

label_map_inv = {i: label for label, i in label_map.items()}

# Prediction function
def predict(texts):
    inputs = tokenizer(texts, truncation=True, max_length=512, return_tensors="pt")
    input_ids, attention_mask = inputs["input_ids"], inputs["attention_mask"]
    input_ids, attention_mask = input_ids.to(device), attention_mask.to(device)

    model.eval()
    with torch.no_grad():
        outputs = model(input_ids=input_ids, attention_mask=attention_mask)
        logits = outputs.logits
        preds = torch.argmax(logits, dim=1).cpu().numpy()

    return [label_map_inv[pred] for pred in preds]

# import numpy as numpy
# import tensorflow as tf
# from tensorflow.keras.layers import Input, Dense, Dropout, GlobalAveragePooling1D
# from transformers import TFDistilBertModel, DistilBertTokenizerFast

# MODEL_PATH = "Model/Final Model/saved_my_model.keras"
# TOKENIZER_PATH = "Model/Final Model/tokenizer_saved.zip/"

# model = TFDistilBertModel.from_pretrained(MODEL_PATH)
# tokenizer = DistilBertTokenizerFast.from_pretrained(TOKENIZER_PATH)

# def build_model():
#     bert_model = TFDistilBertModel.from_pretrained("distilbert-base-uncased")
#     input_ids = Input(shape = (512,), dtype = tf.float32, name = "input_ids")
#     attention_mask = Input(shape = (512, ), dtype = tf.float32, name = "attention_mask")

#     bert_output = bert_model(input_ids = input_ids, attention_mask = attention_mask)