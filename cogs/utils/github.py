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
    headers = {
        "Accept": "application/vnd.github.v3.text+json",
    }

    response = requests.get(
        "https://api.github.com/repos/liner-exe/discord-commands-bot/releases/latest",
        headers=headers,
    )

    if not response.ok:
        return ""

    data = response.json()

    if not data.get("body_text"):
        return "" # Raise there error if needed

    return data["body_text"]
