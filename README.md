# Consolify

![logo](https://github.com/funkycharlie/Consolify/assets/152520435/7ac23679-16d6-4b0c-8c8a-e9e2b58332c2)

Thanks for checking out Consolify!

This project is in no way done whatsoever, so if you find anything that wants changing, that'd really help me out if you made a pull request, or even just an issue!

To start using it, clone or download the repository.

Then, install the required modules using:

`pip install -r requirements.txt`

Afterwards, you can run:

`python3 main.py`

to start the program.

## On first startup

The program will ask you to add your API keys.

To do this, navigate to https://developer.spotify.com, then login, then navigate to the dashboard.

Create a new application. Give it a title, and a description.

Set the Redirect URI to http://localhost:8080

Then once you have finished setting it up, navigate to settings.

Copy and paste each key when prompted into the terminal.

Finally, the app will check if you are authenticated.

## Commands

At the moment there are two commands for Consolify:

### search:

The search command starts a search. You can search for a specific song you would like.

Afterwards, you can choose the number of the song you want to listen to.

If a song isn't already playing, it'll also ask you for the device to play it on.

At any time you can type 'back' to go back.

**Arguments**

-a : For each search result, show the album of that track.

### nowplaying:

Running this command tells you what song is currently playing.

**Arguments**

-a : Shows the album of the current song.

## License

This software is under the GNU General Public license. 
Take a look at the [LICENSE](LICENSE) file for more info.
