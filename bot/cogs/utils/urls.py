import urllib

def url_encode(text):
    encoded_text = urllib.parse.urlencode(text)
    return encoded_text