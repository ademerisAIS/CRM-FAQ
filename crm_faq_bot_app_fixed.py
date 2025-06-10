
import streamlit as st
import pandas as pd
from openai import OpenAI

# --- CONFIGURATION ---
st.set_page_config(page_title="CRM FAQ Bot", layout="centered")
st.title("🤖 CRM FAQ Chatbot")

# --- Initialize OpenAI client ---
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# --- LOAD DATA ---
@st.cache_data
def load_data(file_path):
    return pd.read_excel(file_path)

df = load_data("crm_data.xlsx")

# --- DISPLAY DATA (optional for user transparency) ---
with st.expander("📊 View CRM Data"):
    st.dataframe(df)

# --- USER QUESTION INPUT ---
user_question = st.text_input("Ask a question about a customer:", placeholder="e.g., What is the status of Acme Inc?")

if user_question:
    # Convert data to string context
    data_context = df.to_string(index=False)

    # Build prompt
    prompt = f"""
You are a helpful assistant. Use the following CRM data to answer the user's question.

CRM Data:
{data_context}

Question: {user_question}
Answer:
"""

    # Call GPT using new SDK format
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a CRM assistant answering user questions using the data provided."},
            {"role": "user", "content": prompt}
        ]
    )

    # Show the answer
    answer = response.choices[0].message.content.strip()
    st.markdown("### 🤖 Answer")
    st.success(answer)
