import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""✰ʜᴇʟʟᴏ... {message.from_user.mention()} , 
ᴍʏ ɴᴀᴍᴇ [{bn}](t.me/{bu}) .
ᴀ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴜsɪᴄ sᴛʀᴇᴀᴍɪɴɢ ʙᴏᴛ
ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ: /
""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "♪ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ​ ♪", url=f"https://t.me/{bu}?startgroup=true"
                  ],[
                    InlineKeyboardButton(
                        "♪ ᴏᴡɴᴇʀ ♪", url=f"https://t.me/{me}"
                    ),
                    InlineKeyboardButton(
                        "♪ sᴜᴘᴘᴏʀᴛ ♪", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                  ],[
                    InlineKeyboardButton(
                        "♪ Mᴀʀᴠᴇʟᴏᴜs ✨🤍 ♪", url=f"https://t.me/love_world135")
                ]
            ]
       ),
    )
