#pages/update_patient.py
import streamlit as st
import database from get_all_albums, update_album

st.subheader("Update Album")
albums_dataframe = get_all_albums()
selected = st.dataframe(albums_dataframe, on_select="rerun", selection_mode="single-row")
 
if selected.selection.rows:
    selected_index = selected.selection.rows[0]
    album_row = albums_dataframe.iloc[selected_index]
    st.write(f"Editing album: {album_row['albumTitle']}")
 
    with st.form("update_album_form"):
        new_title = st.text_input("Album Title", value=album_row["albumTitle"])
        new_artist = st.text_input("Artist Name", value=album_row["artistName"])
        new_label = st.text_input("Record Label", value=album_row["recordLabel"] or "")
        submitted = st.form_submit_button("Save changes")
        if submitted:
            update_album(int(album_row["albumID"]), new_title, new_artist, new_label)
            st.success("Album updated")
            st.rerun()