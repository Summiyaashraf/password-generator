import streamlit as st  
import random  
import string  

# Function to generate a random password
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  # Includes uppercase and lowercase letters

    if use_digits:
        characters += string.digits  # Adds numbers (0-9)

    if use_special:
        characters += string.punctuation  # Adds special characters (!@#$%^&*)

    return "".join(random.choice(characters) for _ in range(length))

# Function to check password strength
def check_password_strength(password):
    if len(password) < 8:
        return "🔴 Weak"
    elif len(password) < 12:
        return "🟡 Medium"
    else:
        return "🟢 Strong"

# Streamlit UI setup
st.title("🔐 Password Generator")

# User input for password generation
length = st.slider("Select password length:", min_value=6, max_value=32, value=16)
use_digits = st.checkbox("Include numbers (0-9)")
use_special = st.checkbox("Include special characters (!@#$%^&*)")

# Button to generate password
if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    strength = check_password_strength(password)  # Check strength

    # Display password with copy functionality
    st.text_input("Generated Password:", password, key="password")
    st.write(f"🔍 **Strength:** {strength}")  # Show strength indicator

    st.write("---------------------------")
    st.write("🚀 Built with ❤ by [Summiya](https://github.com/Summiyaashraf)")
