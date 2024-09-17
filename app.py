import streamlit as st
import requests
import re

# Streamlit frontend for user input
st.title("User Information Form")

username = st.text_input("Enter your username:")
email = st.text_input("Enter your Gmail ID:")

# Regular expression for validating an email address
email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

if st.button("Submit"):
    if username and email:
        # Check if the email is valid
        if re.match(email_regex, email):
            # Sending data to Flask backend
            data = {'username': username, 'phone_number': email}
            response = requests.post("http://localhost:5000/submit", json=data)

            if response.status_code == 200:
                st.success("Data submitted successfully!")
            else:
                st.error("Failed to submit data.")
        else:
            st.error("Please enter a valid email address.")
    else:
        st.error("Please provide both username and email.")

