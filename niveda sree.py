import streamlit as st
st.title("Guessing Game with Binary Search")
st.write("Think of a number between 1 and 10, and I'll try to guess it!")
if 'low' not in st.session_state:
    st.session_state.low = 1  
    st.session_state.high = 10  
    st.session_state.guess = (st.session_state.low + st.session_state.high) // 2  
st.write(f"My guess is: **{st.session_state.guess}**")
col1, col2, col3 = st.columns(3)

with col1:
    too_low = st.button("Too Low")
with col2:
    correct = st.button("Correct!")
with col3:
    too_high = st.button("Too High")
if too_low:
      st.session_state.low = st.session_state.guess + 1
elif too_high:
    st.session_state.high = st.session_state.guess - 1
elif correct:
    st.success(f"I guessed your number! It's {st.session_state.guess}. ")
    st.stop()  
if st.session_state.low <= st.session_state.high:
    st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
else:
    st.error("Hmm... Something went wrong. Are you sure you followed the rules?")
