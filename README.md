# CRM FAQ Bot (Streamlit + GPT)

This is a simple CRM FAQ chatbot powered by OpenAI's GPT-4o model and Streamlit. It uses an Excel file as a mock CRM database.

## 🔧 How to Run

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Set your OpenAI API key using Streamlit secrets:

Create a `.streamlit/secrets.toml` file:
```
[OPENAI_API_KEY]
OPENAI_API_KEY = "sk-your-api-key"
```

3. Run the app:
```
streamlit run crm_faq_bot_app.py
```

## 📁 Files Included

- `crm_faq_bot_app.py` – Main Streamlit app
- `crm_data.xlsx` – Dummy CRM records (10 entries)
- `requirements.txt` – Python dependencies
- `README.md` – Setup instructions