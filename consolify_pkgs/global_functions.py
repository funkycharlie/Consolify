from .sp_module import sp
import spotipy


def choose_device():
    devices = sp.devices()
    if not devices['devices']:
        print("No devices found. Check spotify is open on the device you want to listen on.")
        return None

    print("Choose a device:")
    for i, device in enumerate(devices['devices']):
        print(f"{i}. {device['name']} ({device['id']})")
    print("If your device is not listed, check that spotify is open on that device.")

    try:
        device_number = input("Consolify/Playback/Choose Device >")
        if device_number == "back":
            return "back"

        selected_device_id = devices['devices'][device_number]['id']
        return selected_device_id
    except (ValueError, IndexError):
        print("Invalid input. Please choose a valid device number")
        choose_device()


def playback(selected_track):
    def playback_restart():
        selected_track_name = selected_track['name']
        selected_track_artists = ", ".join([artist['name'] for artist in selected_track['artists']])
        track_uri = selected_track['uri']

        try:
            if sp.current_playback() is None:
                device_id = choose_device()
                if device_id == "back":
                    return "back"

                sp.start_playback(uris=[track_uri], device_id=device_id)
            else:
                sp.start_playback(uris=[track_uri])

            print(f"Now playing: {selected_track_name} by {selected_track_artists}")

        except spotipy.SpotifyException as e:
            print(f"There was an error playing the track: {e}")
            playback_restart()
    playback_restart()



