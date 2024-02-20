from aiogram import types

from keyboards.default.mainBtn import PayBtn, payments
from loader import dp
from sheet import getAll, getAllHaveValueOne
from states.payment import PaymenState


# Echo bot
@dp.message_handler(text="💰 Moliya bo’limi")
async def bot_echo(message: types.Message):
    await message.answer(message.text, reply_markup=PayBtn)



ITEMS_PER_PAGE = 5

# Current page
data = []
current_page = 0

# Echo bot
@dp.message_handler(text="🏢 Hamkor-do'konlar")
async def bot_echo(message: types.Message):
    global data
    global current_page

    data = await getAllHaveValueOne("🏢 Hamkor-do'konlar", "A3:CC", 26, 1)
    start_idx = current_page * ITEMS_PER_PAGE
    end_idx = (current_page + 1) * ITEMS_PER_PAGE

    text, markup = generate_message_text(start_idx, end_idx)

    await message.answer(text=text, reply_markup=markup)


@dp.callback_query_handler(lambda callback_query: callback_query.data == 'moliya_1', state=PaymenState.confirming)
async def bot_echo(callback: types.CallbackQuery):
    global data
    global current_page

    data = await getAllHaveValueOne("🏢 Hamkor-do'konlar", "A3:CC", 26, 1)
    start_idx = current_page * ITEMS_PER_PAGE
    end_idx = (current_page + 1) * ITEMS_PER_PAGE

    text, markup = generate_message_text(start_idx, end_idx)

    await callback.message.edit_text(text=text, reply_markup=markup)

@dp.callback_query_handler(lambda c: c.data in ['prev0001', 'next0001'])
async def process_callback(callback_query: types.CallbackQuery):
    global current_page
    global data  # Use the global data variable
    if callback_query.data == 'prev0001':
        current_page = max(0, current_page - 1)
    elif callback_query.data == 'next0001':
        current_page = min(len(data) // ITEMS_PER_PAGE, current_page + 1)
    start_idx = current_page * ITEMS_PER_PAGE
    end_idx = (current_page + 1) * ITEMS_PER_PAGE

    # Generate the message text with order IDs and navigation buttons
    text, markup = generate_message_text(start_idx, end_idx)

    # Edit the message with the updated text and buttons
    await callback_query.message.edit_text(text=text, reply_markup=markup)

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def generate_message_text(start_idx, end_idx):
    global data

    # Check if there is any data to display
    if not data:
        return "🙁 Hozir yangi buyurtmalar yo'q. Iltimos, sal chidab turing!", None

    # Create the message text with order IDs
    t = 0
    for i in range(start_idx, end_idx):
        t += 1
        if t > ITEMS_PER_PAGE or i >= len(data):
            break
    text = f"""
Pastdagi subyekt va obyektlarga to’lov qilish kerak. <b>Bittasini tanlang</b>!
"""

    # Check if there are more pages
    has_previous_page = start_idx > 0
    has_next_page = end_idx < len(data)

    # Create an inline keyboard for navigation
    markup = InlineKeyboardMarkup()
    keyboard = []
    row = []  # Initialize an empty row
    for i in range(start_idx, end_idx):
        if i >= len(data):
            break
        button = InlineKeyboardButton(text=f"{data[i][6]}: {data[i][25]} so`m", callback_data=f"partnerMoney_{data[i][0]}")
        row.append(button)

        # Check if the row has reached the desired width (1 in this case)
        if len(row) == 1:
            keyboard.append(row)  # Add the row to the keyboard
            row = []  # Reset the row

    # If there are any remaining buttons in the row, add them
    if row:
        keyboard.append(row)

    markup.inline_keyboard = keyboard

    # Add "Previous" button if available
    if has_previous_page:
        markup.row(InlineKeyboardButton("⬅️ Oldingilari", callback_data="prev0001"))

    # Add "Next" button if available
    if has_next_page:
        if has_previous_page:
            markup.insert(InlineKeyboardButton("Keyingilari ➡️", callback_data="next0001"))
        else:
            markup.add(InlineKeyboardButton("Keyingilari ➡️", callback_data="next0001"))

    # markup.row(InlineKeyboardButton('🔄 Yangilash', callback_data='refresh0001'))
    return text, markup

def generate_message_text_default(start_idx, end_idx, data):
    # Check if there is any data to display
    if not data:
        return "🙁 Hozir yangi buyurtmalar yo'q. Iltimos, sal chidab turing!", None

    # Create the message text with order IDs
    t = 0
    for i in range(start_idx, end_idx):
        t += 1
        if t > ITEMS_PER_PAGE or i >= len(data):
            break
    text = f"""
Pastdagi subyekt va obyektlarga to’lov qilish kerak. <b>Bittasini tanlang</b>!
"""

    # Check if there are more pages
    has_previous_page = start_idx > 0
    has_next_page = end_idx < len(data)

    # Create an inline keyboard for navigation
    markup = InlineKeyboardMarkup()
    keyboard = []
    row = []  # Initialize an empty row
    for i in range(start_idx, end_idx):
        if i >= len(data):
            break
        button = InlineKeyboardButton(text=f"{data[i][6]}: {data[i][25]} so`m", callback_data=f"partnerMoney_{data[i][0]}")
        row.append(button)

        # Check if the row has reached the desired width (1 in this case)
        if len(row) == 1:
            keyboard.append(row)  # Add the row to the keyboard
            row = []  # Reset the row

    # If there are any remaining buttons in the row, add them
    if row:
        keyboard.append(row)

    markup.inline_keyboard = keyboard

    # Add "Previous" button if available
    if has_previous_page:
        markup.row(InlineKeyboardButton("⬅️ Oldingilari", callback_data="prev0001"))

    # Add "Next" button if available
    if has_next_page:
        if has_previous_page:
            markup.insert(InlineKeyboardButton("Keyingilari ➡️", callback_data="next0001"))
        else:
            markup.add(InlineKeyboardButton("Keyingilari ➡️", callback_data="next0001"))

    # markup.row(InlineKeyboardButton('🔄 Yangilash', callback_data='refresh0001'))
    return text, markup