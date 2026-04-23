import streamlit as st

st.set_page_config(page_title="My Projects", page_icon="📂", layout="centered")

st.title("📂 My Projects")
st.caption("Simple portfolio of my projects")

# ----------------------------
# PROJECT LIST
# ----------------------------
projects = {
    "Student Management System": "Manages student records and information.",
    "Simple Calculator": "Performs basic math operations.",
    "Portfolio Website": "Shows my skills and projects online."
}

st.subheader("Projects")

selected_project = st.selectbox("Choose a project:", list(projects.keys()))

st.write("### Description")
st.write(projects[selected_project])

# ----------------------------
# LIKE BUTTON
# ----------------------------
st.subheader("❤️ Like This Page")

if "likes" not in st.session_state:
    st.session_state.likes = 0

if st.button("Like 👍"):
    st.session_state.likes += 1

st.write("Total Likes:", st.session_state.likes)
