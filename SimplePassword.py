#Day 7/50 - AI Python Challenge
#Simple Password : Check if a password meets basic requirements (minimum length).

import streamlit as st
import string

# Page title
st.title("🔐 Password Validator")
st.markdown("Check if your password meets the required security rules:")

# User input
password = st.text_input("Enter your password", type="password")

# Button to validate
if st.button("Check Password"):
    # Check length
    is_long_enough = len(password) >= 14

    # Check for uppercase
    has_uppercase = any(char.isupper() for char in password)

    # Check for special character
    special_characters = string.punctuation
    has_special = any(char in special_characters for char in password)

    # Validation result
    if is_long_enough and has_uppercase and has_special:
        st.success("✅ Password is valid!")
    else:
        st.error("❌ Please enter a valid password.")