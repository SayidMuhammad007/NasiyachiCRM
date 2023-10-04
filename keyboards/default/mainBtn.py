from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

from sheet import getData

menuBtn = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='📋 Buyurtmalar'),
            KeyboardButton(text='💲 Daromadim')
        ],
        [
            KeyboardButton(text="➕ Yangi buyurtma")
        ]
    ],
    resize_keyboard=True
)

async def markets(data):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    for item in data:
        if len(item) > 28 and item[28]:
            button_text = item[28]
            button = KeyboardButton(text=button_text)
            keyboard.insert(button)
    return keyboard

def confirmBtn():
    keyboard = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="Tasdiqlash✅", callback_data=f"true")
        ],
        [
            KeyboardButton(text="Bekor qilish❌", callback_data=f"false")
        ]
    ], row_width=2, resize_keyboard=True)
    return keyboard

def confirmBtn2():
    keyboard = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="⚪ ️ RASMIYLASHTIRILDI", callback_data=f"true")
        ],
        [
            KeyboardButton(text="❌ BEKOR QILINDI", callback_data=f"false")
        ]
    ], row_width=2, resize_keyboard=True)
    return keyboard

async def times():
    data = await getData(1, 80, "⚙️ Sozlamalar")
    print(data)
    keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    for i in data:
        keyboard.insert(i[45])
    return keyboard

def CancelBtn():
    keyboard = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="❌ Bekor qilish")
        ]
    ], row_width=2, resize_keyboard=True)
    return keyboard