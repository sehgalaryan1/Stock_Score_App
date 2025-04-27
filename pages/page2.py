import streamlit as st
import pandas as pd

st.title("Page 2: Stock Price Statistics")


if 'data' in st.session_state:
   st.write("Statistics of the DataFrame:")
   st.write(st.session_state.data.describe())
else:
   st.write("No stock data found. Please select stock on Main Page.")



#if 'data' in st.session_state:
#   st.write("Statistics of the DataFrame:")
#   st.write(st.session_state.data.describe())
#else:
#   st.write("No DataFrame found. Please create it in the 'Create DataFrame' page.")


#if "Close" in data:
#   st.subheader("Closing Price Over Time")
#   st.line_chart(data['Close'])
#else:
#   st.warning("Closing price data is not available for this stock.")
