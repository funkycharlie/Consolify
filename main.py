from consolify_pkgs import commands
import spotipy
from consolify_pkgs.sp_module import sp


def main():
    try:
        user_profile = sp.current_user()
        print("Successfully authenticated. User profile:")
        print(f"Display name: {user_profile['display_name']}")
        print(f"User ID: {user_profile['id']}")

    except spotipy.SpotifyException as e:
        print(f"Error accessing Spotify API: {e}")
    while True:

        user_input = input("Consolify >")
        if user_input == "nowplaying":
            commands.nowplaying()
        elif user_input == "search":
            commands.spotify_search()
        elif user_input == "close":
            break
        else:
            print("Not a command! Type 'help' for a list of commands.")


if __name__ == "__main__":
    main()
