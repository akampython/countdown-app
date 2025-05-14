import streamlit as st
from datetime import datetime

# Configure the page
st.set_page_config(page_title="Countdown Timer", layout="centered")

# Inject custom CSS for dark theme and red text
st.markdown("""
    <style>
        .main {
            background-color: #0e1117;
            color: #FF4B4B;
        }
        .countdown {
            font-size: 48px;
            font-weight: bold;
            text-align: center;
            color: #FF4B4B;
        }
        h1 {
            color: #FF4B4B;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1>⏳ Countdown to 11 June 2025 - 11:00 PM</h1>", unsafe_allow_html=True)

# Target time
target_time = datetime(2025, 6, 11, 23, 0, 0)
now = datetime.now()

# Calculate remaining time
if now >= target_time:
    st.markdown("<div class='countdown'>🎉 Time has arrived! 🎉</div>", unsafe_allow_html=True)
else:
    remaining = target_time - now
    days = remaining.days
    hours, rem = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(rem, 60)

    countdown_text = f"{days}d {hours}h {minutes}m {seconds}s"
    st.markdown(f"<div class='countdown'>{countdown_text}</div>", unsafe_allow_html=True)

    # Optional: Auto-refresh every second (experimental)
    st.experimental_autorefresh(interval=1000, limit=10000)
