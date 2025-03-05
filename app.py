import random
import string
import streamlit as st

# Function to generate a password
def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    if length < 8:
        return "❌ Password must be at least 8 characters long!"
    
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "❌ Please select at least one character type!"
    
    return ''.join(random.choice(characters) for _ in range(length))

# Streamlit UI
st.set_page_config(page_title="Password Generator", page_icon="🔐", layout="centered")

st.title("🔐 Secure Password Generator")

# Sidebar for settings
st.sidebar.header("Customize Your Password")
num_passwords = st.sidebar.number_input("Number of Passwords", min_value=1, max_value=10, value=1, step=1)
length = st.sidebar.slider("Password Length", min_value=8, max_value=50, value=12, step=1)

use_upper = st.sidebar.checkbox("Include Uppercase Letters", value=True)
use_lower = st.sidebar.checkbox("Include Lowercase Letters", value=True)
use_digits = st.sidebar.checkbox("Include Numbers", value=True)
use_symbols = st.sidebar.checkbox("Include Symbols", value=True)

# Generate passwords
if st.sidebar.button("Generate Passwords"):
    st.subheader("🔑 Generated Passwords:")
    passwords = [generate_password(length, use_upper, use_lower, use_digits, use_symbols) for _ in range(num_passwords)]

    for password in passwords:
        st.code(password)
        
        # Add a copy button using Streamlit's clipboard-friendly text input
        st.text_input("Copy Password:", password, key=password)

# Footer
st.markdown("---")
st.caption("🔒 Built with ❤️ by Mehak Hamid")
