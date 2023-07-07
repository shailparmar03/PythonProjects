import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"
SPOTIFY_CLIENT_ID="36954d647b224bfa93d5538c695f9f06"
SPOTIPY_CLIENT_SECRET="96323b2fbb1c48d09dc53379b3c7300f"
SPOTIPY_REDIRECT_URI="http://example.com"

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

try:
    response = requests.get(url=BILLBOARD_URL + date)
    response.raise_for_status()

except requests.exceptions.HTTPError as e:
    print(e)
else:
    soup = BeautifulSoup(response.text,"html.parser")
    songs_name_span = soup.select(selector="li h3#title-of-a-story")
    song_names=[song.getText().strip() for song in songs_name_span]
    song_uris=[]

    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri=SPOTIPY_REDIRECT_URI,
            client_id=SPOTIFY_CLIENT_ID,
            client_secret=SPOTIPY_CLIENT_SECRET,
            show_dialog=True,
            cache_path="token.txt"
        )
    )
    user_id = sp.current_user()["id"]
    year = date.split("-")[0]
    for song in song_names:
        result=sp.search(q=f"track:{song} year:{year}",type="track")
        print(result)
        try:
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        except IndexError:
            print(f"{song} doesn't exist in Spotify. Skipped.")

    playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
    print(playlist)
    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)