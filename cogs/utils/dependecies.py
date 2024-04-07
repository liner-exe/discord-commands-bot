import subprocess
import sys

def check_installed() -> None:
    """
    Check installation of packages used in project.
    """
    try:
        print("Checking installation of dependecies...")
        import nextcord
        import asyncio
        import typing_extensions
        import psutil
        import requests
        print("All dependencies are installed!")

    except ImportError as e:
        print(f"Some of dependencies are missing: {e}")
        print("Installing missing dependecies...")
        subprocess.call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("All dependecies installed succesfully!")