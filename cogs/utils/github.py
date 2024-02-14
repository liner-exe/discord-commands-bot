import requests
from bs4 import BeautifulSoup

def get_latest():
    response = requests.get("https://raw.githubusercontent.com/r-liner/discord-commands-bot/master/version.txt")
    return response.text

def check_for_updates(version):
    latest = get_latest()
    if latest > version:
        return True
    
    return False

def changelog():
    latest = get_latest()
    response = requests.get(f"https://github.com/r-liner/discord-commands-bot/releases/tag/v{latest}")
    soup = BeautifulSoup(response.text, "html.parser")
    _changelog = soup.find("div", class_="markdown-body my-3").get_text()

    return _changelog