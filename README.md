# 💬 Real-Time Sentiment Analysis Using Neural Networks and Streamlit App
## 📘 Project Overview

This project aims to build a real-time sentiment analysis system that classifies user input text (e.g., reviews or feedback) as Positive, Negative, or Neutral using deep learning techniques.
It integrates a neural network model trained on a public dataset (IMDb) and an interactive Streamlit web application for real-time inference and visualization.

The project demonstrates the end-to-end workflow of data preprocessing, model development, evaluation, and deployment — showcasing how Natural Language Processing (NLP) can be applied for customer feedback analysis and opinion mining.

## 🚀 Key Features

🔤 Text Preprocessing — Tokenization, stopword removal, lemmatization

🧠 Deep Learning Model — Neural network built using TensorFlow/Keras

💬 Real-Time Prediction — Streamlit interface for live user input

📊 Visualization — Confidence scores and sentiment probabilities

☁️ Deployment Ready — Deployable on Streamlit Cloud, Render, or AWS

## 🧩 Key Skills

Programming: Python
Libraries: TensorFlow, Keras, Scikit-learn, Pandas, NumPy, Matplotlib, NLTK, Hugging Face
Frontend: Streamlit
Deployment: Streamlit Cloud / AWS
Version Control: Git, GitHub

## 📊 Project Workflow
1. Data Collection

Dataset: IMDb Movie Reviews Dataset
 from Hugging Face

50,000 labeled movie reviews for binary sentiment classification (positive/negative).

2. Data Preprocessing

Cleaned text data: lowercasing, punctuation removal, and tokenization.

Used NLTK for stopword removal and Word Embeddings (GloVe) for feature representation.

3. Model Development

Implemented a 3-layer neural network with embedding, LSTM, and dense layers.

Activation: ReLU and Sigmoid

Optimizer: Adam | Loss: Binary Crossentropy

Achieved ~90% accuracy on test data.

4. Evaluation

Metrics: Accuracy, Precision, Recall, F1-Score, and Confusion Matrix

Visualized training history (loss & accuracy curves).

5. Streamlit App Development

Designed a simple and interactive UI where users can:

Enter custom text

View sentiment result instantly

See model confidence level

## 🧠 Key Learnings
Practical implementation of NLP & Deep Learning models.

Experience in model deployment and real-time inference.

Understanding of text preprocessing and embeddings in sentiment analysis.

Integration of AI model with web frameworks like Streamlit.

## 🙌 Future Enhancements

Extend model to multi-class sentiment classification (e.g., 5-star ratings).

Use transformer-based models (BERT, DistilBERT) for improved accuracy.

Add data visualization dashboard for sentiment trends over time.

Enable API endpoint for integration with other applications.

## 👩‍💻 Author

Bhuvana Sangari
📍 Data Science Student | AI & NLP Enthusiast
🔗 LinkedIn
 | GitHub

## Application
![Screenshot 2025-06-12 221407](https://github.com/user-attachments/assets/d3e5532f-44d9-463b-85a6-921bb033928e)

