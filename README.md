# Spotify Song Exporter

This Python script utilizes Spotipy to fetch and export a list of user-saved songs from Spotify.

## Overview

The provided Python script interacts with the Spotify API using Spotipy and exports a list of user-saved songs to a JSON file.

## Prerequisites
Just follow this <a href="https://developer.spotify.com/documentation/web-api"> Spotify Api Documentation</a> getting started portion

Before running the __init_.py, make sure you have the necessary prerequisites installed.

Update the .env file
```bash
#.env file
SPOTIPY_CLIENT_ID="your spotify client id"
SPOTIPY_CLIENT_SECRET="your spotify client secret"
SPOTIPY_REDIRECT_URI=" your redirect uri"
#Spotify Scope
scope = "user-library-read"
```

```bash
# Install required Python packages
poetry install

```

Exporting Songs
The script allows you to export the list of songs to a JSON file (output.json). The exported file will contain a formatted list of songs with artist names and track names.

Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.
