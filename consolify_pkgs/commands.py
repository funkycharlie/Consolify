from .sp_module import sp


def nowplaying():
    current_song = sp.current_playback()
    if current_song['item'] is not None:
        song_name = current_song['item']['name']
        artists = ', '.join([artist['name'] for artist in current_song['item']['artists']])
        print(f"Now playing: {song_name} by {artists}.")
    else:
        print("No song currently playing.")


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


