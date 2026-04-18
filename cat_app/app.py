import streamlit as st

st.set_page_config(
    page_title="Cat Central",
    page_icon="🐱",
    layout="wide"
)

# Navigation pages
blog_page = st.Page("pages/1_🐱_Blog.py", title="Cat Blog", icon="🐱")
chat_page = st.Page("pages/2_💬_Cat_Chat.py", title="Meow Chat", icon="💬")
data_page = st.Page("pages/3_📊_Cat_Data.py", title="Cat Stats", icon="📊")
quiz_page = st.Page("pages/4_✏️_Cat_Quiz.py", title="Cat Quiz", icon="✏️")

pg = st.navigation([blog_page, chat_page, data_page, quiz_page])
pg.run()

# Sidebar content (shared across pages)
with st.sidebar:
    st.image("https://cataas.com/cat", caption="Random Cat of the Moment", width=250)
    st.markdown("---")
    st.markdown("### 🐾 Cat Central")
    st.caption("Everything feline, beautifully interactive.")