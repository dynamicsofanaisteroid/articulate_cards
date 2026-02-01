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

# --- App Setup ---
st.set_page_config(page_title="Articulate Cards", page_icon="🃏", layout="centered")
st.title("🃏 Articulate Card Generator")
st.caption("Roll a category, draw cards, and track your round!")

# --- Session State Initialization ---
for key in ['category', 'current_card', 'correct_count', 'skip_count', 'in_round']:
    if key not in st.session_state:
        st.session_state[key] = None if key in ['category', 'current_card'] else 0

# --- Roll Category ---
if st.button("🎲 Roll Category"):
    st.session_state.category = random.choice(df['category'].unique())
    st.session_state.current_card = None
    st.session_state.correct_count = 0
    st.session_state.skip_count = 0
    st.session_state.in_round = True

# --- Display Selected Category ---
if st.session_state.category:
    color = category_colors.get(st.session_state.category, "#f7f7f7")
    st.markdown(
        f'''
        <div style="background-color:{color};padding:20px;border-radius:10px;text-align:center;margin-bottom:20px">
            <h3 style="color:white;">Category: {st.session_state.category}</h3>
        </div>
        ''',
        unsafe_allow_html=True
    )

# --- Generate Card Button ---
if st.session_state.category and not st.session_state.current_card:
    if st.button("🎴 Generate Card"):
        clues = df[df['category'] == st.session_state.category]['clue'].tolist()
        st.session_state.current_card = random.choice(clues)

# --- Display Current Card and Action Buttons ---
if st.session_state.current_card:
    color = category_colors.get(st.session_state.category, "#f7f7f7")
    st.markdown(
        f'''
        <div style="background-color:{color};padding:30px;border-radius:15px;text-align:center;margin-bottom:20px">
            <h2 style="color:white;">{st.session_state.current_card}</h2>
        </div>
        ''',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    # --- Skip Button ---
    if col1.button("⏭ Skip"):
        st.session_state.skip_count += 1
        clues = df[df['category'] == st.session_state.category]['clue'].tolist()
        st.session_state.current_card = random.choice(clues)
        st.rerun()

    # --- Correct Button ---
    if col2.button("✅ Correct!"):
        st.session_state.correct_count += 1
        clues = df[df['category'] == st.session_state.category]['clue'].tolist()
        st.session_state.current_card = random.choice(clues)
        st.rerun()

    # --- End Round Button ---
    if col3.button("⏹ End Round"):
        st.markdown("---")
        st.subheader("🧾 Round Summary")
        st.success(f"✅ Correct: {st.session_state.correct_count}")
        st.warning(f"⏭ Skipped: {st.session_state.skip_count}")
        st.session_state.category = None
        st.session_state.current_card = None
        st.session_state.correct_count = 0
        st.session_state.skip_count = 0
        st.session_state.in_round = False
