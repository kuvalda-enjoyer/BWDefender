from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters.command import Command

router = Router()

@router.message(F.text, Command("start"))
async def start(message: Message):
    await message.answer("Привет, это тестовый бот BWDefender, он пока не работает((")

@router.message(F.text)
async def echo(message: Message):
    await message.answer(str(message.from_user).replace(' ', '\n'))