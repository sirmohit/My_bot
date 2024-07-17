from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher,executor,types
import asyncio
from aiogram.types import ParseMode
import openai
import sys

class Reference:
    '''
    A class to store previously response from the chatGPT API
    '''
    
    def __init__(self) -> None:
        self.response = ""

load_dotenv()
openai.api_key= os.getenv("OPEN_API_KEY")

reference = Reference()

TOKEN = os.getenv('TOKEN')

# MODEL NAME

MODEL_NAME = 'gpt-3.5-turbo'

# initialize bot and dispatcher
bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot)

def clear_past():
    '''
    this function to clear the previous conversion  and context
    '''
    reference.response = ""

@dispatcher.message_handler(commands=['start']) 
async def welcome(message: types.Message):
    """
    This handler receives messages with `/start` command or `/help` command
    """
    await message.reply("Hi\n I am Tele Bot \n Created by Mohit \n How can I assist you?")

@dispatcher.message_handler(commands=['start']) 
async def command_start_handler(message: types.Message):
    """
    This handler receives messages with `/start` command or `/help` command
    """
    await message.reply("Hi\n I am Tele Bot \n Created by Mohit \n How can I assist you?")

@dispatcher.message_handler(commands = ['clear']) 
async def clear(message: types.Message):
    """
    A handler to clear previous conversation and context.
    """
    clear_past()
    await message.answer("I have cleared the past conversation and context.")

@dispatcher.message_handler(commands=['help']) 
async def helper(message: types.Message):
    """
    This handler to display helper menu.
    """
    help_command = '''
    Hi there, I'm chatGPT Telegram Bot created by Mohit! Please follow this commands -
    /start - to start the conversation
    /clear - to clear the past conversation and context.
    /help - to get this help menu.
    I hope this helps. :'''
    await message.reply(help_command)

@dispatcher.message_handler()
async def chatgpt(message:types.message):
    '''A handler to process user's input and generate a resopnse using the chatGPT API.
    '''
    print(f">>>USER:\n\t{message.text}")
    response = openai.ChatCompletion.create(
        model = MODEL_NAME,
        message = [
            {'role' : 'assistant','content':reference.response}, # role assists
            {'role' : 'user', 'content' : message.text} # our query
        ]
    )
    reference.response = response['choices'][0]['message']['content']
    print(f'>>>chatGPT:\n\t{reference.response}')
    await bot.send_message(chat_id = message.chat.id,text = reference.response)




async def main():
    # Start polling
    await dispatcher.start_polling()

if __name__ == '__main__':
    # Run the main function in the asyncio event loop
    asyncio.run(main())
    