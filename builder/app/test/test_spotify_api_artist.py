import vcr

from app.services.apis import SpotifyAPI
from app.services.clients import spotify


ARTIST_SPOTIFY_URI = 'spotify:artist:0gxyHStUsqpMadRV0Di1Qt'
EXPECTED_ARTIST_RESULT = {
    'genres': [
        'dance pop',
        'dance rock',
        'europop',
        'new romantic',
        'new wave',
        'new wave pop',
        'soft rock',
        'synthpop'
    ],
    'images': [
        {
            'height': 640,
            'url': 'https://i.scdn.co/image/ff2ff20dae7cf00a9320d0663100be14ccdd9dac',
            'width': 640
        },
        {
            'height': 320,
            'url': 'https://i.scdn.co/image/95cb17dae0addf1a0e9e7b68ca98746e793fc8c2',
            'width': 320
        },
        {
            'height': 160,
            'url': 'https://i.scdn.co/image/5a471f7f34b4415f932e352a81fe38cfa60a92b5',
            'width': 160
        }
    ],
    'name': 'Rick Astley',
    'uri': 'spotify:artist:0gxyHStUsqpMadRV0Di1Qt'
}


@vcr.use_cassette('cassettes/spotify_api_artist.yml')
def test_spotify_api_artist():
    spotify_api = SpotifyAPI(client_service=spotify)

    artist = spotify_api.artist(uri=ARTIST_SPOTIFY_URI)
    assert artist == EXPECTED_ARTIST_RESULT
