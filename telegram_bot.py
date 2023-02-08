import telegram
from dotenv import load_dotenv
import os

load_dotenv()
TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
bot = telegram.Bot(token=TELEGRAM_TOKEN)
bot.send_message(chat_id='@SGK_dvmn', text="лалалалала")