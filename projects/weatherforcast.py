import streamlit as st
import requests

st.title("🌤️ Weather Forecast App")
API_KEY = "7aef300bf92095fb26726790ba511514"

# Store the state of the button
if "weather_requested" not in st.session_state:
    st.session_state.weather_requested = False

# Input: City name
city = st.text_input("Enter city name", "London")

# Button press
if st.button("Get Weather"):
    st.session_state.weather_requested = True

# Only fetch weather if button was pressed
if st.session_state.weather_requested:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        st.subheader(f"Weather in {data['name']}")

        temp = data['main']['temp']
        desc = data['weather'][0]['description'].title()
        humidity = data['main']['humidity']
        wind = data['wind']['speed']

        st.metric("🌡 Temperature (°C)", f"{temp}°C")
        st.metric("💧 Humidity", f"{humidity}%")
        st.metric("🌬 Wind Speed", f"{wind} m/s")
        st.write(f"**Condition:** {desc}")
    else:
        st.error("City not found or API error.")
