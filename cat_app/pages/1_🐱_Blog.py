import streamlit as st
import time

st.title("🐱 The Purr-spective")
st.caption("An interactive blog about our feline overlords")

# Like/dislike functionality with session state
if "likes" not in st.session_state:
    st.session_state.likes = {"post1": 0, "post2": 0, "post3": 0}

# Blog Post 1 - with expandable content
col1, col2 = st.columns([3, 1])
with col1:
    st.header("Why Cats Sleep 16 Hours a Day")
with col2:
    if st.button("❤️ Like", key="like1"):
        st.session_state.likes["post1"] += 1
        st.balloons()
    st.metric("Likes", st.session_state.likes["post1"])

with st.expander("Read more..."):
    st.markdown("""
    Cats are crepuscular predators, meaning they hunt at dawn and dusk.
    The rest of the time? Energy conservation mode.
    """)
    # Interactive slider for "cat napping hours"
    nap_hours = st.slider("How many hours did YOUR cat nap today?", 0, 24, 16)
    if nap_hours > 20:
        st.success("Professional napper detected! 🏆")
    st.progress(nap_hours / 24, text=f"{nap_hours}/24 hours")

# Blog Post 2 - with image upload and comments
st.header("The Science of the Slow Blink")
uploaded_photo = st.file_uploader("Share a photo of your cat slow-blinking", type=['png', 'jpg', 'jpeg'])
if uploaded_photo:
    st.image(uploaded_photo, width=300)
    st.caption("Aww! That's a happy cat.")

# Comments section
with st.container(border=True):
    st.subheader("💭 Comments")
    name = st.text_input("Your name", key="comment_name")
    comment = st.text_area("Your thoughts on slow blinking", key="comment_text")
    if st.button("Post Comment"):
        if name and comment:
            st.toast(f"Thanks {name}! Your purr-spective matters. 🐱")