import requests
from datetime import datetime

# Get your token by registering at https://pixe.la/v1/users (see step 1 below)
PIXELA_TOKEN = "your-token-here"
PIXELA_USERNAME = "your-username-here"
GRAPH_ID = "graph1"

USERS_ENDPOINT = "https://pixe.la/v1/users"
GRAPHS_ENDPOINT = f"{USERS_ENDPOINT}/{PIXELA_USERNAME}/graphs"
PIXEL_ENDPOINT = f"{GRAPHS_ENDPOINT}/{GRAPH_ID}"

auth_headers = {
    "X-USER-TOKEN": PIXELA_TOKEN,
}

# 1. Create account (run once)
user_payload = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=USERS_ENDPOINT, json=user_payload)
# print(response.text)

# 2. Create graph (run once)
graph_payload = {
    "id": GRAPH_ID,
    "name": "Programming",
    "unit": "hours",
    "type": "float",
    "color": "sora",
}
# response = requests.post(url=GRAPHS_ENDPOINT, json=graph_payload, headers=auth_headers)
# print(response.text)

# 3. Post today's pixel (run daily)
today = datetime.now().strftime("%Y%m%d")
pixel_payload = {
    "date": today,
    "quantity": "2.5",
}
# response = requests.post(url=PIXEL_ENDPOINT, json=pixel_payload, headers=auth_headers)
# print(response.text)