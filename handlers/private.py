import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/dfb645bbd6b7ea1540f92.jpg",
        caption=f"""**✰ʜᴇʟʟᴏ... , 
ᴍʏ ɴᴀᴍᴇ ɪs {BOT_NAME}.
ᴀ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴜsɪᴄ sᴛʀᴇᴀᴍɪɴɢ ʙᴏᴛ
ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ: /
➖➖➖➖➖➖➖➖➖➖➖➖➖
✰ ᴍᴀɴᴀɢᴇᴅ ʙʏ:- [✰ ɪʀᴏɴ ✰](https://t.me/marrk85)
➖➖➖➖➖➖➖➖➖➖➖➖➖**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "♪ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ​ ♪", url="https://t.me/Marrk_music_bot?startgroup=true")
                  ],[
                    InlineKeyboardButton(
                        "♪ ᴜᴘᴅᴀᴛᴇ'ꜱ ♪", url="https://t.me/marrkchannel"
                    ),
                    InlineKeyboardButton(
                        "♪ sᴜᴘᴘᴏʀᴛ ♪", url="https://t.me/marrkmusic"
                    )
                ],
            ]
       ),
    )

@Client.on_message(command(["ping"]) & filters.group & ~filters.edited & ~filters.private)

async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/dfb645bbd6b7ea1540f92.jpg",
        caption=f"""ɪ ᴀᴍ ᴀʟɪᴠᴇ ʙᴀʙʏ 🖤""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "♪ sᴜᴘᴘᴏʀᴛ ♪", url=f"https://t.me/marrkmusic")
                ]
            ]
        ),
    )
