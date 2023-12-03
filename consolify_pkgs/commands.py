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
    def play_search(check_quick):
        try:
            track_number_int = 0 if check_quick else int(input("Consolify/Search/Play > "))
            selected_track = result['tracks']['items'][track_number_int]
            if track_number_int == "back":
                return "back"
            playback(selected_track)
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid track number or type 'back' to go back.")
            play_search(check_quick)

    def add_queue_search(check_quick):
        try:
            track_number = 0 if check_quick else int(input("Consolify/Search/Add To Queue > "))
            selected_track = result['tracks']['items'][track_number]
            if track_number == "back":
                return "back"
            add_to_queue(selected_track)
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid track number or type 'back' to go back.")
            add_queue_search(check_quick)

    while True:
        search_str = input("Consolify/Search > ")
        if search_str == "back":
            break

        try:
            result = sp.search(q=search_str, limit=10)
            print(" ")

            if "-p" and "-q" not in args:
                for i, t in enumerate(result['tracks']['items']):
                    track_name = t['name']
                    artists = ', '.join([artist['name'] for artist in t['artists']])
                    album = t['album']['name']
                    print(f" {i} {track_name} by {artists}")
                    if "-a" in args:
                        print(f"Album: {album}")
                    print(" ")

            if "-p" in args:
                play_search_result = play_search(True)
                if play_search_result == "back":
                    break
                continue

            if "-q" in args:
                add_queue_search_result = add_queue_search(True)
                if add_queue_search_result == "back":
                    break
                continue

        except spotipy.SpotifyException as e:
            print(f"Error: Search query not valid: {e}")
            continue

        print(""" 
What would you like to do? You could say: 'play', 'back' or 'add queue'
 """)
        user_choice = input("Spotify/Search/Action > ")
        if user_choice == "back":
            continue
        elif user_choice == "play":
            play_search_result = play_search(False)
            if play_search_result == "back":
                continue
        elif user_choice == "add queue":
            add_queue_search_result = add_queue_search(False)
            if add_queue_search_result == "back":
                continue
        else:
            print('Invalid input, please try again')


def pause():
    current_playback = sp.current_playback()
    
    if current_playback is not None:
        # Check if Spotify is already paused
        if current_playback.get('is_playing', False):
            sp.pause_playback()
            print("Paused")
        else: 
            print("Spotify is already paused.")
    else:
        print("Can't pause, there is nothing playing.")


def play():
    current_playback = sp.current_playback()

    # Resume playback if there is a current playback
    if current_playback is not None:
        if current_playback.get('is_playing', False):
            print("Spotify is already playing.")
        else: 
            print("Resuming playback.")
            sp.start_playback()
    # Play recently played songs if there is no current playback
    else:
        recently_played = sp.current_user_recently_played(limit=10)

        # Check if there are recently played songs
        if recently_played and 'items' in recently_played:
            # Get the track URIs from the recently played songs
            track_uris = [item['track']['uri'] for item in recently_played['items']]

            # Choose a device for playback
            device_id = choose_device()

            # Check if the user chose to go back or no device was selected
            if device_id == "back":
                return "back"
            elif device_id is None:
                print("Playback aborted.")
                return

            # Start playback with the most recently played tracks on the chosen device
            sp.start_playback(uris=track_uris, device_id=device_id)
            print(f"Playing the most recently played track: {recently_played['items'][0]['track']['name']}")
        else:
            print("No recently played tracks found.")
