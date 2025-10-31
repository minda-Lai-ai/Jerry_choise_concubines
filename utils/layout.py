import streamlit as st

def render_slot_machine(images):
    st.image(images, width=150)

def render_result_message(message):
    st.markdown(
        f"<marquee style='color:red;font-size:24px'>{message}</marquee>",
        unsafe_allow_html=True
    )