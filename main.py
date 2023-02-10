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
import shutil

def main():
    load_dotenv()
    nasa_token = os.environ["NASA_TOKEN"]
    telegram_token = os.environ["TELEGRAM_TOKEN"]
    bot = telegram.Bot(token=telegram_token)
    sleep_time = int(os.environ["SLEEP_TIME"])
    images_spacex_path = Path('images/')
    images_nasa_path = Path('nasa/')
    chat_id = os.environ["TELEGRAM_CHAT_ID"]

    while True:
        count = 2
        apod_nasa.fetch_nasa_best_images(nasa_token, count)
        count = 3
        epic_nasa.fetch_nasa_earth(nasa_token, count)
        fsi.fetch_spacex_last_launch()

        if not sleep_time:
            sleep_time = 60 * 60 * 4  # 4 часа
            while True:
                re_send_telegram_images(bot, chat_id, images_nasa_path)
                re_send_telegram_images(bot, chat_id, images_spacex_path)
                print('Отправлены старые файлы повторно')
                time.sleep(sleep_time)

        tb.send_telegram_images(bot, chat_id, images_spacex_path)
        tb.send_telegram_images(bot, chat_id, images_nasa_path)
        print('Сейчас удалятся загруженные файлы, чтобы скачать новые для загрузки')

        try:
            shutil.rmtree(images_spacex_path)
            print("Фото spacex удалены")
        except OSError as error:
            print("Фото spacex не было")
        try:
            shutil.rmtree(images_nasa_path)
            print("Фото NASA удалены")
        except OSError as error:
            print("Фото NASA не было")

        time.sleep(sleep_time)



if __name__ == '__main__':
    main()