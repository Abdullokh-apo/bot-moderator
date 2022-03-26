from aiogram import types
from dispatcher import dp, GROUP_ID


@dp.message_handler(is_admin=True, commands=['ban'], commands_prefix='!/')
async def ban_by_admin(message: types.Message):
    if not message.reply_to_message:
        await message.reply('Эта команда должна быть ответом на сообщение.')
        return
    await message.bot.delete_message(chat_id=GROUP_ID,
                                     message_id=message.message_id)
    await message.bot.kick_chat_member(chat_id=GROUP_ID,
                                       user_id=message.reply_to_message.
                                       from_user.id)
