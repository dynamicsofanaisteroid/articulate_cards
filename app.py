import streamlit as st
import pandas as pd
import random
import time

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
defaults = {
    'category': None,
    'current_card': None,
    'correct_count': 0,
    'skip_count': 0,
    'round_active': False,
    'start_time': None,
    'end_time': None,
    'used_cards': []
}
for key, val in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = val

# --- Roll Category ---
if st.button("🎲 Roll Category"):
    st.session_state.category = random.choice(df['category'].unique())
    st.session_state.current_card = None
    st.session_state.correct_count = 0
    st.session_state.skip_count = 0
    st.session_state.round_active = False
    st.session_state.start_time = None
    st.session_state.end_time = None
    st.session_state.used_cards = []

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

# --- Generate Card & Start Timer ---
if st.session_state.category and not st.session_state.current_card:
    if st.button("🎴 Generate Card"):
        clues = df[df['category'] == st.session_state.category]['clue'].tolist()
        st.session_state.current_card = random.choice(clues)
        st.session_state.used_cards = [st.session_state.current_card]
        st.session_state.start_time = time.time()
        st.session_state.end_time = st.session_state.start_time + 30
        st.session_state.round_active = True
        st.rerun()

# --- Timer Display and Auto-End Logic ---
if st.session_state.round_active:
    now = time.time()
    remaining = int(st.session_state.end_time - now)
    
    if remaining > 0:
        st.markdown(f"⏳ Time left: **{remaining} seconds**")
        # Auto-refresh every second to keep timer updating
        time.sleep(0.1)
        st.rerun()
    else:
        # Time's up - end the round
        st.markdown("⏱ **Time's up!**")
        st.session_state.round_active = False
        st.session_state.current_card = None
        st.markdown("---")
        st.subheader("🧾 Round Summary")
        st.success(f"✅ Correct: {st.session_state.correct_count}")
        st.warning(f"⏭ Skipped: {st.session_state.skip_count}")
        st.stop()

# --- Show Current Card and Round Buttons ---
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

    if col1.button("⏭ Skip"):
        st.session_state.skip_count += 1
        # Get new card (avoiding recently used ones if possible)
        clues = df[df['category'] == st.session_state.category]['clue'].tolist()
        available_clues = [c for c in clues if c not in st.session_state.used_cards[-5:]]
        if not available_clues:
            available_clues = clues
        st.session_state.current_card = random.choice(available_clues)
        st.session_state.used_cards.append(st.session_state.current_card)
        st.rerun()

    if col2.button("✅ Correct!"):
        st.session_state.correct_count += 1
        # Get new card (avoiding recently used ones if possible)
        clues = df[df['category'] == st.session_state.category]['clue'].tolist()
        available_clues = [c for c in clues if c not in st.session_state.used_cards[-5:]]
        if not available_clues:
            available_clues = clues
        st.session_state.current_card = random.choice(available_clues)
        st.session_state.used_cards.append(st.session_state.current_card)
        st.rerun()

    if col3.button("🛑 End Round"):
        st.session_state.round_active = False
        st.session_state.current_card = None
        st.markdown("---")
        st.subheader("🧾 Round Summary")
        st.success(f"✅ Correct: {st.session_state.correct_count}")
        st.warning(f"⏭ Skipped: {st.session_state.skip_count}")
        elapsed = int(time.time() - st.session_state.start_time)
        st.info(f"⏱ Time used: {elapsed} seconds")
        st.rerun()
