from aiogram import executor
from datetime import datetime, timedelta
from handlers.users.notification import monitor_database
from loader import dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
import threading
async def on_startup(dispatcher):
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)
    # scheduler = AsyncIOScheduler(timezone="Asia/Tashkent")
    # scheduler.add_job(await monitor_database(), trigger="date", run_date=datetime.now() + timedelta(seconds=60))
    # scheduler.start()

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)