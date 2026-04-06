import streamlit as st
from datetime import datetime
import json
import os
import random

st.set_page_config(page_title="Event Countdown", page_icon="🎉")

DATA_FILE = "countdown_data.json"

def load_data():
    """Load saved countdown data"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {
        "event_name": "Special Event",
        "event_date": "2025-12-25",
        "note": ""
    }

def save_data(event_name, event_date, note):
    """Save countdown data"""
    with open(DATA_FILE, "w") as f:
        json.dump({
            "event_name": event_name,
            "event_date": str(event_date),
            "note": note
        }, f)

# Load saved data
saved = load_data()

st.title("🎈 Event Countdown Calendar")

# Input fields with saved defaults
event_name = st.text_input("📝 What are you counting down to?", 
                           value=saved["event_name"])

event_date = st.date_input("📅 When is it?", 
                           value=datetime.fromisoformat(saved["event_date"]),
                           min_value=datetime.today())

note = st.text_area("💬 Add a note (optional)", 
                    value=saved["note"])

# Image/GIF section (same as before)
st.markdown("### 🖼️ Add some fun")
image_url = st.text_input("Paste a GIF or image URL (optional)",
                          placeholder="https://media.giphy.com/...")

if image_url:
    st.image(image_url, use_container_width=True)

# Save and show button
if st.button("💾 Save & Show Countdown", type="primary"):
    save_data(event_name, event_date, note)
    st.success("✅ Saved! Your countdown will be here next time you visit.")
    
    # Calculate and display
    today = datetime.now().date()
    days_left = (event_date - today).days
    
    if days_left > 0:
        st.markdown(f"## 🎯 {days_left} days left until {event_name}!")
        st.balloons()
    elif days_left == 0:
        st.markdown(f"## 🎉 TODAY IS {event_name.upper()}! 🎉")
        st.snow()
    else:
        st.markdown(f"## 📅 {event_name} was {abs(days_left)} days ago")
    
    if note:
        st.info(f"📌 Note: {note}")
    
    # Random encouragement
    messages = ["Keep going! 🚀", "Almost there! ⭐", "Exciting! 🎪"]
    st.caption(random.choice(messages))