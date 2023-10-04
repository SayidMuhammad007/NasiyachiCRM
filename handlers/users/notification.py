import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode

from loader import bot
from sheet import find_orders, add_row

USER_ID = 5333351384

async def send_notification(user_id, message_text):
    try:
        await bot.send_message(user_id, message_text, parse_mode=ParseMode.MARKDOWN)
    except Exception as e:
        logging.exception(e)

# Monitor the database for new entries
async def monitor_database():
    while True:
        print("s")
        new_entry = await find_orders(0, 79, "📒 Buyurtmalar", user_id=None)
        if new_entry:
            for i in new_entry[0]:
                print(i)
                status = "#YANGI_BUYURTMA"
                msg = f"""
                {status}

                👤 Mijoz ma’lumotlari:

                Mijoz familiya, ism va sharifi: <b>{i[7]}</b>
                Mijoz yoshi: <b>{i[15]}</b>
                🏢 Do’kon ma’lumotlari:

                Buyurtmachi do’kon: <b>{i[21]}</b>
                ℹ️ Buyurtma ma’lumotlari:

                Buyurtma sanasi:<b>{i[4]}</b>
                Buyurtma vaqti: 
                    """
                await send_notification(USER_ID, msg)
                await add_row([["CB", 79, 1]])
        # You can add a sleep or polling mechanism here to check for new entries periodically
