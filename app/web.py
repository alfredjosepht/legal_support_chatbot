import sys
import os

# ---------------------------------------
# Fix Python path for Streamlit
# ---------------------------------------
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import streamlit as st

from utils.auth_db import init_db, register_user, authenticate_user
from nlp.classifier import classify_text
from nlp.entity_extractor import extract_entities
from rules.rule_engine import apply_rules
from response.generator import generate_response


# ---------------------------------------
# INITIAL SETUP
# ---------------------------------------
init_db()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = None


# ---------------------------------------
# AUTH UI
# ---------------------------------------
def login_page():
    st.title("🔐 Student Legal Support System")

    tab1, tab2 = st.tabs(["Login", "Register"])

    with tab1:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if authenticate_user(username, password):
                st.session_state.logged_in = True
                st.session_state.username = username
                st.success("Login successful")
                st.rerun()
            else:
                st.error("Invalid username or password")

    with tab2:
        new_user = st.text_input("New Username")
        new_pass = st.text_input("New Password", type="password")

        if st.button("Register"):
            if register_user(new_user, new_pass):
                st.success("Registration successful. Please login.")
            else:
                st.error("Username already exists")


# ---------------------------------------
# CHATBOT UI
# ---------------------------------------
def chatbot_page():
    st.title("⚖️ Student Legal Support Chatbot")
    st.write(f"Logged in as **{st.session_state.username}**")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = None
        st.rerun()

    st.divider()

    user_input = st.text_area(
        "Describe your issue:",
        placeholder="Example: my friends teased me about my caste",
        height=120
    )

    if st.button("Analyze Issue"):
        if not user_input.strip():
            st.warning("Please describe your issue.")
            return

        domain, confidence = classify_text(user_input)
        entities = extract_entities(user_input)
        contexts = apply_rules(domain, entities)
        response = generate_response(contexts, confidence)

        st.divider()
        st.subheader("Result")
        st.markdown(response)


# ---------------------------------------
# MAIN
# ---------------------------------------
def main():
    if not st.session_state.logged_in:
        login_page()
    else:
        chatbot_page()


if __name__ == "__main__":
    main()
