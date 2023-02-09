import telegram
from dotenv import load_dotenv
import os
from pathlib import Path
import random
import time


def send_telegram_images(bot, chat_id, images_path):
    for root, directory, files in os.walk(images_path):
        random.shuffle(files)
        for file in files:
            with open(f'{images_path}/{file}', 'rb') as fi:
                bot.sendPhoto(chat_id=chat_id, photo=fi)


def main():
    images_spacex_path = Path('images/')
    images_nasa_path = Path('nasa/')
    load_dotenv()
    telegram_token = os.environ["TELEGRAM_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]
    bot = telegram.Bot(token=telegram_token)
    sleep_time = int(os.environ["SLEEP_TIME"])
    if not sleep_time:
        sleep_time = str(60 * 60 * 4)  # 4 часа
    while True:
        send_telegram_images(bot, chat_id, images_spacex_path)
        send_telegram_images(bot, chat_id, images_nasa_path)
        time.sleep(sleep_time)


if __name__ == '__main__':
    main()