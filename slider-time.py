import streamlit as st
from datetime import time

minTime = time(6,00)
maxTime = time(23,00)
defaultMin = time(10,00)
defaultMax = time(20,00)

val1, val2 = st.slider('Time of day?', min_value=minTime, max_value=maxTime, value=(defaultMin, defaultMax), format="LT")

st.write(val1, val2)
# Expected default: 10:00:00 20:00:00
