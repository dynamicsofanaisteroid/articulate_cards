import streamlit as st
import random

# --- Game Data ---
game_categories = {
    'Person': {
        'color': '#FF6B6B',
        'clues': [
            'Albert Einstein', 'Oprah Winfrey', 'Leonardo da Vinci', 'Marie Curie',
            'Nelson Mandela', 'Shakespeare', 'Mozart', 'Cleopatra', 'Gandhi'
        ]
    },
    'Object': {
        'color': '#4ECDC4',
        'clues': [
            'Umbrella', 'Toothbrush', 'Coffee Cup', 'Scissors', 'Bicycle', 'Piano'
        ]
    },
    'Action': {
        'color': '#45B7D1',
        'clues': [
            'Dancing', 'Swimming', 'Cooking', 'Singing', 'Painting', 'Jumping'
        ]
    },
    'World': {
        'color': '#96CEB4',
        'clues': [
            'Paris', 'Great Wall of China', 'Amazon Rainforest', 'Mount Everest'
        ]
    },
    'Random': {
        'color': '#FECA57',
        'clues': [
            'Time Travel', 'Magic Trick', 'Treasure Hunt', 'Robot Dance', 'Dinosaur'
        ]
    }
}

# --- App UI ---
st.set_page_config(page_title="Articulate Cards", page_icon="🃏", layout="centered")
st.title("🃏 Articulate Card Generator")
st.caption("Generate endless cards for your game!")

# --- Session State ---
if 'category' not in st.session_state:
    st.session_state.category = None
if 'current_card' not in st.session_state:
    st.session_state.current_card = None

# --- Category Selection ---
st.subheader("Choose a Category")
cols = st.columns(len(game_categories))
for idx, (cat, data) in enumerate(game_categories.items()):
    if cols[idx].button(cat):
        st.session_state.category = cat
        st.session_state.current_card = None

# --- Generate Card Button ---
if st.session_state.category:
    st.markdown(f"**Selected:** `{st.session_state.category}`")
    if st.button("🎲 Generate Card"):
        clue = random.choice(game_categories[st.session_state.category]['clues'])
        st.session_state.current_card = clue

# --- Display Card ---
if st.session_state.current_card:
    color = game_categories[st.session_state.category]['color']
    st.markdown(f"""
    <div style="background-color:{color};padding:30px;border-radius:15px;text-align:center">
        <h2 style="color:white;">{st.session_state.current_card}</h2>
        <p style="color:white;font-style:italic;">Category: {st.session_state.category}</p>
    </div>
    """, unsafe_allow_html=True)