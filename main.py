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
    telegram_token = os.environ["TELEGRAM_TOKEN"]
    bot = telegram.Bot(token=telegram_token)
    sleep_time = int(os.environ["SLEEP_TIME"])
    images_path = Path('images/')
    chat_id = os.environ["TELEGRAM_CHAT_ID"]

    count = 10
    apod_nasa.fetch_nasa_best_images(nasa_token, count)
    epic_nasa.fetch_nasa_earth(nasa_token, count)
    fsi.fetch_spacex_last_launch()

    if not sleep_time:
        sleep_time = 60 * 60 * 4  # 4 часа

    while True:
      tb.send_telegram_images(bot, chat_id, images_path)
      time.sleep(sleep_time)


if __name__ == '__main__':
    main()