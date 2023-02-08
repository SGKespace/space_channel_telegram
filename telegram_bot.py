import telegram
from dotenv import load_dotenv
import os

load_dotenv()
TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
bot = telegram.Bot(token=TELEGRAM_TOKEN)
print(bot.get_me())