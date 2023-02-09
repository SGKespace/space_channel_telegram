import telegram
from dotenv import load_dotenv
import os
from pathlib import Path


def main(bot, chat_id, images_spacex_path, images_nasa_path):
    bot.send_message(chat_id=chat_id, text="лалалалала")
    for root, directory, files in os.walk(images_nasa_path):
        for file in files:
            bot.sendPhoto(chat_id=chat_id, photo=open(f'{images_nasa_path}/{file}', 'rb'),)


if __name__ == '__main__':
    images_spacex_path = Path('images/')
    images_nasa_path = Path('nasa/')
    load_dotenv()
    TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    main(bot, chat_id, images_spacex_path, images_nasa_path)