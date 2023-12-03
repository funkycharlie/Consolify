import json
import os

import spotipy
from spotipy.oauth2 import SpotifyOAuth

CONFIG_FILE = 'config.json'
CACHE_FILE = 'cache.cache'
REDIRECT_URI = 'http://localhost:8080'
SCOPE = 'user-read-playback-state,user-modify-playback-state,user-read-recently-played,playlist-modify-public,playlist-modify-private'


def get_spotify_credentials():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as file:
            config = json.load(file)
            client_id = config.get('client_id')
            client_secret = config.get('client_secret')
            return client_id, client_secret
    else:
        return None, None


def save_spotify_credentials(client_id, client_secret):
    with open(CONFIG_FILE, 'w') as file:
        json.dump({'client_id': client_id, 'client_secret': client_secret}, file)


def authenticate_spotify():
    client_id, client_secret = get_spotify_credentials()

    if not client_id or not client_secret:
        print("""First, you need to go to https://developer.spotify.com/dashboard, and make an application:
        -Enter a name and description
        -The application's redirect URI MUST be: http://localhost:8080
        -When prompted, go to the settings of your spotify application, and copy the Client ID and Client Secret
        -You'll only have to do this once""")
        client_id = input("Consolify/Client ID > ")
        client_secret = input("Consolify/Client Secret > ")
        save_spotify_credentials(client_id, client_secret)

    try:
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE,
                                                       client_id=client_id,
                                                       client_secret=client_secret,
                                                       redirect_uri=REDIRECT_URI,
                                                       cache_path=CACHE_FILE))
        return sp
    except Exception as e:
        print(f"Error during authentication: {e}")
        return None


try:
    sp = authenticate_spotify()

    if sp:
        user_profile = sp.current_user()
        display_name = user_profile.get('display_name', 'Unknown')
        print(f"Welcome, {display_name}!")

except Exception as e:
    print(f"Error: {e}")
