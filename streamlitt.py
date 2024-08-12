import streamlit as st
import random
import time

# Function to simulate sun position and energy production
def get_sun_position():
    return random.uniform(0, 180)

def get_energy_produced():
    return random.uniform(0, 10)

def get_weather():
    return random.choice(["Sunny", "Cloudy", "Rainy"])

# Streamlit UI
st.title("Single-Axis Solar Tracker")

# Sun Position Display
sun_position = get_sun_position()
st.metric("Sun Position", f"{sun_position:.2f}°")

# Panel Angle Display
panel_angle = st.number_input("Panel Angle", min_value=0.0, max_value=180.0, value=0.0, step=0.1)

# Manual Control
if st.button("Set Angle"):
    st.success(f"Panel angle set to {panel_angle}°")

# Automated Tracking Mode
if st.button("Enable Automated Tracking"):
    st.info("Automated Tracking Enabled")

# Performance Monitoring
energy_produced = get_energy_produced()
st.metric("Energy Produced", f"{energy_produced:.2f} kWh")

# Weather Integration
weather = get_weather()
st.metric("Weather", weather)

# Alerts and Notifications
st.metric("Alerts", "None")

# Update UI periodically
while True:
    sun_position = get_sun_position()
    energy_produced = get_energy_produced()
    weather = get_weather()

    st.metric("Sun Position", f"{sun_position:.2f}°")
    st.metric("Energy Produced", f"{energy_produced:.2f} kWh")
    st.metric("Weather", weather)

    time.sleep(1)




