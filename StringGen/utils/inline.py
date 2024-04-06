from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHANNEL





keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ", callback_data="gensession")],
        [
            InlineKeyboardButton(text="ᴢҽꝛօ", url=f"https://t.me/TopVeGa"),
            InlineKeyboardButton(text="ᴢօꝛօ", url="https://t.me/ToxVeGa"),
        ],
        [InlineKeyboardButton(text="ᴠᴇɢᴧ", url="https://t.me/VeGaOne")],
    ]
)

gen_key = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="ᴩʏʀᴏɢʀᴀᴍ v1", callback_data="pyrogram1"),
            InlineKeyboardButton(text="ᴩʏʀᴏɢʀᴀᴍ v2", callback_data="pyrogram"),
        ],
        [InlineKeyboardButton(text="ᴛᴇʟᴇᴛʜᴏɴ", callback_data="telethon")],
    ]
)

retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="ᴛʀʏ ᴀɢᴀɪɴ", callback_data="gensession")]]
)
