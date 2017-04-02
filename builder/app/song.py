from . import services
from .spotify import SpotifyInfo


def main():
    spotify_info = SpotifyInfo(client_service=services.spotify_client)
    result = spotify_info.song(uri='spotify:track:4uLU6hMCjMI75M1A2tKUQC')
    print(result)


if __name__ == "__main__":
    main()
