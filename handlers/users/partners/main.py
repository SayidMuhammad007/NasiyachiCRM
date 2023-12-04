from aiogram import types
from aiogram.dispatcher import FSMContext

from handlers.users.start import checkUser as check
from loader import dp

ITEMS_PER_PAGE = 5

# Current page
data = []
current_page = 0

@dp.message_handler(text="⬅️ Orqaga")
async def bot_echo(message: types.Message, state: FSMContext):
    await check(message)