import vcr

from app.services.apis import SpotifyAPI
from app.services.clients import spotify


ALBUM_SPOTIFY_URI = 'spotify:album:6N9PS4QXF1D0OWPk0Sxtb4'
EXPECTED_ALBUM_RESULT = {
    'genres': [],
    'images': [
        {
            'height': 640,
            'url': 'https://i.scdn.co/image/15ac2c9091d9b74e841b281ceb23ca8208321444',
            'width': 640
        },
        {
            'height': 300,
            'url': 'https://i.scdn.co/image/90ed6823864381221c03dc3c9fc62d094e81dfb2',
            'width': 300
        },
        {
            'height': 64,
            'url': 'https://i.scdn.co/image/568017ab80000e71ca299909806898f75a948456',
            'width': 64
        }
    ],
    'name': 'Whenever You Need Somebody',
    'release_date': '1987-11-12',
    'uri': 'spotify:album:6N9PS4QXF1D0OWPk0Sxtb4'
}


@vcr.use_cassette('cassettes/spotify_api_album.yml')
def test_spotify_api_album():
    spotify_api = SpotifyAPI(client_service=spotify)

    album = spotify_api.album(uri=ALBUM_SPOTIFY_URI)
    assert album == EXPECTED_ALBUM_RESULT
