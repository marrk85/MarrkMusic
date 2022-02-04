import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/0f0a1d2c1b36bcbda89de.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━
🖤 ʜᴇʏ, ɪ ᴀᴍ sᴜᴘᴇʀ ғᴀsᴛ ᴠᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs...
ᴀʟʟ ᴏꜰ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /
┏━━━━━━━━━━━━━━━━━┓
┣★ ᴄʀᴇᴀᴛᴏʀ : [.|ɪʀᴏɴ|🇮🇳|♡|.](t.me/marrk85)
┗━━━━━━━━━━━━━━━━━┛

🖤 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ [ᴏᴡɴᴇʀ](t.me/marrk85) ʙᴀʙʏ...
━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ​", url="https://t.me/Aaina_music_bot?startgroup=true")
                  ],[
                    InlineKeyboardButton(
                        "ᴜᴘᴅᴀᴛᴇ'ꜱ", url="https://t.me/marrkchannel"
                    ),
                    InlineKeyboardButton(
                        "sᴜᴘᴘᴏʀᴛ", url="https://t.me/marrkmusic"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "🖤ᴀᴀɪɴᴀ ᴄʜᴀɴɴᴇʟ🖤​", url="https://t.me/Aaina_Op"
                    )]
            ]
       ),
    )

@Client.on_message(command(["ping"]) & filters.group & ~filters.edited & ~filters.private)

async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/3106344e011c60d0039ab.jpg",
        caption=f"""ɪ ᴀᴍ ᴀʟɪᴠᴇ ʙᴀʙʏ !🖤""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/marrkmusic")
                ]
            ]
        ),
    )
