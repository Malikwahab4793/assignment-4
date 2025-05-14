
import time
import streamlit as st
from datetime import datetime

# Initialize session state
if "running" not in st.session_state:
    st.session_state.running = False
if "remaining_time" not in st.session_state:
    st.session_state.remaining_time = 10
if "timer_started" not in st.session_state:
    st.session_state.timer_started = False
if "original_time" not in st.session_state:
    st.session_state.original_time = 10

# Set page config
st.set_page_config(page_title="Countdown Timer", page_icon="✨", layout="wide")

# Left column: Clock display
left_col, right_col = st.columns([1, 2])

with left_col:
    st.markdown("## 🕒 Current Time")
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        st.markdown(
            f"""
            <div style="font-size:36px; font-weight:bold; color:#00BFFF; text-align:center;">
                {current_time}
            </div>
            """, unsafe_allow_html=True)
        time.sleep(1)
        break  # One-time update to avoid infinite loop

# Countdown Function
def countdown():
    st.session_state.running = True
    st.session_state.timer_started = True
    placeholder = right_col.empty()
    while st.session_state.remaining_time >= 0 and st.session_state.running:
        mins, secs = divmod(st.session_state.remaining_time, 60)
        placeholder.markdown(f"""
            <div style="text-align: center; font-size: 50px; font-weight: bold; color:#FF5733">
                ⏳ {mins:02}:{secs:02}
            </div>
        """, unsafe_allow_html=True)
        time.sleep(1)
        st.session_state.remaining_time -= 1

    if st.session_state.remaining_time < 0:
        placeholder.success("✌✔ Time's up! The countdown has finished.")
    elif not st.session_state.running:
        placeholder.warning("🤚🛑 Timer stopped! Click 'Start' to resume.")

# UI in right column
with right_col:
    st.markdown("<h1 style='text-align: center; color: #FF5733;'>⏱️ Countdown Timer</h1>", unsafe_allow_html=True)

    if not st.session_state.running and not st.session_state.timer_started:
        st.session_state.original_time = st.number_input("⏲️ Set timer (in seconds):", min_value=1, max_value=3600, value=10, step=1)
        st.session_state.remaining_time = st.session_state.original_time

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Start 🚀"):
            countdown()
    with col2:
        if st.button("Stop ⛔"):
            st.session_state.running = False
    with col3:
        if st.button("Restart 🔁"):
            st.session_state.remaining_time = st.session_state.original_time
            st.session_state.running = True
            countdown()

    if st.session_state.timer_started and not st.session_state.running and st.session_state.remaining_time > 0:
        st.info("⏸ Timer is paused. Click 'Start' to resume.")
