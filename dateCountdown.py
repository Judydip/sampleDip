import streamlit as st
from datetime import datetime
import json
import os
import random

st.set_page_config(page_title="Event Countdown", page_icon="🎉")

# ============================================
# FILE SAVING FUNCTIONS
# ============================================

DATA_FILE = "countdown_data.json"

def load_data():
    """Load saved data from JSON file. Returns default if file doesn't exist."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                return data
        except (json.JSONDecodeError, IOError):
            return get_default_data()
    else:
        return get_default_data()

def get_default_data():
    """Return default values when no saved data exists."""
    return {
        "event_name": "Special Event",
        "event_date": "2025-12-25",
        "note": "",
        "image_url": ""
    }

def save_data(event_name, event_date, note, image_url):
    """Save all data to JSON file."""
    data = {
        "event_name": event_name,
        "event_date": str(event_date),
        "note": note,
        "image_url": image_url
    }
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# ============================================
# LOAD SAVED DATA ON STARTUP
# ============================================

saved = load_data()

# ============================================
# SESSION STATE FOR EDIT MODE
# ============================================

if "edit_mode" not in st.session_state:
    st.session_state.edit_mode = False

# ============================================
# VIEW MODE (DEFAULT - SHOWS COUNTDOWN IMMEDIATELY)
# ============================================

def show_countdown():
    """Display the saved countdown prominently."""
    
    # FIXED: Convert to date() so both are the same type
    event_date = datetime.fromisoformat(saved["event_date"]).date()
    today = datetime.now().date()
    days_left = (event_date - today).days
    
    # Header with event name
    st.markdown(f"# 🎯 {saved['event_name']}")
    
    # Show the image/GIF if saved
    if saved.get("image_url"):
        st.image(saved["image_url"], use_container_width=True)
    
    # Big countdown display
    st.markdown("---")
    
    if days_left > 0:
        st.markdown(f"<h1 style='text-align: center; font-size: 72px;'>{days_left}</h1>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center;'>days left</h3>", unsafe_allow_html=True)
        
        weeks = days_left // 7
        remainder = days_left % 7
        if weeks > 0:
            st.caption(f"⏰ That's {weeks} week(s) and {remainder} day(s)!")
        
        st.balloons()
        
    elif days_left == 0:
        st.markdown(f"<h1 style='text-align: center; font-size: 72px;'>🎉 TODAY! 🎉</h1>", unsafe_allow_html=True)
        st.snow()
        
    else:
        days_ago = abs(days_left)
        st.markdown(f"<h1 style='text-align: center; font-size: 72px;'>{days_ago} days ago</h1>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    if saved.get("note"):
        st.info(f"📌 {saved['note']}")
    
    messages = [
        "🎯 You've got this!",
        "⭐ Every day brings you closer!"
    ]
    st.caption(random.choice(messages))
    
    if st.button("✏️ Edit Event", type="secondary", use_container_width=True):
        st.session_state.edit_mode = True
        st.rerun()

# ============================================
# EDIT MODE
# ============================================

def show_edit_form():
    """Show the edit form to change event details."""
    
    global saved
    
    st.markdown("## ✏️ Edit Your Event")
    st.caption("Change the details below and click Save")
    
    # Convert saved date string back to date object
    current_date = datetime.fromisoformat(saved["event_date"]).date()  # FIXED: added .date()
    
    # Input fields pre-filled with saved data
    new_event_name = st.text_input("Event name:", value=saved["event_name"])
    new_event_date = st.date_input("Event date:", value=current_date, min_value=datetime.today().date())  # FIXED: added .date()
    new_note = st.text_area("Note/reminder:", value=saved.get("note", ""))
    new_image_url = st.text_input(
        "Image or GIF URL:", 
        value=saved.get("image_url", ""),
        placeholder="https://media.giphy.com/..."
    )
    
    # Preview the image if URL provided
    if new_image_url:
        st.markdown("**Preview:**")
        st.image(new_image_url, width=200)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("💾 Save Changes", type="primary", use_container_width=True):
            save_data(new_event_name, new_event_date, new_note, new_image_url)
            saved = load_data()
            st.session_state.edit_mode = False
            st.rerun()
    
    with col2:
        if st.button("❌ Cancel", use_container_width=True):
            st.session_state.edit_mode = False
            st.rerun()

# ============================================
# MAIN: CHOOSE VIEW OR EDIT MODE
# ============================================

if st.session_state.edit_mode:
    show_edit_form()
else:
    show_countdown()

# ============================================
# SIDEBAR WITH INFO
# ============================================

with st.sidebar:
    st.markdown("## 📅 Current Event")
    st.markdown(f"**{saved['event_name']}**")
    st.markdown(f"**Date:** {saved['event_date']}")
    
    st.divider()
    st.markdown("### How to use")
    st.markdown("""
    1. Click **Edit Event** to change anything
    2. Add a picture URL (GIPHY works great)
    3. Click **Save Changes**
    4. Your event + picture will show immediately
    
    **Picture tips:**
    - Find GIFs on GIPHY.com
    - Right-click → Copy image address
    - Paste into the URL field
    """)