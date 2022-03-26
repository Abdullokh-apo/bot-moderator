import logging
from aiogram import Bot, Dispatcher, executor, types

from filters.admin import IsAdminFilter

API_TOKEN = '5185115302:AAFpjxwEYAbf_gNg7bUo8G6pNIunH-t6xWw'
GROUP_ID = -1001566770681

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

dp.filters_factory.bind(IsAdminFilter)
