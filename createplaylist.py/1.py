import requests

SPOTIFY_CREATE_PLAYLIST_URL = '	https://api.spotify.com/v1/users/{user_id}/playlists'
ACCESS_TOKEN = 'BQDhExjAiTM1OBMv9IzdwYL8lFgycVzChy6MP_PlGSQMmUGNsDjQW8uHXMpKKLDuK0IWK7nSHz09lwubiRjFBrLjkQRCtClKZwquBxArE2qh9l4OgUAESX0VzvvUl8bTnXBatkaT5Mglr9C9ageX5lI9t4KqFLB1c1cnQe21zLUHdRZzkAyBjmFFMoKVDFpCM_RYG2VWK886biJwxxbPgiYYcL0q'


def create_playlist_on_spotify(name, public):
    response = requests.post(
        SPOTIFY_CREATE_PLAYLIST_URL,
        headers={
            "Authorization": f"bearer{ACCESS_TOKEN}"
        },
        json={
            "name": name,
            "public": public
        }
    )
    json_resp = response.json()

    return json_resp

    def main():
        playlist = create_playlist_on_spotify(
            name-"My Private Playlist",
            public=False
        )

        print(f"Playlist: {playlist}")

    if __name__ == '__main__':
        main()
