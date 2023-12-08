from libraries import commands
import spotipy
from libraries.sp_module import sp
from colorama import Fore, Style


def main():
    global user_profile
    print(Fore.GREEN + """ 
:'######:::'#######::'##::: ##::'######:::'#######::'##:::::::'####:'########:'##:::'##:
'##... ##:'##.... ##: ###:: ##:'##... ##:'##.... ##: ##:::::::. ##:: ##.....::. ##:'##::
 ##:::..:: ##:::: ##: ####: ##: ##:::..:: ##:::: ##: ##:::::::: ##:: ##::::::::. ####:::
 ##::::::: ##:::: ##: ## ## ##:. ######:: ##:::: ##: ##:::::::: ##:: ######:::::. ##::::
 ##::::::: ##:::: ##: ##. ####::..... ##: ##:::: ##: ##:::::::: ##:: ##...::::::: ##::::
 ##::: ##: ##:::: ##: ##:. ###:'##::: ##: ##:::: ##: ##:::::::: ##:: ##:::::::::: ##::::
. ######::. #######:: ##::. ##:. ######::. #######:: ########:'####: ##:::::::::: ##::::
:......::::.......:::..::::..:::......::::.......:::........::....::..:::::::::::..:::::
 """ + Style.RESET_ALL)
    try:
        user_profile = sp.current_user()
        print("Successfully authenticated. User profile:")
        print(f"Display name: {user_profile['display_name']}")
        print(f"User ID: {user_profile['id']}")

    except spotipy.SpotifyException as e:
        print(f"Error accessing Spotify API: {e}")
    while True:

        user_input = input("Consolify > ")
        if user_input.split()[0] == "nowplaying":
            commands.nowplaying(user_input.split())
        elif user_input.split()[0] == "search":
            commands.spotify_search(user_input.split())
        elif user_input == "pause":
            commands.pause()
        elif user_input == "play":
            commands.play()
        elif user_input == "skip":
            commands.skip()
        elif user_input == "prev":
            commands.prev()
        elif user_input == "shuffle":
            commands.shuffle()
        elif user_input == "createplist":
            commands.create_playlist(user_profile)
        elif user_input == "playlists":
            commands.playlists()
        elif user_input == "library":
            commands.show_library()
        elif user_input == "close":
            break
        elif user_input == "help":
            print("""=== HELP ===

>>> General <<<
                  
search: Search spotify for a specific song. Use '-a' to show the album.
nowplaying: Shows the song that is playing. Use '-a' to show the album for each search result.
library: Displays the last 20 tracks you added to your library.
createplist: Create a new playlist.
playlists: Allows you to view all the songs in a playlist from your library.
close: Closes the program.
                  
>>> Playback Controls <<<
                  
play: Resume playback or play recently played tracks if no current playback.
pause: Pause the currently playing song.
skip: Skips to the next song.
prev: Skips to the previous song.
shuffle: Toggles the shuffle state.


For more info, read the README.md file.""")
        else:
            print("Not a command! Type 'help' for a list of commands.")


if __name__ == "__main__":
    main()
