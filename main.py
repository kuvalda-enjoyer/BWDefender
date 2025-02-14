import asyncio
from aiogram import Dispatcher
from typing import *
from backend.bot.create import create
from backend.handlers.handlers import router
from backend.classes_states.classes_states import *
from aiogram.fsm.storage.memory import MemoryStorage

bot = create()
storage = MemoryStorage()
dp = Dispatcher(parse_mode="HTML", storage=storage)
dp.include_router(router)

async def main():
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    asyncio.run(main())