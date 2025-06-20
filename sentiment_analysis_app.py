# -*- coding: utf-8 -*-
"""Sentiment_analysis_app.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kT9MP9gUT0dOQkru22DJEfNFChDQQt8S
"""



import streamlit as st
from transformers import BertTokenizer, BertForSequenceClassification
import torch

model = BertForSequenceClassification.from_pretrained("sentiment_model")
tokenizer = BertTokenizer.from_pretrained("sentiment_model")
model.eval()

st.title("💬 Real-Time Sentiment Analysis App")

user_input = st.text_area("Enter your feedback:")

if st.button("Predict") and user_input.strip():
    inputs = tokenizer(user_input, return_tensors="pt", truncation=True, padding=True, max_length=128)
    with torch.no_grad():
        outputs = model(**inputs)
        prediction = torch.argmax(outputs.logits, dim=1).item()
        label_map = {0: "Negative", 1: "Positive", 2: "Neutral"}
        st.write(f"Sentiment: **{label_map.get(prediction, 'Unknown')}**")
