import streamlit as st
import random
import time

st.title("💬 MeowGPT - Cat Wisdom Chat")

# Cat personality responses
cat_responses = {
    "food": [
        "The bowl is half empty. I can see the bottom. This is unacceptable.",
        "Treats now. Questions later. Preferably never.",
        "I don't care that I just ate. That was 5 minutes ago. Feed me."
    ],
    "sleep": [
        "Your keyboard is warm. It is now my bed.",
        "I've selected the most inconvenient spot to nap. You're welcome.",
        "15 hours today. Rookie numbers."
    ],
    "affection": [
        "I will allow pets. Three exactly. Four and I bite.",
        "I'm ignoring you. This is how I show love.",
        "*slow blink* You're acceptable. For now."
    ],
    "play": [
        "That red dot? I know it's you. I still must destroy it.",
        "3 AM zoomies are non-negotiable.",
        "I've knocked something off the counter. Come see what."
    ]
}

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Meow. I am the cat wisdom dispenser. What do you seek, human?"}
    ]

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar="🐱" if message["role"] == "assistant" else "👤"):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask the cat anything..."):
    # Display user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)
    
    # Generate cat response
    with st.chat_message("assistant", avatar="🐱"):
        message_placeholder = st.empty()
        
        # Select response based on keywords
        prompt_lower = prompt.lower()
        if any(word in prompt_lower for word in ["food", "hungry", "treat", "eat"]):
            response = random.choice(cat_responses["food"])
        elif any(word in prompt_lower for word in ["sleep", "nap", "tired"]):
            response = random.choice(cat_responses["sleep"])
        elif any(word in prompt_lower for word in ["pet", "love", "cuddle", "affection"]):
            response = random.choice(cat_responses["affection"])
        elif any(word in prompt_lower for word in ["play", "toy", "laser", "zoom"]):
            response = random.choice(cat_responses["play"])
        else:
            response = "Mrrrrow? *stares at you blankly* Try asking about food, sleep, pets, or play."
        
        # Simulate typing
        full_response = ""
        for chunk in response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})

# Clear chat button
if st.button("🧹 Clear Chat History"):
    st.session_state.messages = [
        {"role": "assistant", "content": "Meow. I am the cat wisdom dispenser. What do you seek, human?"}
    ]
    st.rerun()