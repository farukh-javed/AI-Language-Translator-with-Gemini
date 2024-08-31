# 🌐 Translation App

A simple and powerful translation app that uses Google Generative AI (Gemini-1.5-pro) and LangChain to translate text between multiple languages.

## 🚀 Features

- **Language Selection:** Choose from languages like English, Urdu, Spanish, French, German, Chinese, and Japanese.
- **AI-Powered Translations:** Get accurate and context-aware translations powered by Google's Gemini AI.
- **User-Friendly Interface:** Easy-to-use Streamlit interface with options to select input and output languages.

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/farukh-javed/Translation-App.git
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your environment variables by creating a `.env` file and adding your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

## 🖥️ Usage

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Open the app in your browser, select your languages, and start translating!

## 📄 Code Overview

- `app.py`: The main application file that sets up the Streamlit interface and integrates with Google Generative AI using LangChain.

## 🤖 Powered By

- **LangChain**
- **Google Generative AI (Gemini-1.5-pro)**
- **Streamlit**

## 📝 License

This project is licensed under the MIT License.
