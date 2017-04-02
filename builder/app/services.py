import os

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')


def spotify_client():
    client_creds = SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID,
                                            client_secret=SPOTIFY_CLIENT_SECRET)
    return spotipy.Spotify(client_credentials_manager=client_creds)
