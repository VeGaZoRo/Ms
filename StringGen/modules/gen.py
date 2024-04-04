import asyncio
from pyrogram import Client
from pyrogram import filters
from pyrogram import Client, filters
from oldpyro import Client as Client1
from oldpyro.errors import ApiIdInvalid as ApiIdInvalid1
from oldpyro.errors import PasswordHashInvalid as PasswordHashInvalid1
from oldpyro.errors import PhoneCodeExpired as PhoneCodeExpired1
from oldpyro.errors import PhoneCodeInvalid as PhoneCodeInvalid1
from oldpyro.errors import PhoneNumberInvalid as PhoneNumberInvalid1
from oldpyro.errors import SessionPasswordNeeded as SessionPasswordNeeded1
from pyrogram.errors import (
    ApiIdInvalid,
    FloodWait,
    PasswordHashInvalid,
    PhoneCodeExpired,
    PhoneCodeInvalid,
    PhoneNumberInvalid,
    SessionPasswordNeeded,
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telethon import TelegramClient
from telethon.errors import (
    ApiIdInvalidError,
    PasswordHashInvalidError,
    PhoneCodeExpiredError,
    PhoneCodeInvalidError,
    PhoneNumberInvalidError,
    SessionPasswordNeededError,
)
from telethon.sessions import StringSession
from telethon.tl.functions.channels import JoinChannelRequest
from pyromod.listen.listen import ListenerTimeout

from config import SUPPORT_CHANNEL
from StringGen import Anony
from StringGen.utils import retry_key


async def gen_session(
    message, user_id: int, telethon: bool = False, old_pyro: bool = False
):
    if telethon:
        ty = f"ᴛᴇʟᴇᴛʜᴏɴ"
    elif old_pyro:
        ty = f"ᴩʏʀᴏɢʀᴀᴍ v1"
    else:
        ty = f"ᴩʏʀᴏɢʀᴀᴍ v2"

    await message.reply_text(f"<b>╮⦿ محاولة بدء فيجا بستخراج\n╯⦿ جلسه : {ty} لك</b>")

    try:
        api_id = await Anony.ask(
            identifier=(message.chat.id, user_id, None),
            text="<b>╮⦿ من فضلك عزيزي ارسل\n╯⦿ لي ᴀᴘɪ ɪᴅ الخاص بك</b>",
            filters=filters.text,
            timeout=300,
        )
    except ListenerTimeout:
        return await Anony.send_message(
            user_id,
            "<b>╮⦿ عزيزي لقد نفذ الوقت\n╯⦿ يرجئ اعاده المحاوله</b>.",
            reply_markup=retry_key,
        )

    if await cancelled(api_id):
        return

    try:
        api_id = int(api_id.text)
    except ValueError:
        return await Anony.send_message(
            user_id,
            "» ᴛʜᴇ ᴀᴘɪ ɪᴅ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs ɪɴᴠᴀʟɪᴅ.\n\nᴘʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ ᴀɢᴀɪɴ.",
            reply_markup=retry_key,
        )

    try:
        api_hash = await Anony.ask(
            identifier=(message.chat.id, user_id, None),
            text="<b>╮⦿ من فضلك عزيزي ارسل\n╯⦿ لي ᴀᴘɪ ʜᴀsʜ الخاص بك </b>",
            filters=filters.text,
            timeout=300,
        )
    except ListenerTimeout:
        return await Anony.send_message(
            user_id,
            "<b>╮⦿ عزيزي لقد نفذ الوقت\n╯⦿ يرجئ اعاده المحاوله</b>.",
            reply_markup=retry_key,
        )

    if await cancelled(api_hash):
        return

    api_hash = api_hash.text

    if len(api_hash) < 30:
        return await Anony.send_message(
            user_id,
            "» ᴛʜᴇ ᴀᴘɪ ʜᴀsʜ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs ɪɴᴠᴀʟɪᴅ.\n\nᴘʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ ᴀɢᴀɪɴ.",
            reply_markup=retry_key,
        )

    try:
        phone_number = await Anony.ask(
            identifier=(message.chat.id, user_id, None),
            text="<b>╮⦿  عزيزي من فضلك ارسل رقم الهاتف الخاص بك\n│᚜⦿ برمز الدوله الخاصه بك\n╯⦿ هكذا : +20101236789000 </b>",
            filters=filters.text,
            timeout=300,
        )
    except ListenerTimeout:
        return await Anony.send_message(
            user_id,
            "<b>╮⦿ عزيزي لقد نفذ الوقت\n╯⦿ يرجئ اعاده المحاوله</b>.",
            reply_markup=retry_key,
        )

    if await cancelled(phone_number):
        return
    phone_number = phone_number.text

    await Anony.send_message(user_id, "<b>╮⦿ من فضلك عزيزي\n╯⦿ ارسل كود ᴏᴛᴩ الخاص بك</b>")
    if telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif old_pyro:
        client = Client1(":memory:", api_id=api_id, api_hash=api_hash)
    else:
        client = Client(name="Anony", api_id=api_id, api_hash=api_hash, in_memory=True)
    await client.connect()

    try:
        if telethon:
            code = await client.send_code_request(phone_number)
        else:
            code = await client.send_code(phone_number)
        await asyncio.sleep(1)

    except FloodWait as f:
        return await Anony.send_message(
            user_id,
            f"» ғᴀɪʟᴇᴅ ᴛᴏ sᴇɴᴅ ᴄᴏᴅᴇ ғᴏʀ ʟᴏɢɪɴ.\n\nᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ғᴏʀ {f.value or f.x} sᴇᴄᴏɴᴅs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ.",
            reply_markup=retry_key,
        )
    except (ApiIdInvalid, ApiIdInvalidError, ApiIdInvalid1):
        return await Anony.send_message(
            user_id,
            "» ᴀᴘɪ ɪᴅ ᴏʀ ᴀᴘɪ ʜᴀsʜ ɪs ɪɴᴠᴀʟɪᴅ.\n\nᴘʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.",
            reply_markup=retry_key,
        )
    except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
        return await Anony.send_message(
            user_id,
            "» ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ ɪɴᴠᴀʟɪᴅ.\n\nᴘʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.",
            reply_markup=retry_key,
        )

    try:
        otp = await Anony.ask(
            identifier=(message.chat.id, user_id, None),
            text=f"<b>⭓ᴍᴜˢɪᴄ✘ᴠᴇɢᴀ♪\n╮⦿ تم ارسال كود ᴏᴛᴩ \n│᚜⦿ الي رقم : +201123645178 \n│᚜⦿ تم ارسل كود ᴏᴛᴩ لك هكذا : 12345\n╯⦿ من فضلك ارسله لي هكذا 1 2 3 4 5</b>",
            filters=filters.text,
            timeout=600,
        )
        if await cancelled(otp):
            return
    except ListenerTimeout:
        return await Anony.send_message(
            user_id,
            "<b>╮⦿ عزيزي لقد نفذ الوقت\n╯⦿ يرجئ اعاده المحاوله</b>.",
            reply_markup=retry_key,
        )

    otp = otp.text.replace(" ", "")
    try:
        if telethon:
            await client.sign_in(phone_number, otp, password=None)
        else:
            await client.sign_in(phone_number, code.phone_code_hash, otp)
    except (PhoneCodeInvalid, PhoneCodeInvalidError, PhoneCodeInvalid1):
        return await Anony.send_message(
            user_id,
            "» ᴛʜᴇ ᴏᴛᴩ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs <b>ᴡʀᴏɴɢ.</b>\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.",
            reply_markup=retry_key,
        )
    except (PhoneCodeExpired, PhoneCodeExpiredError, PhoneCodeExpired1):
        return await Anony.send_message(
            user_id,
            "» ᴛʜᴇ ᴏᴛᴩ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs <b>ᴇxᴩɪʀᴇᴅ.</b>\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.",
            reply_markup=retry_key,
        )
    except (SessionPasswordNeeded, SessionPasswordNeededError, SessionPasswordNeeded1):
        try:
            pwd = await Anony.ask(
                identifier=(message.chat.id, user_id, None),
                text="<b>╮⦿ من فضلك عزيزي\n╯⦿  ارسل لي كلمه السر</b>",
                filters=filters.text,
                timeout=300,
            )
        except ListenerTimeout:
            return Anony.send_message(
                user_id,
                "<b>╮⦿ عزيزي لقد نفذ الوقت\n╯⦿ يرجئ اعاده المحاوله</b>.",
                reply_markup=retry_key,
            )

        if await cancelled(pwd):
            return
        pwd = pwd.text

        try:
            if telethon:
                await client.sign_in(password=pwd)
            else:
                await client.check_password(password=pwd)
        except (PasswordHashInvalid, PasswordHashInvalidError, PasswordHashInvalid1):
            return await Anony.send_message(
                user_id,
                "» ᴛʜᴇ ᴩᴀssᴡᴏʀᴅ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs ᴡʀᴏɴɢ.\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.",
                reply_markup=retry_key,
            )

    except Exception as ex:
        return await Anony.send_message(user_id, f"ᴇʀʀᴏʀ : <code>{str(ex)}</code>")

    try:
        txt ="<b>⭓ᴍᴜˢɪᴄ✘ᴠᴇɢᴀ♪\n╮⦿ تم استخراج جلسه بنجاح\n│᚜⦿ من اصدار : {0}\n╯⦿ هذه هي جلستك\n\n\n<code>{1}</code>\n\n\n╮⦿ تم استخرجها لك من\n╯⦿ <a href={2}>سورس فيجا ميوزك</a>\n⦿ #ملاحظه : لا تشركها مع صديقك.</b>"
        if telethon:
            string_session = client.session.save()
            await client.send_message(
                "me",
                txt.format(ty, string_session, SUPPORT_CHANNEL),
                link_preview=False,
                parse_mode="html",
            )
            await client(JoinChannelRequest("@VeGaSource"))
        else:
            string_session = await client.export_session_string()
            await client.send_message(
                "me",
                txt.format(ty, string_session, SUPPORT_CHANNEL),
                disable_web_page_preview=True,
            )
            await client.join_chat("QURANI_C")
    except KeyError:
        pass
    try:
        await client.disconnect()
        await Anony.send_video(
            video="https://telegra.ph/file/8ef1b86bf2ece63f1d570.mp4",
            chat_id=user_id,
            caption=f"<b>⭓ᴍᴜˢɪᴄ✘ᴠᴇɢᴀ♪\n╮⦿ شكرا لك عزيزي لثقتك بفيجا\n╯⦿ هذه هيا جلستك : {ty} \n╮⦿ تم ارسلها لك في رسائل المحفوظه\n╯⦿ ولا تنسي الانضمام الي.<a href={SUPPORT_CHANNEL}>فيجا ميوزك</a>",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="sᴀᴠᴇᴅ ᴍᴇssᴀɢᴇs",
                            url=f"tg://openmessage?user_id={user_id}",
                            )
                        ],
                        [
                         InlineKeyboardButton(
                                "ᴠᴇɢᴧ", url=f"https://t.me/VeGaSource",
                        )
                    ]
                ]
            )
        )
    except Exception as e:
        print(f"حدث خطأ ما: {e}")



            
        
        
        
        


async def cancelled(message):
    if "/cancel" in message.text:
        await message.reply_text(
            "» ᴄᴀɴᴄᴇʟʟᴇᴅ ᴛʜᴇ ᴏɴɢᴏɪɴɢ sᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛɪᴏɴ ᴩʀᴏᴄᴇss.", reply_markup=retry_key
        )
        return True
    elif "/restart" in message.text:
        await message.reply_text(
            "» sᴜᴄᴄᴇssғᴜʟʟʏ ʀᴇsᴛᴀʀᴛᴇᴅ ᴛʜɪs ʙᴏᴛ.", reply_markup=retry_key
        )
        return True
    elif message.text.startswith("/"):
        await message.reply_text(
            "» ᴄᴀɴᴄᴇʟʟᴇᴅ ᴛʜᴇ ᴏɴɢᴏɪɴɢ sᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛɪᴏɴ ᴩʀᴏᴄᴇss.", reply_markup=retry_key
        )
        return True
    else:
        return False
