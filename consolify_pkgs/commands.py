from .global_functions import *
from .sp_module import sp


def nowplaying(args):
    current_song = sp.current_playback()
    if current_song is not None:
        song_name = current_song['item']['name']
        artists = ', '.join([artist['name'] for artist in current_song['item']['artists']])
        album = current_song['item']['album']['name']
        print(f"Now playing: {song_name} by {artists}.")
        if args[-1] == "-a":
            print(f"Album: {album}")
    else:
        print("No song currently playing.")


def spotify_search(args):
    while True:
        search_str = input("Consolify/Search >")
        if search_str == "back":
            break
        try:
            result = sp.search(q=search_str, limit=10)
            for i, t in enumerate(result['tracks']['items']):
                track_name = t['name']
                artists = ', '.join([artist['name'] for artist in t['artists']])
                album = t['album']['name']
                print(f" {i} {track_name} by {artists}")
                if args[-1] == "-a":
                    print(f"Album: {album}")
                print(" ")
        except spotipy.SpotifyException as e:
            print(f"Error: Search query not valid: {e}")
            continue

        def play_search():

            try:
                track_number = input("Consolify/Search/Play >")
                if track_number == "back":
                    return "back"
                track_number_int = int(track_number)
                selected_track = result['tracks']['items'][track_number_int]
                playback(selected_track)

            except (ValueError, IndexError):
                print("Invalid input. Please enter a valid track number, or to go back, type 'back'.")
                play_search()

        play_search_result = play_search()
        if play_search_result == "back":
            continue
