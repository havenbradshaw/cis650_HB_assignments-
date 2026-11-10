import streamlit as st
from database import search_tracks
 
st.subheader("Search Tracks")
artist_name = st.text_input("Artist name contains")
min_duration = st.number_input("Minimum duration (seconds)", min_value=0, value=0, step=10)
 
results = search_tracks(artist_name, min_duration)
st.write(f"{len(results)} track(s) found")
st.dataframe(results)
 