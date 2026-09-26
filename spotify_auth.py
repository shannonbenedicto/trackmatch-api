import os
import base64
import requests
from dotenv import load_dotenv


def get_access_token():
    
    load_dotenv()

    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

    combined = f"{client_id}:{client_secret}"
    encoded = base64.b64encode(combined.encode())

    response = requests.post(
        'https://accounts.spotify.com/api/token',
        headers = {'Authorization': 'Basic ' + encoded.decode()},
        data = {'grant_type': 'client_credentials'} 
        )
    
    response_dict = response.json()
    
    return response_dict['access_token']