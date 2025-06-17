import streamlit as st
import os

st.title("🚀 Hello from Streamlit!")
st.write("This is a basic Streamlit app running on the web.")

# Print environment variables
st.header("🌍 Environment Variables")

# Loop through environment variables
for key, value in os.environ.items():
    st.text(f"{key} = {value}")      # Display on web
    print(f"{key} = {value}") 

aws_key = os.getenv("AWS_ACCESS_KEY")
print("AWS_ACCESS_KEY:", aws_key)
