import logging
from aiogram.types import ParseMode

from loader import bot
from sheet import getData1, getAll, add_row

USER_ID = 5333351384

from aiogram.utils.exceptions import ChatNotFound

async def send_notification(user_id, message_text):
    try:
        await bot.send_message(user_id, message_text, parse_mode=ParseMode.HTML)
    except ChatNotFound:
        logging.warning(f"Chat not found for user_id: {user_id}")
    except Exception as e:
        logging.exception(e)

# Monitor the database for new entries
async def monitor_database():
    try:
        data = await getData1(value_to_find=5, cur=52, table="🏢 Hamkor-do'konlar")
        print(data)
        logging.exception("Sending...")
        if data:
            print(len(data[0]))
            users = await getAll("👥 Xodimlar")
            for i in users:
                text = f"""
🔥 <b>Yangi hamkor keldi yoki soqqani bosish vaqti</b>!

😎 Hamkorni tasdiqlab yuborilar hamkasblar!
                """
                await send_notification(i[4], text)
                await add_row([["BA", int(data[0][0]) + 3, 0]], table="🏢 Hamkor-do'konlar")
                logging.exception("Sended")
            else:
                logging.exception("Nothing to send")
    except Exception as e:
        logging.exception(e)

