import streamlit as st

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# Page layout
about_dev = st.Page(
    page = "views/about_dev.py",
    title = "About Developer",
    icon = ":material/account_circle:",
    default = True,
)

medical_chatbot = st.Page(
    page = "views/medical_chatbot.py",
    title = "Medical Chatbot",
    icon = ":material/chat_bubble:",
    default = False,
)

# Navigation Setup [without sections]
# pg = st.navigation(pages=[about_page, medical_chatbot_page])

# Navigation Setup [without sections]
pg = st.navigation(
    {
        "Info": [about_dev],
        "Chatbot": [medical_chatbot],
    }
)

# Add logo
st.logo("assets/chatbot.png") 


# Display text in bold and color in the sidebar
st.sidebar.markdown("<h4 style='color: #00A2E8; font-weight: bold;'>֎ MedAssist 2.0</h4>", unsafe_allow_html=True)

# Run Navigation
pg.run()