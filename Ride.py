import math
import streamlit as st


st.title("ALOHA")
st.text_input("How many people are there in the queue?",key="people")
st.text_input("How long does the ride take in min?",key="duration")
st.text_input("How many people can the ride take per cycle?",key="capacity")


def queue_time():
    people_in_queue = int(st.session_state["people"])
    ride_duration = int(st.session_state["duration"])
    capacity_per_cycle = int(st.session_state["capacity"])
    cycles_needed = math.ceil(people_in_queue/capacity_per_cycle)
    total_time = cycles_needed * ride_duration
    st.text(f"Estimated total wait time for the queue: {total_time}m")



st.button("Calculate",on_click=queue_time)



