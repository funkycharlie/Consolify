import spotipy
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
scope = "user-read-playback-state,user-modify-playback-state"
sp: Spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,
                                               client_id='e1cda6ac7c13441d8302de7b313b97ea',
                                               client_secret='7ccac525673e455c9778614487dcf453',
                                               redirect_uri='http://localhost:8080',
                                               cache_path='cache.cache'
                                               ))