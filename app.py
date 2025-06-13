import streamlit as st
import json
import pandas as pd
from openai import OpenAI

st.set_page_config(page_title="Flashcard Generator", layout="wide")
st.title("📚 Flashcard Generator using OpenAI GPT-3.5")

openai_api_key = st.text_input("Enter your OpenAI API Key:", type="password")

topic = st.text_input("Enter a topic:")
generate_btn = st.button("Generate Flashcards")

if generate_btn and openai_api_key and topic:
    st.info("Generating flashcards...")
    # Simulated flashcards (in actual use, call OpenAI API)
    flashcards = [
        {"question": "What is AI?", "answer": "AI stands for Artificial Intelligence."},
        {"question": "Name a type of machine learning.", "answer": "Supervised learning."}
    ]
    df = pd.DataFrame(flashcards)
    st.dataframe(df)
    st.download_button("Download JSON", json.dumps(flashcards), file_name="flashcards.json")
    st.download_button("Download CSV", df.to_csv(index=False), file_name="flashcards.csv")