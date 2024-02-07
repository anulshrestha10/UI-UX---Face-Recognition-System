import time
from datetime import datetime

import pandas as pd
import streamlit as st

ts=time.time()
date=datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
timestamp=datetime.fromtimestamp(ts).strftime("%H:%M-%S")

from streamlit_autorefresh import st_autorefresh

count = st_autorefresh(interval=2000, limit=100, key="fizzbuzzcounter")

if count == 0:
    st.write("Welcome to ShresthaCompany's Attendance List")
elif count % 3 == 0 and count % 5 == 0:
    st.write("Have a good day !")
elif count % 3 == 0:
    st.write("Have a wonderful day! Enjoy work")
elif count % 5 == 0:
    st.write("Goodbye")
else:
    st.write(f"Count: {count}")


df=pd.read_csv("Attendance/Attendance_" + date + ".csv")

st.dataframe(df.style.highlight_max(axis=0))