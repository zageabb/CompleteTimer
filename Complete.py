import streamlit as st
import time
import threading

def countdown_timer(total_seconds, countdown_placeholder):
    for remaining in range(total_seconds, -1, -1):
        mins, secs = divmod(remaining, 60)
        hrs, mins = divmod(mins, 60)
        timer_display = f"{hrs:02}:{mins:02}:{secs:02}"

        # Display countdown timer in large font
        countdown_placeholder.markdown(
            f"<h1 style='text-align: center; font-size: 72px;'>{timer_display}</h1>",
            unsafe_allow_html=True,
        )

        time.sleep(1)

    countdown_placeholder.markdown(
        "<h1 style='text-align: center; font-size: 72px;'>Time's up!</h1>",
        unsafe_allow_html=True,
    )

def count_up_timer(countup_placeholder):
    start_time = time.time()
    while True:
        elapsed = int(time.time() - start_time)
        mins, secs = divmod(elapsed, 60)
        hrs, mins = divmod(mins, 60)
        timer_display = f"{hrs:02}:{mins:02}:{secs:02}"

        # Display count up timer in large font
        countup_placeholder.markdown(
            f"<h1 style='text-align: center; font-size: 72px;'>{timer_display}</h1>",
            unsafe_allow_html=True,
        )

        time.sleep(1)

# Streamlit app setup
st.title("Large Number Timer")

# Timer settings
st.subheader("Timers")
hours = st.number_input("Hours:", min_value=0, value=0, step=1, key="timer_hours")
minutes = st.number_input("Minutes:", min_value=0, max_value=59, value=0, step=1, key="timer_minutes")
seconds = st.number_input("Seconds:", min_value=0, max_value=59, value=0, step=1, key="timer_seconds")

total_seconds = int(hours * 3600 + minutes * 60 + seconds)

if st.button("Start Timers"):
    countdown_placeholder = st.empty()
    countup_placeholder = st.empty()

    # Run countdown and count up timers concurrently
    countdown_thread = threading.Thread(target=countdown_timer, args=(total_seconds, countdown_placeholder))
    countup_thread = threading.Thread(target=count_up_timer, args=(countup_placeholder,))

    countdown_thread.start()
    countup_thread.start()
