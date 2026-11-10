import streamlit as st
 
def home():
    st.title("Music Library")
    st.write("Use the sidebar to navigate")
 
pg = st.navigation([
    st.Page(home, title="Home"),
    st.Page("pages/new_album.py", title="New Album"),
    st.Page("pages/new_track.py", title="New Track"),
    st.Page("pages/update_album.py", title="Update Album"),
    st.Page("pages/search_tracks.py", title="Search Tracks"),
    st.Page("pages/delete_track.py", title="Delete Track"),
    ])

pg.run()
 