import spotipy
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
import os

client_id = os.environ['API']
client_secret = os.environ['API_SECRET']
scope = "user-read-playback-state,user-modify-playback-state"
sp: Spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,
                                               client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri='http://localhost:8080',
                                               cache_path='cache.cache'
                                               ))