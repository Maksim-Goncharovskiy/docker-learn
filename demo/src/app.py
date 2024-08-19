import requests

response = requests.get("https://google.com")

if response.status_code == 200:
    print("Hello google! And docker of course :)")