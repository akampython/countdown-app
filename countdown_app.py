import streamlit as st
from datetime import datetime
import time

# Set Streamlit page settings
st.set_page_config(
    page_title="كاتی ئاهەنگ گێڕان",
    layout="centered"
)

# 🌙 Styling: Dark background + red text
st.markdown("""
    <style>
        body {
            background-color: #0e1117;
        }
        .countdown {
            font-size: 48px;
            font-weight: bold;
            color: #FF4B4B;
            text-align: center;
        }
        h1 {
            color: #FF4B4B;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# 🕓 Target datetime: 11 June 2025 at 11:00 PM
target_time = datetime(2025, 6, 11, 23, 0, 0)

# 🕒 Create a placeholder to hold the countdown text
countdown_placeholder = st.empty()

# Display the title
st.markdown("<h1>🖕👹⏳ كاتی ماوە بۆ ئاهەنگ گێڕان</h1>", unsafe_allow_html=True)

# 🕓 Countdown Logic
while True:
    now = datetime.now()
    if now >= target_time:
        countdown_placeholder.markdown("<div class='countdown'>🎉 Time has arrived! 🎉</div>", unsafe_allow_html=True)
    else:
        remaining = target_time - now
        days = remaining.days
        hours, remainder = divmod(remaining.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        countdown_str = f"{days}d {hours}h {minutes}m {seconds}s"
        countdown_placeholder.markdown(f"<div class='countdown'>{countdown_str}</div>", unsafe_allow_html=True)

    # Wait for 1 second before updating again
    time.sleep(1)
