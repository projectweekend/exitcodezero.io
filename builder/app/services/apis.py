from concurrent.futures import ThreadPoolExecutor, as_completed

from app.utils import filter_dict


class SpotifyAPI:

    def __init__(self, client_service):
        self._client = client_service()

    def artist(self, uri):
        artist = self._client.artist(uri)
        return filter_dict(artist, {'uri', 'name', 'images', 'genres'})

    def album(self, uri):
        album = self._client.album(uri)
        return filter_dict(album, {'uri', 'name', 'images', 'genres', 'release_date'})

    def song(self, uri):
        track = self._client.track(uri)
        result = filter_dict(track, {'name', 'preview_url', 'uri'})
        result['artist'] = {'uri': track['artists'].pop()['uri']}
        result['album'] = {'uri': track['album']['uri']}
        return result
