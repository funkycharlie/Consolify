import spotipy
from .sp_module import sp
import time


def choose_device():
    devices = sp.devices()
    if not devices['devices']:
        print("No devices found. Check if Spotify is open on the device you want to listen to.")
        return None

    print("Choose a device:")
    for i, device in enumerate(devices['devices']):
        print(f"{i}. {device['name']} ({device['id']})")

    print("If your device is not listed, check that Spotify is open on that device.")

    while True:
        try:
            device_number = input("Consolify/Playback/Choose Device > ")
            if device_number.lower() == "back":
                return "back"

            device_number = int(device_number)
            selected_device_id = devices['devices'][device_number]['id']
            return selected_device_id
        except (ValueError, IndexError):
            print("Invalid input. Please choose a valid device number")


def playlists_global(uri):
    playlist_items = sp.playlist_items(uri)
    if 'items' in playlist_items:
        for i, item in enumerate(playlist_items['items']):
            track = item['track']
            print(f"{i}. {track['name']}")
    else:
        print("No items found in the playlist.")
        return
    print("What would you like to do? You could say 'add', 'play' or 'back'.")
    action = input("Consolify/Playlist/Action > ")
    if action == "back":
        return "back"
    elif action == "play":
        track_selection = input("Spotify/Playlist/Play > ")
        if track_selection == "back":
            playlists_global(uri)
        else:
            track_selection = int(track_selection)
            track = playlist_items['items'][track_selection]
            track_uri = track['track']
            playback(track_uri)
    elif action == "add":
        track_uri = spotify_search_global("Playlist")
        if track_uri == "back":
            playlists_global(uri)
        else:
            sp.playlist_add_items(playlist_id=uri, items=[track_uri])
        playlists_global(uri)
    else:
        print("That isn't a valid response, please try again.")
        time.sleep(2)
        playlists_global(uri)




def playback(selected_track):
    selected_track_name = selected_track['name']
    selected_track_artists = ", ".join([artist['name'] for artist in selected_track['artists']])
    track_uri = selected_track['uri']

    try:
        current_playback = sp.current_playback()
        if current_playback is None:
            device_id = choose_device()
            if device_id == "back":
                return "back"
            elif device_id is None:
                print("Playback aborted.")
                return

            sp.start_playback(uris=[track_uri], device_id=device_id)
        else:
            sp.start_playback(uris=[track_uri])

        print(f"Now playing: {selected_track_name} by {selected_track_artists}")

    except spotipy.SpotifyException as e:
        print(f"There was an error playing the track: {e}")


def add_to_queue(selected_track):
    selected_track_name = selected_track['name']
    selected_track_artists = ", ".join([artist['name'] for artist in selected_track['artists']])
    track_uri = selected_track['uri']

    try:
        current_playback = sp.current_playback()

        if current_playback is None:
            device_id = choose_device()
            if device_id == "back":
                return "back"
            elif device_id is None:
                print("Playback aborted.")
                return

            sp.add_to_queue(uri=track_uri, device_id=device_id)
        else:
            sp.add_to_queue(uri=track_uri)

        print(f"Added to queue: {selected_track_name} by {selected_track_artists}")

    except spotipy.SpotifyException as e:
        print(f"There was an error adding the track to the queue: {e}")


def spotify_search_global(args):
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

        if "Playlist" in args:
            while True:
                user_choice = input("Search/Add to Playlist > ")
                if user_choice == "back":
                    return "back"
                try:
                    user_choice = int(user_choice)
                    track = result['tracks']['items'][user_choice]
                    return track['uri']
                except (ValueError, IndexError):
                    print("That's not a valid choice, please try again.")
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


def add_songs_playlist(playlist):
    track_uri = [spotify_search_global(["Playlist"])]
    if track_uri == "back":
        return "back"
    print("Adding tracks to playlist:", track_uri)
    sp.playlist_add_items(playlist_id=playlist, items=track_uri)
