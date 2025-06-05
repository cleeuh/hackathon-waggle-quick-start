import sage_data_client
import requests
from requests.auth import HTTPBasicAuth
import os


def fetch_waggle_image(url, username, password):
    try:
        auth = HTTPBasicAuth(username, password)
        response = requests.get(url, auth=auth)
        if response.status_code == 200:
            content_type = 'image'
            file_extension = os.path.splitext(url)[1].lower()

            if 'image' in content_type or file_extension in {'.jpg', '.jpeg', '.png', '.gif'}:
                return response.content
            else:
                print("The URL does not contain a valid image.")
        else:
            print(f"Failed to fetch the image. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    
    return None

df = sage_data_client.query(
    start="2025-03-06T07:00:00.000Z",
    end="2025-03-07T07:00:00.000Z", 
    filter={
        "vsn": "W069",
        "task": "imagesampler-bottom"
    }
)

# Image URL at column value of first row
image_url       = df.iloc[0]["value"]
image_content   = fetch_waggle_image(image_url, "YOUR_USERNAME", "YOUR_ACCESS_TOKEN")

with open('./downloaded_image.jpg', 'wb') as file:
    file.write(image_content)