import streamlit as st

# Header
col1, col2 = st.columns(2, gap = "small", vertical_alignment = "center")
with col1:
    st.image("./assets/developer.png", width = 250)
with col2:
    # Use st.markdown to reduce the font size of the title
    st.markdown("<h5 style='font-size: 32px; color: white;'>Rutton Chandra Sarker</h5>", unsafe_allow_html=True)
    st.write("🚀 Data Science Enthusiast")
    st.write("🪶 Consistency & Discipline is the key to success!")
    st.write("📧 Email: sarker.rutton@gmail.com")
    github_link = "https://github.com/RuttonSarker"
    hackerrank_link = "https://www.hackerrank.com/profile/RuttonSarker"
    st.markdown(f"👨🏻‍💻 Profile: 🌐 [GitHub]({github_link}) | 💻 [HackerRank]({hackerrank_link})")

# Experience & Qualifications
st.write("\n")
st.subheader("🏫 Education")
st.write(
    """
    - 🎓 M.Sc. in Computational Science (Present) | Laurentian University, Canada 🇨🇦 
    - 🎓 B.Sc. in Computer Science & Engineering | North South University, Bangladesh 🇧🇩
    """
   )

# Field of Interest
st.write("\n")
st.subheader("📌 Field of Interest")
st.write(
    """
    - Artificial Intelligence (AI)
    - Machine Learning/Deep Learning (ML/DL)
    - Natural Language Processing (NLP)
    - Large Language Models (LLM)
    """
   )

# Technical Skills
st.write("\n")
st.subheader("🎯 Technical Skills")
st.write(
    """
    - Programming Languages: C++, Java, Python, R
    - Database Management: MySQL, MongoDB
    - Machine Learning Libraries: Scikit-learn, TensorFlow, Keras, PyTorch
    - Data Analysis & Visualization: Pandas, NumPy, Matplotlib, Seaborn
    - LLM Frameworks: Langchain, Hugging Face Transformers
    - Web Scraping: BeautifulSoup, Selenium
    - Visualization Tools: Tableau, Power BI
    - Virtualization: Docker
    - Version Control: Git, GitHub
    
    """
   )
