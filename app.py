import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(
    page_title="Ramón Sieira - AI Specialist",
    page_icon="🤖",
    layout="wide"
)
# ---- FOTO DE PERFIL ----
image = Image.open("foto_perfil.png")
st.image(image, width=200, caption="", use_column_width=False)

# ---- HEADER ----
st.markdown("<h1 style='text-align: center;'>Hi 👋, I'm Ramón Sieira</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>AI Specialist & Machine Learning Engineer from Spain 🇪🇸</h3>",
            unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center;'>Passionate about Artificial Intelligence, Data Science, and building impactful, real-world solutions.</p>",
    unsafe_allow_html=True)
st.markdown("---")

st.markdown(
    "<p style='text-align: center;'>Passionate about Artificial Intelligence, Data Science, and building impactful, real-world solutions.</p>",
    unsafe_allow_html=True)
st.markdown("---")
# ---- ABOUT ME ----
st.header("🚀 About Me")
st.markdown("""
- 🤖 **AI Specialist at [SDG Group Spain](https://www.sdggroup.com/en/)**
- 🧠 Strong background in **Machine Learning, Deep Learning & Advanced Analytics**
- ☁️ Experienced with **Azure, Databricks & scalable ML solutions**
- 🏆 Award-winning data scientist in hackathons and Kaggle competitions
- 🌱 Constantly learning and pushing the boundaries of AI
""")

# ---- PROFESSIONAL EXPERIENCE ----
st.header("💼 Professional Experience")
st.markdown("""
**SDG Group Spain** (Logroño, La Rioja, Spain)  
*4+ years*

- **AI Specialist** (Oct 2025 – Present)  
- **Senior Consultant** (Apr 2024 – Present)  
- **Consultant AI Engineer** (Oct 2022 – Apr 2024)  
- **Analyst** (Jul 2021 – Oct 2022)

Working on end-to-end AI solutions, from data engineering and modeling to deployment, delivering value across multiple industries.
""")

# ---- EDUCATION ----
st.header("🎓 Education")
st.markdown("""
🎓 **BSc in Computer Engineering – Knowledge Management**  
**University of La Rioja** (2016 – 2021)
""")

# ---- CERTIFICATIONS ----
st.header("🏅 Certifications")

st.subheader("🧠 Machine Learning & AI")
st.markdown("""
- **Databricks Certified Machine Learning Professional**  _(Databricks)_
- **Professional Machine Learning Engineer**  _(Google Cloud)_
- **Machine Learning Specialization**  _(Coursera)_
- **Machine Learning with Python**  _(Coursera)_
""")

st.subheader("☁️ Microsoft Azure Certifications")
st.markdown("""
- **Microsoft Certified: Azure AI Engineer Associate**  _(Microsoft)_
- **Microsoft Certified: Azure Data Scientist Associate**  _(Microsoft)_
- **Microsoft Certified: Azure AI Fundamentals**  _(Microsoft)_
- **Microsoft Certified: Azure Data Fundamentals**  _(Microsoft)_
- **Microsoft Certified: Azure Fundamentals**  _(Microsoft)_
""")

# ---- AWARDS ----
st.header("🏆 Awards & Achievements")
st.markdown("""
- 🥇 **1st Prize – Marine Datathon**
- 🥇 **1st Prize – IMMUNE**: Credit Card Churn Prediction
- 🥈 **2nd Prize – Schneider Electric European Data Science Hackathon**
- 🥉 **Bronze Medal – Kaggle**: Novozymes Enzyme Stability Prediction Competition
""")

# ---- LANGUAGES & TOOLS ----
st.header("🛠️ Languages & Tools")

tools = [
    ("Python", "https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg"),
    ("Pandas", "https://raw.githubusercontent.com/devicons/devicon/master/icons/pandas/pandas-original.svg"),
    ("PySpark", "https://raw.githubusercontent.com/devicons/devicon/master/icons/apache/apache-original.svg"),
    ("Scikit-learn", "https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg"),
    ("PyTorch", "https://www.vectorlogo.zone/logos/pytorch/pytorch-icon.svg"),
    ("TensorFlow", "https://www.vectorlogo.zone/logos/tensorflow/tensorflow-icon.svg"),
    ("Azure", "https://raw.githubusercontent.com/devicons/devicon/master/icons/azure/azure-original.svg"),
]

cols = st.columns(len(tools))
for col, (name, url) in zip(cols, tools):
    col.markdown(f'<a href="#" target="_blank"><img src="{url}" width="50" height="50"></a>', unsafe_allow_html=True)

# ---- CONNECT ----
st.header("🤝 Connect with Me")
st.markdown("""
<a href="https://www.linkedin.com/in/rasieira" target="_blank">
  <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg"
       alt="LinkedIn" width="50" height="50"/>
</a>
""", unsafe_allow_html=True)

# ---- FOOTER ----
st.markdown(
    "<p style='text-align: center; font-style: italic;'>💡 \"Turning data into intelligent, scalable solutions.\"</p>",
    unsafe_allow_html=True)
