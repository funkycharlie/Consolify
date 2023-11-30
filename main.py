from consolify_pkgs import commands


def main():
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

