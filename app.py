from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0, api_key=api_key)

st.set_page_config(
    page_title="Translation App",
    page_icon="🌐",
    layout="centered"
)

st.title("🔤 Translation App")

languages = ["English", "Urdu", "Spanish", "French", "German", "Chinese", "Japanese"]

template = """
Translate this text from {input_language} into {output_language},\
using simple and make sure to write only translation:
{text}
"""

input_language = st.sidebar.selectbox("Select input language", languages)
output_language = st.sidebar.selectbox("Select output language", languages)

with st.form(key='translation_form'):
    text_to_translate = st.text_area("Enter the text you want to translate", height=150)
    submit_button = st.form_submit_button("Translate")

    if submit_button:
        if text_to_translate:
            prompt_template = ChatPromptTemplate.from_template(template)
            prompt = prompt_template.format_messages(
                input_language=input_language,
                output_language=output_language,
                text=text_to_translate
            )
            response = llm(prompt)
            st.markdown(f"## Translation:\n{response.content.strip()}")
        else:
            st.warning("Please enter some text to translate.")
+
st.markdown("---")
st.write("Powered by next.ai")
