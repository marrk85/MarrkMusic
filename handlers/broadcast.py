import asyncio

from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant

from callsmusic.callsmusic import client as Marrk
from config import SUDO_USERS

@app.on_message(filters.command("broadcast") & filters.user(SUDOERS))async def broadcast_message(_, message): if not message.reply_to_message: pass else : x = message.reply_to_message.message_id y = message.chat.id sent = 0 pin = 0 chats = [] schats = await get_served_chats() for chat in schats: chats.append(int(chat["chat_id"])) for i in chats: try: m = await app.forward_messages(i, y, x) try: await m.pin(disable_notification=False) pin += 1 except Exception: pass await asyncio.sleep(.3) sent += 1 except Exception: pass await message.reply_text(f"sᴛᴀʀᴛɪɴɢ ʙʀᴏᴀᴅᴄᴀsᴛ ɪɴ {sent} ᴄʜᴀᴛs ᴡɪᴛʜ {pin} ᴘɪɴs ʙᴀʙʏ.") return if len(message.command) < 2: await message.reply_text("Usage:\n/broadcast [MESSAGE]") return text = message.text.split(None, 1)[1] sent = 0 pin = 0 chats = [] schats = await get_served_chats() for chat in schats: chats.append(int(chat["chat_id"])) for i in chats: try: m = await app.send_message(i, text=text) try: await m.pin(disable_notification=False) pin += 1 except Exception: pass await asyncio.sleep(.3) sent += 1 except Exception: pass await message.reply_text(f"sᴛᴀʀᴛɪɴɢ ʙʀᴏᴀᴅᴄᴀsᴛ ɪɴ {sent} ᴄʜᴀᴛs ᴡɪᴛʜ {pin} ᴘɪɴs ʙᴀʙʏ.")
