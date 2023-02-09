import telegram
from dotenv import load_dotenv
import os
from pathlib import Path
import random
import time


def send_telegram_images(bot, chat_id, images_spacex_path, images_nasa_path):
    # bot.send_message(chat_id=chat_id, text="лалалалала")
    for root, directory, files in os.walk(images_nasa_path):
        random.shuffle(files)
        for file in files:
            bot.sendPhoto(chat_id=chat_id, photo=open(f'{images_nasa_path}/{file}', 'rb'),)
    for root, directory, files in os.walk(images_spacex_path):
        random.shuffle(files)
        for file in files:
            bot.sendPhoto(chat_id=chat_id, photo=open(f'{images_spacex_path}/{file}', 'rb'),)


def main():
    images_spacex_path = Path('images/')
    images_nasa_path = Path('nasa/')
    load_dotenv()
    TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    sleep_time = int(os.environ["SLEEP_TIME"])
    if not sleep_time:
        sleep_time = str(60 * 60 * 4)  # 4 часа
    while True:
        send_telegram_images(bot, chat_id, images_spacex_path, images_nasa_path)
        time.sleep(sleep_time)


if __name__ == '__main__':
    main()