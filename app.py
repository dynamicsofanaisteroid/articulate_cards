import streamlit as st
import pandas as pd
import random

# --- Load card data ---
@st.cache_data
def load_data():
    return pd.read_csv("cards (1).csv")

df = load_data()

# --- App UI ---
st.set_page_config(page_title="Articulate Cards", page_icon="🃏", layout="centered")
st.title("🃏 Articulate Card Generator")
st.caption("Generate endless cards for your game!")

# --- Session State Setup ---
if 'category' not in st.session_state:
    st.session_state.category = None
if 'current_card' not in st.session_state:
    st.session_state.current_card = None

# --- Category Selection ---
st.subheader("Choose a Category")
categories = sorted(df['category'].unique())
cols = st.columns(len(categories))
for i, cat in enumerate(categories):
    if cols[i].button(cat):
        st.session_state.category = cat
        st.session_state.current_card = None

# --- Generate Button ---
if st.session_state.category:
    st.markdown(f"**Selected:** `{st.session_state.category}`")
    if st.button("🎲 Generate Card"):
        clues = df[df['category'] == st.session_state.category]['clue'].tolist()
        st.session_state.current_card = random.choice(clues)

# --- Display Card ---
if st.session_state.current_card:
    category_color = {
        "Person": "#FF6B6B",
        "Object": "#4ECDC4",
        "Action": "#45B7D1",
        "World": "#96CEB4",
        "Random": "#FECA57"
    }.get(st.session_state.category, "#f7f7f7")

    st.markdown(
        f'''
        <div style="background-color:{category_color};padding:30px;border-radius:15px;text-align:center">
            <h2 style="color:white;">{st.session_state.current_card}</h2>
            <p style="color:white;font-style:italic;">Category: {st.session_state.category}</p>
        </div>
        ''',
        unsafe_allow_html=True
    )
