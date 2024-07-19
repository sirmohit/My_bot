import logging
from aiogram import Bot, Dispatcher,types
from dotenv import load_dotenv
import asyncio
from aiogram.types import ParseMode
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

@dp.message_handler() 
async def clear(message: types.Message):
    """
    A will return echo.
    """

    await message.answer(message.text)

async def main():
    # Start polling
    await dp.start_polling()
"""
if __name__ == "_main_":
   executor.start_polling(dp, skip_updates=True)
"""
if __name__ == '__main__':
    # Run the main function in the asyncio event loop
    asyncio.run(main())
    
    
