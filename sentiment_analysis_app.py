# -*- coding: utf-8 -*-
"""Sentiment_analysis_app.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kT9MP9gUT0dOQkru22DJEfNFChDQQt8S
"""



import streamlit as st
from transformers import BertTokenizer, BertForSequenceClassification
import torch

st.set_page_config(page_title="Sentiment Analysis", page_icon="https://static.vecteezy.com/system/resources/previews/026/226/868/non_2x/sentiment-analysis-icon-illustration-vector.jpg", layout="centered")

st.markdown(
    """
    <style>
        body {
            background-color: #f0f2f6;
        }
        .stApp {
            background-image: linear-gradient(to right, #ffffff, #e0f7fa);
            color: #000000;
            padding: 20px;
            font-family: 'Segoe UI', sans-serif;
        }
        .stTextInput>div>div>input {
            background-color: #ffffff;
            color: #000000;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="title-container">
        <img src="https://static.vecteezy.com/system/resources/previews/026/226/868/non_2x/sentiment-analysis-icon-illustration-vector.jpg" alt="Logo"  width="30" style="margin-right: 15px;">
        <h1>Real-Time Sentiment Analysis App</h1>
    </div>
    """,
    unsafe_allow_html=True
)

model = BertForSequenceClassification.from_pretrained("C:\\Users\\bhuva\\Downloads\\sentiment_model")
tokenizer = BertTokenizer.from_pretrained("C:\\Users\\bhuva\\Downloads\\sentiment_model")
model.eval()

st.title("💬Real-Time Sentiment Analysis App")

user_input = st.text_area("Enter your feedback:")

if st.button("Predict") and user_input.strip():
    inputs = tokenizer(user_input, return_tensors="pt", truncation=True, padding=True, max_length=128)
    with torch.no_grad():
        outputs = model(**inputs)
        prediction = torch.argmax(outputs.logits, dim=1).item()
        label_map = {0: "Negative", 1: "Positive", 2: "Neutral"}
        st.write(f"Sentiment: **{label_map.get(prediction, 'Unknown')}**")
        
