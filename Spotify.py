import connection
import requests

conn = connection.r
access_token = 'BQAMxh5jIYAcBjTJ6pfK99cx4XNEYtfxoRWMWiAQ-P_Ekn-o4O48z-AtnJTiDyx13XTUOVqRv1GvuIWm4GZ89JJxwsfTFfnJ2x0OSWkYNVvbFGATqJ4'
token_type = 'Bearer'

def get_artist():

    headers = {
    'Authorization': token_type + " " + access_token,
    }

    response = requests.get('https://api.spotify.com/v1/artists/4Z8W4fKeB5YxbusRsdQVPb', headers=headers)
    print(response.json())

get_artist()

