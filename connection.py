import base64
import requests

client_id= "b0201acd74ba40d9bfc01668802d237b"
client_secret= "c878abf0522b4372a4edbad6ae50a608"

client_creds = f"{client_id}:{client_secret}"

client_creds_b64 = base64.b64encode(client_creds.encode())
type(client_creds_b64)

token_url = "https://accounts.spotify.com/api/token"
method = "POST"
token_data = {
    "grant_type": "client_credentials"
}
token_headers = {
    "Authorization": f"Basic {client_creds_b64.decode()}" # <base64 encoded client_id:client_secret>
}

r = requests.post(token_url, data=token_data, headers=token_headers)
print(r.json())
valid_request = r.status_code in range(200, 299)