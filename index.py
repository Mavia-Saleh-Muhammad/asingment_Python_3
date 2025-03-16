import re
import random
import string
import streamlit as st

# Page Styling
st.set_page_config(
    page_title="VIP Password Strength Checker",
    page_icon="🔐",
    layout="centered",
)

# Custom CSS for Styling
st.markdown("""
    <style>
        .main { text-align: center; }
        .stTextInput { width: 60% !important; margin: auto; display: block; }
        .stButton button {
            background-color: #4CAF50; color: white; padding: 10px 20px;
            border: none; cursor: pointer; border-radius: 5px;
        }
        .stButton button:hover { background-color: #45a049; }
        .stProgress > div > div > div { background-color: #4CAF50; }
        .stMarkdown { text-align: center; }
    </style>
""", unsafe_allow_html=True)

# Page title and description
st.title("🔐 VIP Password Strength Checker")
st.write("Enter a password to check its strength and get tips to make it stronger. 💪")

# Function: Password Strength Checker
def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Uppercase Letter Check
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one uppercase letter.")

    # Lowercase Letter Check
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one lowercase letter.")

    # Number Check
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one number.")

    # Special Character Check
    if re.search(r'[@$!%*?&]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one special character (@, $, !, %, *, ?, &).")

    # Common Passwords Check
    common_passwords = ["password", "123456", "qwerty", "admin", "letmein"]
    if password.lower() in common_passwords:
        feedback.append("❌ Avoid using common passwords.")

    # Repeated Characters Check
    if re.search(r'(.)\1{2,}', password):
        feedback.append("❌ Avoid using repeated characters.")

    return score, feedback

# Function: Generate a strong password
def generate_strong_password():
    length = 12
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# User input field
password = st.text_input("🔑 Enter your password", type="password")

# Password Strength Meter
if password:
    score, feedback = check_password_strength(password)
    strength_percentage = (score / 7)  # Convert to range [0.0, 1.0]
    st.progress(strength_percentage)

    # Strength Evaluation
    if score == 7:
        st.success("✅ Strong Password! 🔥")
    elif score >= 4:
        st.warning("⚠️ Moderate Password! Try making it stronger.")
    else:
        st.error("❌ Weak Password! Please follow the suggestions below.")

    # Show Feedback
    for suggestion in feedback:
        st.write(suggestion)

# Generate Strong Password
if st.button("🎲 Generate Strong Password"):
    strong_password = generate_strong_password()
    st.text_input("🔑 Generated Strong Password", strong_password, type="password")

# Dark Mode Toggle
dark_mode = st.checkbox("🌙 Dark Mode")
if dark_mode:
    st.markdown(
        """
        <style>
        .main { background-color: #1e1e1e; color: #ffffff; }
        </style>
        """,
        unsafe_allow_html=True,
    )
