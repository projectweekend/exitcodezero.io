from app.services import clients
from app.services.apis import SpotifyAPI


def main():
    spotify_api = SpotifyAPI(client_service=clients.spotify)
    result = spotify_api.song(uri='spotify:track:4uLU6hMCjMI75M1A2tKUQC')
    print(result)


if __name__ == "__main__":
    main()
