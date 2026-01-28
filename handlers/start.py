from aiogram import Router,types
from aiogram.filters import Command
import asyncio
from db_queries.queries_registration import insert_user



router = Router()

@router.message(Command('start'))
async def start_command(message: types.Message):
    await message.answer(text =f"Salom, {message.from_user.first_name}")
    await asyncio.to_thread(insert_user)