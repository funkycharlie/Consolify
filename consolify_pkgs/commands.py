from .global_functions import *
from .sp_module import sp


def nowplaying(args):
    current_song = sp.current_playback()
    if current_song is not None:
        song_name = current_song['item']['name']
        artists = ', '.join([artist['name'] for artist in current_song['item']['artists']])
        album = current_song['item']['album']['name']
        print(f""" 
Now playing: {song_name} by {artists}.""")
        if "-a" in args:
            print(f"Album: {album}")
        print(" ")
    else:
        print("""
No song currently playing.
        """)


def spotify_search(args):
    spotify_search_global(args)



def pause():
    if sp.current_playback() is not None:
        sp.pause_playback()
        print("Paused")
    else:
        print("Can't pause, there is nothing playing.")


def play():
    recently_played = sp.current_user_recently_played(limit=10)
    if recently_played and 'items' in recently_played:
        track_uris = [item['track']['uri'] for item in recently_played['items']]
        sp.start_playback(uris=[track_uris[0]])
        print(f"Playing the most recently played track: {recently_played['items'][0]['track']['name']}")
    else:
        print("No recently played tracks found.")


def create_playlist(user_profile):
    playlist_name = input("Consolify/Playlist/Name > ")
    playlist = sp.user_playlist_create(user=user_profile['id'], name=playlist_name)
    print(f"\nCreated new playlist: {playlist_name}\n")
    print("Would you like to add songs now? (y, or any other input for no.)")
    add_songs_choice = input("Consolify/Playlist/Action > ")
    if add_songs_choice == "y":
        while True:
            result = add_songs_playlist(playlist['uri'])
            if result == "back":
                break
            print("Add another? (y, or any other input for no.)")
            choice = input("Consolify/Playlist/Action > ")
            if choice == "y":
                continue
            else:
                break
