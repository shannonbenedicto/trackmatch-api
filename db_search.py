import sqlite3

def find_db_track(track_name, artist):

    con = sqlite3.connect('trackmatch.db')
    cur = con.cursor()

    # Artists field uses LIKE pattern since each track may be made by multiple artists - my code only checks against one
    cur_pos = cur.execute("SELECT * FROM tracks WHERE track_name = ? AND artists LIKE ?", (track_name, f"%{artist}%"))
    response = cur.fetchone()

    con.close()

    if response is None:
        return None

    track_data = {}
    for i in range(len(response)):
        # Fill dict with the column name as the key and record value as the value
        track_data[cur_pos.description[i][0]] = response[i]

    return track_data