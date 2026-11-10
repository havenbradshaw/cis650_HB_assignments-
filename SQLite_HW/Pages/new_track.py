# pages/new_patient_intake.py
import streamlit as st
from database import add_album
 
st.subheader("New Album")
with st.form("new_album_form"):
    album_title = st.text_input("Album Title")
    artist_name = st.text_input("Artist Name")
    record_label = st.text_input("Record Label")
    submitted = st.form_submit_button("Save Album")
if submitted:
    if album_title and artist_name:
        new_album_id = add_album(album_title, artist_name, record_label)
        st.success(f"Album created.  Album ID: {new_album_id}")
    else:
        st.error("Album title and artist name are required.")
 