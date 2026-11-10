import sqlite3

import sqlite3
import pandas as pd

DB_FILE = "music.db"

def get_connection():
    connection = sqlite3.connect(DB_FILE)
    connection.execute("PRAGMA foreign_keys=ON")
    return connection


def initialize_database():
    connection = get_connection()
    with open("schema.sql", "r") as schema_file:
        schema_script = schema_file.read()
    connection.executescript(schema_script)
    connection.commit()
    connection.close()
    print("Database initialized")


def update_album_total(connection, album_id):
    """Sets the album's totalDuration to the sum of its tracks"""
    connection.execute(
        """
        UPDATE Album
        SET totalDuration = (SELECT COALESCE(SUM(duration), 0) FROM Track WHERE albumID = ?)
        WHERE albumID = ?
        """,
        (album_id, album_id)
    )


def add_album(album_title, artist_name, record_label):
    """Inserts a new album and returns the new albumID"""
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO Album(albumTitle, artistName, recordLabel, totalDuration) VALUES(?, ?, ?, 0)",
        (album_title, artist_name, record_label)
    )
    connection.commit()
    new_album_id = cursor.lastrowid
    connection.close()
    return new_album_id


def add_track(album_id, track_title, duration):
    """Inserts a new track, refreshes the album total, and returns the new trackID"""
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO Track(trackTitle, duration, albumID) VALUES(?, ?, ?)",
        (track_title, duration, album_id)
    )
    update_album_total(connection, album_id)
    connection.commit()
    new_track_id = cursor.lastrowid
    connection.close()
    return new_track_id


def get_all_albums():
    connection = get_connection()
    albums_dataframe = pd.read_sql_query("Select * from Album", connection)
    connection.close()
    return albums_dataframe


def get_all_tracks():
    connection = get_connection()
    tracks_dataframe = pd.read_sql_query(
        """
        Select Track.trackID, Track.trackTitle, Track.duration, Album.albumTitle, Album.artistName
        from Track join Album on Album.albumID = Track.albumID
        order by Album.albumTitle, Track.trackID
        """,
        connection
    )
    connection.close()
    return tracks_dataframe


def update_album(album_id, album_title, artist_name, record_label):
    connection = get_connection()
    try:
        cursor = connection.execute(
            "UPDATE Album set albumTitle=?, artistName=?, recordLabel=? where albumID=?",
            (album_title, artist_name, record_label, album_id)
        )
        connection.commit()
        return cursor.rowcount
    finally:
        connection.close()


def search_tracks(artist_name, min_duration):
    """Parameter query: tracks by artist (partial match) at least min_duration seconds long"""
    connection = get_connection()
    tracks_dataframe = pd.read_sql_query(
        """
        Select Track.trackID, Track.trackTitle, Track.duration, Album.albumTitle, Album.artistName
        from Track join Album on Album.albumID = Track.albumID
        where Album.artistName like ? and Track.duration >= ?
        order by Album.artistName, Track.trackTitle
        """,
        connection,
        params=(f"%{artist_name}%", min_duration)
    )
    connection.close()
    return tracks_dataframe


def delete_track(track_id):
    connection = get_connection()
    row = connection.execute("Select albumID from Track where trackID=?", (track_id,)).fetchone()
    connection.execute("Delete from Track where trackID=?", (track_id,))
    if row:
        update_album_total(connection, row[0])
    connection.commit()
    connection.close()


if __name__ == "__main__":
    initialize_database()