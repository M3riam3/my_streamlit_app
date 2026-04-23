import streamlit as st
from PIL import Image

st.title("👩‍💻 About Me")

st.markdown("---")

# Profile Section
col1, col2 = st.columns([1,2])

with col1:
    image = Image.open("assets/pic1.jpeg")
    st.image(image, caption="Meriam R. Rojas")

with col2:
    st.subheader("Hello! 👋")

    st.write("""
    I am **Meriam R. Rojas**, a student currently taking  
    **Bachelor of Science in Computer Science**.

    I am passionate about **programming, web development, and learning new technologies**.  
    My goal is to become a **professional software developer** and create systems that help people and organizations.
    """)

st.markdown("---")

# Skills Section
st.subheader("🛠 My Skills")

skills = {
    "🐍 Python": 90,
    "🌐 HTML": 80,
    "🎨 CSS": 75,
    "⚡ Streamlit": 85
}

for skill, level in skills.items():
    st.write(skill)
    st.progress(level)

st.markdown("---")

# Education Section
st.subheader("🎓 Education")

st.info("""
**Bachelor of Science in Computer Science**  
Currently studying programming, software development, and web technologies.
""")

st.markdown("---")

# Hobbies Section
st.subheader("🎯 My Hobbies & Interests")

hobby = st.radio(
    "What do I enjoy doing?",
    ["💻 Coding", "📚 Reading Tech Blogs", "🎨 Designing Websites"]
)

if hobby == "💻 Coding":
    st.success("I enjoy writing code and building software projects.")

elif hobby == "📚 Reading Tech Blogs":
    st.success("I like learning about new technologies and programming trends.")

elif hobby == "🎨 Designing Websites":
    st.success("I enjoy creating visually appealing web interfaces.")

st.markdown("---")

# Fun Fact
with st.expander("✨ Fun Fact About Me"):
    st.write("""
    I enjoy exploring new programming tools and improving my coding skills every day.
    """)

