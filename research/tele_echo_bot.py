import logging
from aiogram import Bot, Dispatcher,executor,types
from dotenv import load_dotenv
import os

load_dotenv()
API_TOKEN = os.getenv("TOKEN")
#print(API_TOKEN)

#config logging
logging.basicConfig(level=logging.INFO)

# Initialize bot  and dispatcher
bot = Bot(token = API_TOKEN) 
dp = Dispatcher(bot)  #it will connet my object with telebot token

@dp.message_handler(commands=['start','help']) 
async def command_start_handler(message: types.Message):
    """
    This handler receives messages with `/start` command or `/help` command
    """
    await message.reply("Hi\n I am Echo Bot! \n How can I help you.")

@dp.message_handler(commands=['start','help']) 
async def echo(message: types.Message):
    """
    This will return echo
    """
    await message.answer(message.text)

if __name__ == "_main_":
    executor.start_polling(dp, skip_updates=True)
