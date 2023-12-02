# Consolify

![logo](https://github.com/funkycharle/Consolify/assets/152520435/7ac23679-16d6-4b0c-8c8a-e9e2b58332c2)

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

The search command starts a search for specific song you would like only.

Next, you choose what you want to do with the search results.

Afterwards, you can choose the number of the song you want to listen to.

If a song isn't already playing, it'll also ask you for the device to play it on.

At any time you can type 'back' to go back.

**Arguments**

-a : For each search result, show the album of that track.

-p : Plays the first search result of the search query.

-q : Adds the first search result of the search query to the queue.

**Search Actions**

There are a few actions you can take after the search results are displayed:

play: Plays the track, specified afterwards.

add queue: Adds the track specified later to the queue.

back: Goes back to the search box.

### nowplaying:

Running this command tells you what song is currently playing.

**Arguments**

-a : Shows the album of the current song.

### pause:

Running this command stops the current song.

### play:

Running this command plays the last 10 recently played tracks.

### help:

Displays help on all the commands in the program (not always up to date, check this README document for the latest.)

## License

This software is under the GNU General Public license. 
Take a look at the [LICENSE](LICENSE) file for more info.
