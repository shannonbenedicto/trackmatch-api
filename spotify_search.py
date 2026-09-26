import requests

def search_track(track_name, artist, token):

    if artist is not None:
        query = f"track:{track_name} artist:{artist}"
    else:
        query = f"track:{track_name}"

    matched = requests.get(
    'https://api.spotify.com/v1/search',
    headers = {"Authorization": f"Bearer {token}"},
    params = {"q": query, "type": "track"}
    )

    matched_songs = matched.json()["tracks"]["items"]
    if len(matched_songs) == 0:
        return None

    song = matched_songs[0]

    return {
    "track_id": song["id"],
    "track_name": song["name"],
    "artist": song["artists"][0]["name"]
    }
    