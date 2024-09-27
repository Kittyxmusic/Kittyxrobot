import asyncio
from platform import python_version as pyver
from datetime import datetime  # To track start time and calculate uptime

from pyrogram import __version__ as pver
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as lver
from telethon import __version__ as tver

from MukeshRobot import SUPPORT_CHAT, pbot, BOT_USERNAME, OWNER_ID, BOT_NAME, START_IMG

# Store the bot start time
START_TIME = datetime.now()

MISHI = "https://envs.sh/STz.jpg"  # Use a single image URL

Mukesh = [
    [
        InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇ", url=f"https://t.me/kittyxupdates"),
        InlineKeyboardButton(text="ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
    ],
    [
        InlineKeyboardButton(
            text="˹🕸️ ᴛᴧᴘ тᴏ sᴇᴇ ᴍᴧɢɪᴄ 🕸️˼",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

# Function to calculate uptime
def get_readable_time():
    now = datetime.now()
    uptime_duration = now - START_TIME
    hours, remainder = divmod(uptime_duration.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{uptime_duration.days}d {hours}h {minutes}m {seconds}s"

@pbot.on_message(filters.command("alive"))
async def restart(client, m: Message):
    await m.delete()
    accha = await m.reply("🐳")
    await asyncio.sleep(0.2)
    await accha.edit("🐋")
    await asyncio.sleep(0.1)
    await accha.edit("💤")
    await asyncio.sleep(0.1)
    await accha.edit("🎉")

    await accha.delete()
    await asyncio.sleep(0.3)
    umm = await m.reply_sticker(
        "CAACAgUAAxkDAAJHbmLuy2NEfrfh6lZSohacEGrVjd5wAAIOBAACl42QVKnra4sdzC_uKQQ"
    )
    await umm.delete()
    await asyncio.sleep(0.2)

    # Get the formatted uptime string
    uptime = get_readable_time()

    # Replace the empty placeholder {} with the message sender's first name
    await m.reply_photo(
        MISHI,  # Use a single image URL from MISHI
        caption=f"""**Hey {m.from_user.first_name}\n\n I am [{BOT_NAME}](t.me/{BOT_USERNAME}) alive and working since {uptime} ✨🥀 \n\n**Made by ➛** [🇲σ᭡፝֟ɳ🌙](https://t.me/about_ur_moonshining/5)""",
        reply_markup=InlineKeyboardMarkup(Mukesh)
    )

__mod_name__ = "ᴀʟɪᴠᴇ"
__help__ = """
 ❍ /alive ➛ ᴄʜᴇᴄᴋ ʙᴏᴛ ᴀʟɪᴠᴇ sᴛᴀᴛᴜs.
 ❍ /ping ➛ ᴄʜᴋ ᴘɪɴɢ sᴛᴀᴛᴜs.
 ❍ /stats : sʜᴏᴡs ᴛʜᴇ ᴏᴠᴇʀᴀʟʟ sᴛᴀᴛs ᴏғ ᴛʜᴇ ʙᴏᴛ.

☆✧....𝐁𝐘🫧 » [☄️𝐌ᴏᴏɴ🌙](https://t.me/Moonshining2)....🥀🥀✧☆
"""
