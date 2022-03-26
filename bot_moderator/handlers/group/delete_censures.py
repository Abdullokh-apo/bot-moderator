from contextlib import suppress
from aiogram import types
from aiogram.utils.exceptions import MessageToDeleteNotFound
from dispatcher import dp
from censure.censure import all


@dp.message_handler()
async def del_msg(message: types.Message):
    for censure in all:
        if censure in str(message.text).lower():
            with suppress(MessageToDeleteNotFound):
                await message.delete()
                print('message was deleted')
