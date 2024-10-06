import requests
import json

def generate_random_color():
    url = "http://colormind.io/api/"
    data = {"model": "default"}

    response = requests.post(url, json=data)

    result = json.loads(response.text)
    colors = result['result']

    return colors[0]

def hex_to_rgb(hex_color):
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return [r, g, b]

def rgb_to_hex(rgb_color):
    hex_value = ""
    for component in rgb_color:
        hex_component = hex(component)[2:].zfill(2)
        hex_value += hex_component

    return hex_value.upper()

def rgb_to_hex_color(rgb_color):
    hex_value = ""
    for component in rgb_color:
        hex_component = hex(component)[2:].zfill(2)
        hex_value += hex_component

    return int(hex_value, 16)