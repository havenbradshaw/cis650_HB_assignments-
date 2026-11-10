import streamlit as st

from database import get_all_tracks, delete_track
 
st.subheader("Delete Track")
tracks_dataframe = get_all_tracks()
selected = st.dataframe(tracks_dataframe, on_select="rerun", selection_mode="single-row")
 
if selected.selection.rows:
    selected_index = selected.selection.rows[0]
    track_row = tracks_dataframe.iloc[selected_index]
    st.write(f"Selected track: {track_row['trackTitle']} ({track_row['albumTitle']})")
    confirm = st.checkbox("I confirm the deletion")
    if st.button("Delete track"):
        if confirm:
            delete_track(int(track_row["trackID"]))
            st.rerun()
        else:
            st.warning("Please check the confirmation box before deleting")
 