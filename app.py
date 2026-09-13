import os
import streamlit as st
from google import genai

# Page Configuration
st.set_page_config(page_title="AI Vision & Text Analyzer", page_icon="⚡")

st.title("⚡ Hackathon Level 1: AI Analyzer")
st.write("Upload an image or type a text prompt to test the Google Gemini API!")

# Fetch API Key from Streamlit Secrets or Environment
api_key = os.environ.get("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY")

if not api_key:
    api_key = st.text_input("Enter your Gemini API Key:", type="password")

if api_key:
    client = genai.Client(api_key=api_key)
    
    user_prompt = st.text_area("Enter your prompt:", "Explain how AI agents work in simple terms.")
    
    if st.button("Run Analysis", type="primary"):
        with st.spinner("Analyzing with Gemini..."):
            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=user_prompt,
                )
                st.success("Done!")
                st.markdown("### Result:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
else:
    st.warning("Please enter your API Key above to continue.")