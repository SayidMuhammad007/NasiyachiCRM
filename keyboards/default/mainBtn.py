from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, \
    InlineKeyboardMarkup

from sheet import getData

menuBtn = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='📋 Buyurtmalar'),
            KeyboardButton(text='💲 Daromadim')
        ],
        [
            KeyboardButton(text="➕ Yangi buyurtma"),
            KeyboardButton(text="🛒 Buyurtmalar")
        ],
        [
            KeyboardButton(text="🤝 Hamkorlar bo’limi"),
            KeyboardButton(text="💰 Moliya bo’limi")
        ]
    ],
    resize_keyboard=True
)

adminBtn = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='📋 Buyurtmalar'),
            KeyboardButton(text='💲 Daromadim')
        ],
        [
            KeyboardButton(text="➕ Yangi buyurtma"),
            KeyboardButton(text="🛒 Buyurtmalar")
        ],
        [
            KeyboardButton(text="🤝 Hamkorlar bo’limi"),
            KeyboardButton(text="💰 Moliya bo’limi")
        ],
        [
            KeyboardButton(text="🚻 HR bo’limi"),
            KeyboardButton(text="➕ Yangi hamkor")
        ]
    ],
    resize_keyboard=True
)



PayBtn = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='📄 To’lovlar'),
        ],
        [
            KeyboardButton(text="⬅️ Orqaga")
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

async def cancel(data, id):
    keyboard = InlineKeyboardMarkup(row_width=1)
    for item in data:
        if len(item) > 115 and item[115]:
            button_text = item[115]
            button = InlineKeyboardButton(text=button_text, callback_data=f"cancelReason_{button_text}_{id}")
            keyboard.insert(button)
    button = InlineKeyboardButton(text="◀️ Orqaga", callback_data=f"cancelCancel_{id}")
    keyboard.insert(button)
    return keyboard


async def payments(data):
    keyboard = InlineKeyboardMarkup(row_width=1)

    for item in data:
        button_text = ""

        if len(item) > 84:
            if item[84]:
                button_text = item[84]
            elif item[85]:
                button_text = item[85]

            if button_text:
                # Ensure that callback_data adheres to Telegram API specifications
                callback_data = f"select_{button_text}"  # Trim to a reasonable length

                button = InlineKeyboardButton(text=button_text, callback_data=callback_data)
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

def confirmBtn0(id):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Tasdiqlash✅", callback_data=f"truePartner_{id}"),
                InlineKeyboardButton(text="Bekor qilish❌", callback_data=f"falsePartner_{id}")

            ],
        ],
        row_width=2
    )
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

partnerMenu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='📋 Barchasi'),
            KeyboardButton(text="🆕 Yangi do'kon!")
        ],
        [
            KeyboardButton(text="🟡 Qabul qilindi!"),
            KeyboardButton(text="📔 O'quv jarayonida!")
        ],
        [
            KeyboardButton(text="✅ Hamkorlikda!"),
            KeyboardButton(text="❌ Bloklandi!")
        ],
        [
            KeyboardButton(text="⬅️ Orqaga")
        ]
    ],
    resize_keyboard=True
)