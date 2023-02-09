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
import telegram_bot as tb
import telegram
import time

def main():
    load_dotenv()
    nasa_token = os.environ["NASA_TOKEN"]
    apod_nasa.fetch_nasa_best_image(nasa_token, 2)  # грузим 2 лучших картинки случайным образом
    epic_nasa.fetch_nasa_earth(nasa_token, 3)  # грузим 3  картинки
    launche_id = ''  # указать id заппуска, если нет, то последний
    fsi.fetch_spacex_last_launch(launche_id)

    images_spacex_path = Path('images/')
    images_nasa_path = Path('nasa/')
    TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    sleep_time = int(os.environ["SLEEP_TIME"])
    if not sleep_time:
        sleep_time = 60 * 60 * 4  # 4 часа
    while True:
        tb.send_telegram_image(bot, chat_id, images_spacex_path, images_nasa_path)
        time.sleep(sleep_time)


if __name__ == '__main__':
    main()