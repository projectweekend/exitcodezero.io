from spotipy import Spotify
from app.services import clients


def test_spotify_client():
    spotify_client = clients.spotify()
    assert isinstance(spotify_client, Spotify)
