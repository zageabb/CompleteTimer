import streamlit as st
import time

# Streamlit app setup
st.title("Large Number Timer")

# Create a sidebar for inputs
with st.sidebar:
    st.subheader("Timers")
    hours = st.number_input("Hours:", min_value=0, value=0, step=1, key="timer_hours")
    minutes = st.number_input("Minutes:", min_value=0, max_value=59, value=0, step=1, key="timer_minutes")
    seconds = st.number_input("Seconds:", min_value=0, max_value=59, value=0, step=1, key="timer_seconds")

# Calculate total time in seconds
total_seconds = int(hours * 3600 + minutes * 60 + seconds)

if st.button("Start Timers"):
    countdown_placeholder = st.empty()
    countup_placeholder = st.empty()

    countdown_start = time.time()
    countup_start = time.time()

    while total_seconds >= 0:
        # Countdown timer logic
        elapsed_countdown = int(time.time() - countdown_start)
        remaining_seconds = total_seconds - elapsed_countdown
        if remaining_seconds < 0:
            countdown_display = "Time's up!"
        else:
            mins, secs = divmod(remaining_seconds, 60)
            hrs, mins = divmod(mins, 60)
            countdown_display = f"{hrs:02}:{mins:02}:{secs:02}"

        # Count-up timer logic
        elapsed_countup = int(time.time() - countup_start)
        mins, secs = divmod(elapsed_countup, 60)
        hrs, mins = divmod(mins, 60)
        countup_display = f"{hrs:02}:{mins:02}:{secs:02}"

        # Update the display
        countdown_placeholder.markdown(
            f"<h1 style='text-align: center; font-size: 72px;'>{countdown_display}</h1>",
            unsafe_allow_html=True,
        )

        countup_placeholder.markdown(
            f"<h1 style='text-align: center; font-size: 72px;'>{countup_display}</h1>",
            unsafe_allow_html=True,
        )

        time.sleep(1)

        if remaining_seconds < 0:
            break
