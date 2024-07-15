import requests

def get_latest():
    response = requests.get("https://raw.githubusercontent.com/r-liner/discord-commands-bot/master/version.txt")
    return response.text

def check_for_updates(version):
    latest = get_latest()
    if latest > version:
        return True
    
    return False

def changelog():
    # Use text media_type: https://docs.github.com/en/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types
    headers = {
        "Accept": "application/vnd.github.v3.text+json",
    }

    response = requests.get(
        "https://api.github.com/repos/liner-exe/discord-commands-bot/releases/latest",
        headers=headers,
    )

    response.raise_for_status()

    if not response.get("body"):
        return "" # Raise there error if needed

    return response["body"]
