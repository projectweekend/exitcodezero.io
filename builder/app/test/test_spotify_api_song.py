import vcr

from app.services.apis import SpotifyAPI
from app.services.clients import spotify


SONG_SPOTIFY_URI = 'spotify:track:4uLU6hMCjMI75M1A2tKUQC'
EXPECTED_SONG_RESULT = {
    'name': 'Never Gonna Give You Up',
    'preview_url': 'https://p.scdn.co/mp3-preview/a69cabb16c6c3333db903d1f538e808493689e40?cid=eb0f8ab201994a8583fb25f99aa6fad5',
    'uri': 'spotify:track:4uLU6hMCjMI75M1A2tKUQC',
    'album': {
        'uri': 'spotify:album:6N9PS4QXF1D0OWPk0Sxtb4'
    },
    'artist': {
        'uri': 'spotify:artist:0gxyHStUsqpMadRV0Di1Qt'
    }
}


@vcr.use_cassette('cassettes/spotify_api_song.yml')
def test_spotify_api_song():
    spotify_api = SpotifyAPI(client_service=spotify)

    song = spotify_api.song(uri=SONG_SPOTIFY_URI)
    assert song == EXPECTED_SONG_RESULT
