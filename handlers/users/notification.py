import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode

from loader import bot
from sheet import find_orders, add_row, getData, getData1

USER_ID = 5333351384

async def send_notification(user_id, message_text):
    try:
        await bot.send_message(user_id, message_text, parse_mode=ParseMode.MARKDOWN)
    except Exception as e:
        logging.exception(e)

# Monitor the database for new entries
async def monitor_database():
    data = await getData1(value_to_find=1, cur=52, table="🏢 Hamkor-do'konlar")
    print(data)
    logging.exception("Sending...")
    if data:
        text = f"""
Hamkorga xabar boradi: “🥳 Tabriklaymiz! Sizga hamkorlik uchun ruxsat berildi. Botning to’liq imkoniyatlaridan foydalanishingiz mumkin!

👤 Siz uchun biriktirilgan menejer:
Menejer: Zikrulloh Ikromov
Telefon raqam: 991707849
Telegram: @ikromoffjr

😉 Savollar bo’lsa, menejeringizga murojaat qilishingiz mumkin!”
"""
        await send_notification(data[0][5], text)
        await add_row([["BA", int(data[0][0]) + 3, 0]], table="🏢 Hamkor-do'konlar")
        logging.exception("Sended")
    else:
        logging.exception("Nothing to send")

