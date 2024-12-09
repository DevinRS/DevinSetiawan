import streamlit as st

def contact_form():
    with st.form("contact_form"):
        st.write("If you have any questions or would like to collaborate, feel free to reach out to me!")
        name = st.text_input("Name", max_chars=50)
        email = st.text_input("Email", max_chars=50)
        message = st.text_area("Message", max_chars=500)
        submit_button = st.form_submit_button(label="Submit")
        if submit_button:
            st.success("Message sent successfully!")