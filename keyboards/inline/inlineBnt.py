from aiogram.types import  InlineKeyboardButton, InlineKeyboardMarkup

from sheet import *


def menejer():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="👤 Menejer", callback_data="manager", url="http://t.me/ikromoffuzb")]
    ])
    return keyboard

def btn1(id):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="🟡RASMIYLASHTIRILMOQDA", callback_data=f"rasmiy_{id}")
        ],
        [
            InlineKeyboardButton(text="❌BEKOR QILINDI", callback_data=f"cancel_{id}")
        ],
        [
            InlineKeyboardButton(text="⛔️SOTILMADI", callback_data=f"notsell_{id}")
        ]
    ])
    return keyboard

def btn2(id):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="⚪️ RASMIYLASHTIRILDI", callback_data=f"finish_{id}")
        ],
        [
            InlineKeyboardButton(text="❌BEKOR QILINDI", callback_data=f"cancel_{id}")
        ]
    ])
    return keyboard

def btn3(id):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Mijoz bilan bog’lanib bo’lmadi", callback_data=f"cancelStatus1_{id}")
        ],
        [
            InlineKeyboardButton(text="Limit ajratilmadi", callback_data=f"cancelStatus2_{id}")
        ],
        [
            InlineKeyboardButton(text="Mijoz bekor qildi", callback_data=f"cancelStatus3_{id}")
        ],
        [
            InlineKeyboardButton(text="Ma'lumot yetarli emas", callback_data=f"cancelStatus4_{id}")
        ],
        [
            InlineKeyboardButton(text="Aloqa o'rnatilmadi", callback_data=f"cancelStatus5_{id}")
        ],
        [
            InlineKeyboardButton(text="Mavjud bo'lmagan raqam", callback_data=f"cancelStatus6_{id}")
        ]
    ])
    return keyboard


def createOrdersBtns(data, data1):
    status = "#YANGI_BUYURTMA"
    if data1 != None:
        status = "#MENING_BUYURTMAM"
    msg = f"""
{status}

👤 Mijoz ma’lumotlari:

Mijoz familiya, ism va sharifi: <b>{data[7]}</b>
Mijoz yoshi: <b>{data[15]}</b>
🏢 Do’kon ma’lumotlari:

Buyurtmachi do’kon: <b>{data[21]}</b>
ℹ️ Buyurtma ma’lumotlari:

Buyurtma sanasi:<b>{data[4]}</b>
Buyurtma vaqti: 
    """
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Qabul qilish", callback_data=f"orderId_{data[0]}")]
    ])
    return keyboard, msg


def btn4(id):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Narx qimmatlik qildi", callback_data=f"notsellStatus1_{id}")
        ],
        [
            InlineKeyboardButton(text="Yaroqsiz mahsulot", callback_data=f"notsellStatus2_{id}")
        ],
        [
            InlineKeyboardButton(text="Shartlarga to’g’ri kelmadi", callback_data=f"notsellStatus3_{id}")
        ]
    ])
    return keyboard


def RequestBtn():
    btn = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
        [
            InlineKeyboardButton(text="✅Ha", callback_data="confirmYes"),
            InlineKeyboardButton(text="❌Yo`q", callback_data="confirmNo"),
        ]
    ])
    return btn

def Month():
    btn = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
        [
            InlineKeyboardButton(text="3 oy", callback_data="3 oy"),
            InlineKeyboardButton(text="6 oy", callback_data="6 oy"),
        ],
        [
            InlineKeyboardButton(text="12 oy", callback_data="12 oy"),
        ]
    ])
    return btn


def Success():
    btn = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
        [
            InlineKeyboardButton(text="Bajarildi ✅", callback_data="success"),
            InlineKeyboardButton(text="Bekor qilindi ❌", callback_data="failure"),
        ]
    ])
    return btn

