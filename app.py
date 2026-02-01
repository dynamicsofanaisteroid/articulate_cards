import streamlit as st
import pandas as pd
import random

# --- Load card data ---
@st.cache_data
def load_data():
    return pd.read_csv("cards (1).csv")

df = load_data()

# --- Category Colors ---
category_colors = {
    "Person": "#FF6B6B",
    "Object": "#4ECDC4",
    "Action": "#45B7D1",
    "World": "#96CEB4",
    "Random": "#FECA57"
}

# --- App UI ---
st.set_page_config(page_title="Articulate Cards", page_icon="🃏", layout="centered")
st.title("🃏 Articulate Card Generator")
st.caption("Roll a category die and reveal your next card!")

# --- Session State Setup ---
if 'category' not in st.session_state:
    st.session_state.category = None
if 'current_card' not in st.session_state:
    st.session_state.current_card = None

# --- Roll Category ---
if st.button("🎲 Roll Category"):
    st.session_state.category = random.choice(df['category'].unique())
    clues = df[df['category'] == st.session_state.category]['clue'].tolist()
    st.session_state.current_card = random.choice(clues)

# --- Display Card ---
if st.session_state.current_card:
    category = st.session_state.category
    color = category_colors.get(category, "#f7f7f7")
    st.markdown(
        f'''
        <div style="background-color:{color};padding:30px;border-radius:15px;text-align:center">
            <h2 style="color:white;">{st.session_state.current_card}</h2>
            <p style="color:white;font-style:italic;">Category: {category}</p>
        </div>
        ''',
        unsafe_allow_html=True
    )
