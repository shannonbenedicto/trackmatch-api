import os
import base64
import requests
import json
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

combined = f"{client_id}:{client_secret}"
encoded = base64.b64encode(combined.encode())

response = requests.post(
    'https://accounts.spotify.com/api/token',
    headers = {'Authorization' : 'Basic ' + encoded.decode()},
    data = {'grant_type' : "client_credentials"}
)

response_dict = response.json()
access_token = response_dict['access_token']

track = requests.get(
    'https://api.spotify.com/v1/search',
    headers = {"Authorization": f"Bearer {access_token}"},
    params = {"q": "Evergreen Omar Apollo", "type": "track"}
)

print(track.status_code)
print(track.text)