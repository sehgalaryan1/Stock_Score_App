import streamlit as st

st.title("Page 3: Close Price data")

if 'data' in st.session_state:
   st.line_chart(st.session_state.data['Close'])
#   st.write(st.session_state.data['Date'])
else:
   st.write("No stock data found. Please select stock on Main Page.")

#   cl_prc=st.session_state.data['Close']
