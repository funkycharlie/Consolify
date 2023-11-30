from .sp_module import sp


def nowplaying():
    current_song = sp.current_playback()
    if current_song and 'item' in current_song and 'name' in current_song['item']:
        song_name = current_song['item']['name']
        artists = ', '.join([artist['name'] for artist in current_song['item']['artists']])
        print(f"Now playing: {song_name} by {artists}.")
    else:
        print("No song currently playing.")
