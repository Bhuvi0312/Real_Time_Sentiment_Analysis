{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5c1e34db",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "from transformers import BertTokenizer, BertForSequenceClassification\n",
    "import torch\n",
    "\n",
    "# Load model\n",
    "model = BertForSequenceClassification.from_pretrained(\"sentiment_model\")\n",
    "tokenizer = BertTokenizer.from_pretrained(\"sentiment_model\")\n",
    "model.eval()\n",
    "\n",
    "st.title(\"Real-Time Sentiment Analysis\")\n",
    "\n",
    "user_input = st.text_area(\"Enter your feedback:\")\n",
    "if st.button(\"Predict\"):\n",
    "    inputs = tokenizer(user_input, return_tensors=\"pt\", truncation=True, padding=True, max_length=128)\n",
    "    with torch.no_grad():\n",
    "        outputs = model(**inputs)\n",
    "        prediction = torch.argmax(outputs.logits, dim=1).item()\n",
    "        label_map = {0: \"Negative\", 1: \"Positive\", 2: \"Neutral\"}\n",
    "        st.write(f\"Sentiment: **{label_map[prediction]}**\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "py311",
   "language": "python",
   "name": "py311"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
