from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.inlineBnt import createOrdersBtns
from sheet import *
from loader import dp

ITEMS_PER_PAGE = 5

# Current page
data = []
current_page = 0

@dp.message_handler(text="🆕 Yangi do'kon!")
async def bot_echo(message: types.Message, state: FSMContext):
    global data  # Use the global data variable
    global current_page

    # Fetch the data from your database using find_orders function
    dataa = await getData2(value_to_find="🆕 Yangi do'kon!", cur=46, table="🏢 Hamkor-do'konlar")
    data = dataa
    # Calculate the start and end index for the current page
    start_idx = current_page * ITEMS_PER_PAGE
    end_idx = (current_page + 1) * ITEMS_PER_PAGE
    text, markup = check(start_idx, end_idx)

    # Check if text is empty before sending a message
    if text:
        await message.answer(text=text, reply_markup=markup)
    else:
        msg = """
🙁 Hozir yangi buyurtmalar yo'q. Iltimos, sal chidab turing!

😉 5 daqiqadan so'ng xabar olsangiz, inshaalloh bu muammoni to'g'rilab qo'yamiz!
        """
        await message.answer(text=msg)

@dp.callback_query_handler(lambda c: c.data in ['prevPartnerNew', 'nextPartnerNew'])
async def process_callback(callback_query: types.CallbackQuery, state: FSMContext):
    global current_page
    global data  # Use the global data variable
    if callback_query.data == 'prevPartnerNew':
        current_page = max(0, current_page - 1)
    elif callback_query.data == 'nextPartnerNew':
        current_page = min(len(data) // ITEMS_PER_PAGE, current_page + 1)
    start_idx = current_page * ITEMS_PER_PAGE
    end_idx = (current_page + 1) * ITEMS_PER_PAGE
    print(f"enxix{end_idx}")
    text, markup = check(start_idx, end_idx)
    print(f'{start_idx} - {end_idx}')
    # Check if text is empty before editing the message
    if text:
        await callback_query.message.edit_text(text=text, reply_markup=markup)

def check(start_idx, end_idx):
    # Check if there are more pages
    has_previous_page = current_page > 0
    has_next_page = end_idx < len(data)

    # Create the message text with order IDs
    text = ""
    t = 0
    print(data)
    for i in range(start_idx, end_idx):
        t += 1
        if t > ITEMS_PER_PAGE or i >= len(data):
            break
        text += f"""
———————————————
• #{data[i][0]}. {data[i][1]}
• {data[i][6]}
• {data[i][10]}
• {data[i][46] if len(data[i]) > 46 and data[i][46] else ""}
"""

    # Create an inline keyboard for navigation
    markup = InlineKeyboardMarkup(row_width=5)

    # Add inline buttons for each order ID
    d = 0
    for i in range(start_idx, end_idx):
        d += 1
        if d > ITEMS_PER_PAGE or i >= len(data):
            break
        if len(data[i]) > 46 and data[i][46] == "🆕 Yangi do'kon!":
            order_id = data[i][0]
            print(order_id)
            callback_data = f"PartnerId_{order_id}"
            markup.insert(InlineKeyboardButton(d, callback_data=callback_data))

    # Add previous and next buttons if available
    if has_previous_page:
        prev_button = InlineKeyboardButton("⬅️ Oldingilari", callback_data="prevPartner")
        markup.add(prev_button)

    if has_next_page:
        next_button = InlineKeyboardButton("Keyingilari ➡️", callback_data="nextPartner")
        if has_previous_page:
            markup.insert(next_button)
        else:
            markup.add(next_button)

    return text, markup
