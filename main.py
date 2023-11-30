from consolify_pkgs import commands


def main():
    while True:
        user_input = input(">")
        if user_input == "nowplaying":
            commands.nowplaying()
        else:
            print("Not a command! Type 'help' for a list of commands.")


if __name__ == "__main__":
    main()

