import connection
import requests

conn = connection.r
token_type = conn.json()['token_type']
access_token = conn.json()['access_token']

def get_artist():

    headers = {
    'Authorization': token_type + " " + access_token,
    }

    response = requests.get('https://api.spotify.com/v1/artists/4Z8W4fKeB5YxbusRsdQVPb', headers=headers)
    print(response.json())

get_artist()

# take a set of songs and organize them into new playlists based on their bpm 

# get a playlist 

# get song tempo 

# add song to new playlist 