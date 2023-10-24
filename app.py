import asyncio
import logging

from aiogram import executor

from loader import dp
import middlewares, filters, handlers
from notification import monitor_database
from utils.notify_admins import on_startup_notify, send_stop_notification
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)

async def on_shutdown_notify(dispatcher):
    await send_stop_notification(dispatcher)
    await dp.storage.close()
    await dp.storage.wait_closed()
    await dp.bot.session.close()
    asyncio.get_event_loop().stop()
async def main():
    # Schedule the monitor_database function to run every 5 minutes
    while True:
        logging.exception("Enter timer...")
        await monitor_database()
        await asyncio.sleep(10)

if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)  # Set the desired logging level
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown_notify)
    loop.run_forever()

