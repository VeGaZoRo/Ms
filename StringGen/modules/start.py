from pyrogram import filters
from pyrogram.types import Message
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from StringGen import Anony
from pyrogram import Client
from StringGen.utils import add_served_user, keyboard
import asyncio

import os
import time
from pyrogram import filters
import random
from pyrogram import Client


@Anony.on_message(filters.command("start") & filters.private & filters.incoming)
async def f_start(_, message: Message):
    await message.reply_photo(
        photo="https://telegra.ph/file/ce276acf3d3895a712914.jpg",
        caption=f"<b>⭓ᴍᴜˢɪᴄ✘ᴠᴇɢᴀ♪\n╮⦿ مرحباً بك عزيزي : {message.from_user.first_name}\n╯⦿ اسمي : {Anony.mention}\n╮⦿ تم صنعي من قبل فـيـجا\n╯⦿ اعمل علي استخراج جلسات</b>",
        reply_markup=keyboard,
    )
    await add_served_user(message.from_user.id)
    
    
    
    
