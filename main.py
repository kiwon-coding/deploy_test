import streamlit as st
import openai

if __name__ == "__main__":
    st.write("hello")
    st.write("hi")

    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", "content": "Hello"}]
    )

    st.write(response)
