import os
from concurrent.futures import ThreadPoolExecutor, as_completed
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')


client_creds = SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID,
                                        client_secret=SPOTIFY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_creds)


def album_info(uri):
    album = sp.album(uri)
    return {
        'uri': album['uri'],
        'genres': album['genres'],
        'images': album['images'],
        'release_date': album['release_date']
    }


def artist_info(uri):
    artist = sp.artist(uri)
    desired_keys = {'uri', 'name', 'images', 'genres'}
    return {k: v for k, v in artist.items() if k in desired_keys}


def song_info(uri):
    track = sp.track(uri)
    result = {
        'title': track['name'],
        'preview_url': track['preview_url']
    }

    with ThreadPoolExecutor() as executor:
        tasks = {
            executor.submit(album_info, track['album']['uri']): 'album',
            executor.submit(artist_info, track['artists'].pop()['uri']): 'artist'
        }

    for future in as_completed(tasks):
        result[tasks[future]] = future.result()

    return result
