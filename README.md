
# Consolify - Spotify Console Interface

Consolify is a console interface for interacting with the Spotify API using the Spotipy library.

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/funkytoast/consolify.git
   cd consolify
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Spotify API credentials:**

   - Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard) and create a new application.
   - Enter a name and description for your application.
   - Set the application's redirect URI to: `http://localhost:8080`
   - Copy the Client ID and Client Secret from your application's settings.
   - Run the main.py and enter the prompted Client ID and Client Secret:

     ```bash
     python main.py
     ```

## Features

### Commands (`commands.py`)

- **nowplaying [options]:** Display information about the currently playing song.
    - Option "-a" shows the album of the song.
- **search [options]:** Search for a specific song on Spotify.
    - Option "-a" shows the album for each search result.
    - Option "-q" adds the first search result to the queue.
    - Option "-p" plays the first search result.
- **pause:** Pause the currently playing song.
- **play:** Resume playback or play recently played tracks if no current playback.
- **createplist:** Create a new playlist for the authenticated user.
- **close:** Exit the program.
- **help:** Display a list of available commands and usage information.

## Playback and Search

### `global_functions.py`

#### Functions

- **choose_device():** Choose a device for playback.
- **playback(selected_track):** Start playback of a selected track.
- **add_to_queue(selected_track):** Add a selected track to the playback queue.
- **spotify_search_global(args):** Global search function with various options.
- **add_songs_playlist(playlist):** Add songs to a specified playlist.

    ### `sp_module.py`

This script is used to set up Spotify API credentials for the Consolify application.

## Usage

1. Run the main.py file to authenticate with Spotify.
2. Enter commands in the console to control your Spotify playback and perform other actions.

For more details, refer to the source code and individual module documentation.

## Dependencies

- spotipy: Spotify API library
- Other project dependencies (see requirements.txt)

## Author

Funkycharlie

## License

This project is licensed under the GNU General Public License - see the [LICENSE](LICENSE) file for details.
