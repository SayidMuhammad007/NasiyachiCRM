import asyncio
import logging

from aiogram import executor
import datetime
from loader import dp
import middlewares, filters, handlers
from notification import monitor_database, send_notification
from sheet import checkStatus, getAll
from utils.notify_admins import on_startup_notify, send_stop_notification
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)

async def sendNotification():
    data = await checkStatus()
    print("ads",data)
    if len(data) > 1:
        for i in data:
            if len(i) > 77:
                parsed_time = datetime.datetime.strptime(i[77], "%H:%M:%S").time()
                current_datetime = datetime.datetime.now().time()
                print("current", current_datetime)
                print("time", i[77])
                print("parsed", parsed_time)

                # Convert time objects to datetime objects
                current_datetime = datetime.datetime.combine(datetime.date.today(), current_datetime)
                parsed_datetime = datetime.datetime.combine(datetime.date.today(), parsed_time)

                time_difference = current_datetime - parsed_datetime
                print("diff", time_difference)

                # Calculate minutes from timedelta
                minutes_difference = int(time_difference.total_seconds() // 60)
                print("minutes_difference", minutes_difference)

                users = await getAll("👥 Xodimlar")
                for j in users:
                    await send_notification(user_id=j[4], message_text=f"<b>‼️ Buyurtmani qabul qiling! {minutes_difference} daqiqadan buyon mijoz kutyapti!</b>")

async def on_shutdown_notify(dispatcher):
    # await send_stop_notification(dispatcher)
    await dp.storage.close()
    await dp.storage.wait_closed()
    await dp.bot.session.close()
    asyncio.get_event_loop().stop()
async def main():
    # Schedule the monitor_database function to run every 5 minutes
    while True:
        logging.exception("Enter timer...")
        await sendNotification()
        # await monitor_database()
        await asyncio.sleep(300)

if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)  # Set the desired logging level
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown_notify)
    loop.run_forever()

