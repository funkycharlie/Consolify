import spotipy

from .sp_module import sp


def choose_device():
    devices = sp.devices()
    if not devices['devices']:
        print("No devices found. Check your spotify client is active.")
        return None

    print("Choose a device:")
    for i, device in enumerate(devices['devices']):
        print(f"{i}. {device['name']} ({device['id']})")

    try:
        device_number = int(input("Consolify/Playback/Choose Device >"))
        selected_device_id = devices['devices'][device_number]['id']
        return selected_device_id
    except (ValueError, IndexError):
        print("Invalid input. Please choose a valid device number")
        choose_device()


def nowplaying():
    current_song = sp.current_playback()
    if current_song is not None:
        song_name = current_song['item']['name']
        artists = ', '.join([artist['name'] for artist in current_song['item']['artists']])
        print(f"Now playing: {song_name} by {artists}.")
    else:
        print("No song currently playing.")


def playback(selected_track):
    selected_track_name = selected_track['name']
    selected_track_artists = ", ".join([artist['name'] for artist in selected_track['artists']])
    track_uri = selected_track['uri']

    try:
        if sp.current_playback() is None:
            device_id = choose_device()
            sp.start_playback(uris=[track_uri], device_id=device_id)
        else:
            sp.start_playback(uris=[track_uri])

        print(f"Now playing: {selected_track_name} by {selected_track_artists}")

    except spotipy.SpotifyException as e:
        print(f"Error playing track: {e}")


def spotify_search():
    while True:
        search_str = input("Consolify/Search >")
        if search_str == "back":
            break
        result = sp.search(q=search_str, limit=20)
        for i, t in enumerate(result['tracks']['items']):
            track_name = t['name']
            artists = ', '.join([artist['name'] for artist in t['artists']])
            print(f" {i} {track_name} by {artists}")

        def play_search():
            try:
                track_number = input("Consolify/Search/Play >")
                if track_number == "back":
                    spotify_search()
                track_number_int = int(track_number)
                selected_track = result['tracks']['items'][track_number_int]
                playback(selected_track)

            except (ValueError, IndexError):
                print("Invalid input. Please enter a valid track number, or to go back, type 'back'.")
                play_search()

        play_search()
