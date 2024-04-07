import configparser

def is_weather_active(func):
    """
    Decorator that checks if an API token for OpenWeather is configured in the 
    application's configuration file. If the token is present, the function is 
    enabled, otherwise it is deactivated.

    Parameters:
        - func: The function to be checked and activated if the API token is present.

    Returns:
        - func if the OpenWeather API token is configured, None otherwise.
    """
    config = configparser.ConfigParser()
    config.read("config.ini")

    if config["weather"]["openweather_token"] != "":
        return func
    else:
        pass
