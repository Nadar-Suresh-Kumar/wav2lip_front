import streamlit as st
import requests

# Streamlit frontend for user input
st.title("User Information Form")

username = st.text_input("Enter your username:")
phone_number = st.text_input("Enter your phone number:")

if st.button("Submit"):
    if username and phone_number:
        # Sending data to Flask backend
        data = {'username': username, 'phone_number': phone_number}
        response = requests.post("http://localhost:5000/submit", json=data)

        if response.status_code == 200:
            st.success("Data submitted successfully!")
        else:
            st.error("Failed to submit data.")
    else:
        st.error("Please provide both username and phone number.")
