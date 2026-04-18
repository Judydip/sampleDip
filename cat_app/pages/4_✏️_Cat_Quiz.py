import streamlit as st
import random
import time

st.title("✏️ Are You a True Cat Expert?")

# Quiz questions
questions = [
    {
        "question": "How many hours does the average cat sleep per day?",
        "options": ["8-10 hours", "12-16 hours", "16-20 hours", "20-24 hours"],
        "correct": 1,
        "explanation": "Cats sleep 12-16 hours daily to conserve energy for hunting."
    },
    {
        "question": "What does it mean when a cat slowly blinks at you?",
        "options": ["They're tired", "They're showing trust/affection", "They're about to attack", "They have dry eyes"],
        "correct": 1,
        "explanation": "The slow blink is a 'cat kiss' - a sign of trust and contentment."
    },
    {
        "question": "What is a group of cats called?",
        "options": ["A pride", "A clowder", "A pack", "A colony"],
        "correct": 1,
        "explanation": "A group of cats is called a clowder or a glaring!"
    },
    {
        "question": "Which cat breed is hairless?",
        "options": ["Siamese", "Sphynx", "Maine Coon", "Ragdoll"],
        "correct": 1,
        "explanation": "The Sphynx is known for its hairless appearance (though it actually has fine fuzz)."
    },
    {
        "question": "How many bones do cats have?",
        "options": ["206", "230", "244", "180"],
        "correct": 1,
        "explanation": "Cats have about 230 bones, compared to 206 in humans. More flexibility!"
    }
]

# Initialize session state
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
    st.session_state.current_q = 0
    st.session_state.score = 0
    st.session_state.answers = []
    st.session_state.show_results = False

# Start quiz
if not st.session_state.quiz_started:
    st.markdown("""
    ### Think you know cats? 🐱
    
    Test your feline knowledge with this 5-question quiz!
    """)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🐾 Start Quiz", use_container_width=True, type="primary"):
            st.session_state.quiz_started = True
            st.session_state.current_q = 0
            st.session_state.score = 0
            st.session_state.answers = []
            st.session_state.show_results = False
            st.rerun()

# Quiz in progress
elif not st.session_state.show_results:
    q_num = st.session_state.current_q
    
    if q_num < len(questions):
        # Progress bar
        st.progress(q_num / len(questions), text=f"Question {q_num + 1} of {len(questions)}")
        
        q_data = questions[q_num]
        st.subheader(f"Q{q_num + 1}: {q_data['question']}")
        
        # Radio buttons for options
        answer = st.radio(
            "Select your answer:",
            options=range(len(q_data['options'])),
            format_func=lambda x: q_data['options'][x],
            key=f"q_{q_num}",
            index=None
        )
        
        col1, col2 = st.columns([1, 4])
        with col1:
            if st.button("Submit Answer", type="primary"):
                if answer is not None:
                    is_correct = (answer == q_data['correct'])
                    if is_correct:
                        st.session_state.score += 1
                    
                    st.session_state.answers.append({
                        "question": q_data['question'],
                        "user_answer": q_data['options'][answer],
                        "correct_answer": q_data['options'][q_data['correct']],
                        "is_correct": is_correct,
                        "explanation": q_data['explanation']
                    })
                    
                    st.session_state.current_q += 1
                    
                    if st.session_state.current_q >= len(questions):
                        st.session_state.show_results = True
                    
                    st.rerun()
                else:
                    st.warning("Please select an answer!")
        
        # Show explanation if answer was just submitted (on next render)
        if len(st.session_state.answers) > q_num:
            last_answer = st.session_state.answers[q_num]
            if last_answer['is_correct']:
                st.success(f"✅ Correct! {last_answer['explanation']}")
            else:
                st.error(f"❌ Not quite. The correct answer was: {last_answer['correct_answer']}")
                st.info(f"💡 {last_answer['explanation']}")

# Results page
else:
    st.balloons()
    st.header("🏆 Quiz Results")
    
    # Score display
    score_percent = (st.session_state.score / len(questions)) * 100
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.metric("Your Score", f"{st.session_state.score}/{len(questions)}", 
                 delta=f"{score_percent:.0f}%")
        
        if score_percent == 100:
            st.success("🎉 Purr-fect score! You're a true Cat Master!")
            st.image("https://cataas.com/cat/cute", width=300)
        elif score_percent >= 60:
            st.info("😺 Good job! You know your cats well.")
        else:
            st.warning("😿 Room for improvement. Study more cat facts!")
    
    # Review answers
    st.subheader("📋 Answer Review")
    for i, ans in enumerate(st.session_state.answers):
        with st.expander(f"Q{i+1}: {ans['question']}", expanded=False):
            st.write(f"**Your answer:** {ans['user_answer']}")
            st.write(f"**Correct answer:** {ans['correct_answer']}")
            st.write(f"**Explanation:** {ans['explanation']}")
            if ans['is_correct']:
                st.success("✅ Correct")
            else:
                st.error("❌ Incorrect")
    
    # Play again button
    if st.button("🔄 Play Again", use_container_width=True):
        st.session_state.quiz_started = False
        st.rerun()