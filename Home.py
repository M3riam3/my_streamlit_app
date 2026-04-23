import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="My Portfolio",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load Image
image = Image.open("assets/pic1.jpeg")

# ---------------- SIDEBAR ----------------
st.sidebar.image(image, width=200)

st.sidebar.title("👩‍💻 Meriam R. Rojas")
st.sidebar.write("🎓 BSCS Student")
st.sidebar.write("💡 Passionate about programming and web development")

st.sidebar.markdown("---")

st.sidebar.subheader("📊 Skill Level")

st.sidebar.progress(90)
st.sidebar.write("Python")

st.sidebar.progress(80)
st.sidebar.write("HTML")

st.sidebar.progress(75)
st.sidebar.write("CSS")

st.sidebar.progress(85)
st.sidebar.write("Streamlit")

st.sidebar.markdown("---")
st.sidebar.success("Thank you for visiting my portfolio!")

# ---------------- HEADER ----------------
st.title("💻 My Portfolio Website")

st.markdown("""
Welcome to my personal portfolio!  
This website showcases my **skills, projects, and interests in programming and technology**.
""")

st.markdown("---")

# ---------------- PROFILE SECTION ----------------
col1, col2 = st.columns([1,2])

with col1:
    st.image(image, caption="Meriam R. Rojas")

with col2:
    st.subheader("👋 Hello!")

    st.write("""
    I am **Meriam R. Rojas**, a student taking **Bachelor of Science in Computer Science**.  
    I enjoy learning new technologies and creating projects that solve real-world problems.

    My interests include:
    - 💻 Software Development  
    - 🌐 Web Development  
    - 📊 Data Visualization  
    """)

    if st.button("👋 Say Hi"):
        st.success("Thank you for visiting my portfolio!")

st.markdown("---")

# ---------------- SKILLS SECTION ----------------
st.subheader("🛠 My Skills")

skill = st.selectbox(
    "Select a skill to learn more:",
    ["Python", "HTML", "CSS", "Streamlit"]
)

if skill == "Python":
    st.info("Python is my main programming language used for building applications and automation.")

elif skill == "HTML":
    st.info("HTML is used for structuring websites and web pages.")

elif skill == "CSS":
    st.info("CSS helps design beautiful and responsive web layouts.")

elif skill == "Streamlit":
    st.info("Streamlit allows me to build interactive data apps using Python.")

st.markdown("---")

# ---------------- PROJECTS SECTION ----------------
st.subheader("📂 My Projects")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("🎓 Student Management System")
    st.write("A system that manages student records and information.")

with col2:
    st.success("🧮 Simple Calculator")
    st.write("A Python program that performs basic mathematical operations.")

with col3:
    st.success("🌐 Portfolio Website")
    st.write("A website that showcases my personal projects and skills.")

st.markdown("---")

# ---------------- METRICS SECTION ----------------
st.subheader("📊 My Learning Progress")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Projects Completed", "3")

with col2:
    st.metric("Skills Learned", "4")

with col3:
    st.metric("Years Studying CS", "1")

st.markdown("---")

# ---------------- FEEDBACK SECTION ----------------
st.subheader("💬 Visitor Feedback")

with st.form("feedback_form"):
    name = st.text_input("Enter your name")
    message = st.text_area("Leave a message")

    submit = st.form_submit_button("Send Feedback")

    if submit:
        st.success(f"Thank you {name}! Your message has been received.")

st.markdown("---")

# ---------------- EXTRA INFO ----------------
with st.expander("📖 More About Me"):
    st.write("""
    I am continuously learning new programming technologies and improving my skills.  
    My goal is to become a **professional software developer** and build systems that help people and organizations.
    """)

st.markdown("---")

st.caption("© 2026 Meriam R. Rojas | Streamlit Portfolio")
