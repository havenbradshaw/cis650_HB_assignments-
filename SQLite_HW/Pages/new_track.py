import streamlit as st
from database import get_all_albums, add_track

st.subheader("New Track")
albums_dataframe = get_all_albums()

if albums_dataframe.empty:
    st.warning("Add an album first.")
else:
    with st.form("new_track_form"):
        selected_album_title = st.selectbox("Album",
albums_dataframe["albumTitle"])
        track_title = st.text_input("Track Title")
        duration = st.number_input("Duration (seconds)", min_value=1, value=180, step=1)
        submitted = st.form_submit_button("Save Track")
    if submitted:
        if track_title:
            selected_album_id = int(albums_dataframe.loc[albums_dataframe["albumTitle"] 
                                == selected_album_title, "albumID"].iloc[0])
            new_track_id = add_track(selected_album_id, track_title, duration)
            st.success(f"Track added. Track ID: {new_track_id}")
        else:
            st.error("Track title is required.")