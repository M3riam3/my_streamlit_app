import streamlit as st

st.title("📞 Contact Me")

st.write("You can send me a message below.")

with st.form("contact_form"):

    name = st.text_input("Enter your name")
    email = st.text_input("Enter your email")
    message = st.text_area("Message")

    submitted = st.form_submit_button("Send")

    if submitted:
        st.success("Message Sent Successfully!")
        st.write("Name:", name)
        st.write("Email:", email)
        st.write("Message:", message)
