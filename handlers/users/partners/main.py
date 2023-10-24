from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from handlers.users.start import checkUser
from keyboards.inline.inlineBnt import createOrdersBtns
from sheet import *
from loader import dp

ITEMS_PER_PAGE = 5

# Current page
data = []
current_page = 0

@dp.message_handler(text="⬅️ Orqaga")
async def bot_echo(message: types.Message, state: FSMContext):
    await checkUser(message)