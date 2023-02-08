import requests
from pathlib import Path
import urllib
import os
from dotenv import load_dotenv
from datetime import datetime
import common_helper_functions as chf
import fetch_spacex_images as fsi
import fetch_epic_nasa_images as epic_nasa
import fetch_apod_nasa_images as apod_nasa


def main():
    load_dotenv()
    nasa_token = os.environ["NASA_TOKEN"]
    apod_nasa.fetch_nasa_best_image(nasa_token, 2)  # грузим 2 лучших картинки случайным образом
    epic_nasa.fetch_nasa_earth(nasa_token, 3)  # грузим 3  картинки
    launche_id = ''
    fsi.fetch_spacex_last_launch(launche_id)


if __name__ == '__main__':
    main()