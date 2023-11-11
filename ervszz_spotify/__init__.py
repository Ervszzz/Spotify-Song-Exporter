from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
import spotipy
import json

# Load environment variables from the .env file
load_dotenv()

# Access the environment variables
SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')
scope = os.getenv('scope')

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# Use the credentials in your code

songs_to_download = []  # initially will be converted into an empty list


def fetch_and_process_songs(offset=0, batch_size=50):
    while True:
        # Retrieve user-saved tracks from Spotify
        song_results = sp.current_user_saved_tracks(batch_size, offset)

        # Break the loop if no more tracks are returned
        if len(song_results['items']) == 0:
            break

        # Process each track in the current batch
        for item in song_results['items']:
            track = item['track']
            formatted_song_desc = f"{track['artists'][0]['name']} – {track['name']}"
            songs_to_download.append(formatted_song_desc)

        # Update the offset for the next batch
        offset += len(song_results['items'])

    return offset


def ask_user_to_export():
    accepted_characters = {'y', 'Y', 'n', 'N'}  # Use curly braces for a set
    while True:
        response = input("Do you want to export the file? [y/n]: ")
        if response in accepted_characters:
            # call the export function
            export_songs_to_file()
            break
        else:
            print("Invalid response! Try again")

def export_songs_to_file():
    print("Exporting Files")
    formatted_song_to_download = [info.replace('\u2013', '-') for info in songs_to_download]

    with open('output.json', 'w') as json_file:
        json.dump(formatted_song_to_download, json_file)

    print("Output has been written to 'output.json'.")

# Fetch and process the initial batch
starting_offset = fetch_and_process_songs()

# Fetch and process the rest of the songs
starting_offset = fetch_and_process_songs(starting_offset)

# Display the final list of songs to download
print("Final Songs to Download:")
print("\n".join(songs_to_download))
print("==========================")
print(f"Total number of songs: {len(songs_to_download)}")

ask_user_to_export()
