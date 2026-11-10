import streamlit as st
 
def home():
    st.title("Music Library")
    st.write("Use the sidebar to navigate")
 
pg = st.navigation([
    st.Page(home, title="Home", icon="⌂"),
    st.Page("pages/new_album.py", title="New Album", icon="♫"),
    st.Page("pages/new_track.py", title="New Track", icon="✙"),
    st.Page("pages/update_album.py", title="Update Album", icon="✎"),
    st.Page("pages/search_tracks.py", title="Search Tracks", icon="⌕"),
    st.Page("pages/delete_track.py", title="Delete Track", icon="✖"),
    ])

pg.run()
 