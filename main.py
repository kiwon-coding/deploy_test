import streamlit as st
import openai
import os


if __name__ == "__main__":
    api_key_input = st.text_input("OpenAI API Key", type="password", value=os.getenv("OPENAI_API_KEY"))

    if api_key_input:
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = [{"role": "user", "content": "Hello"}]
        )

        st.write(response)
    else:
        st.warning("WARNING: Enter your OpenAI API key!")