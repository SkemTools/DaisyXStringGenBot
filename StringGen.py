

import asyncio
from asyncio.exceptions import TimeoutError

from pyrogram import Client, filters
from pyrogram.errors import (
    PhoneCodeExpired,
    PhoneCodeInvalid,
    PhoneNumberInvalid,
    SessionPasswordNeeded,
)

from StringGen.dyrogram import devil as app


@app.on_message(filters.command("genstr") & filters.private)
async def genstr(_, message):
    chat = message.chat
    while True:
        number = await app.ask(
            chat.id, "Send Your Phone Number In International Format."
        )
        if not number.text:
            continue
        phone = number.text.strip()
        confirm = await app.ask(
            chat.id, f'`Is "{phone}" correct?` \n\nSend: `y`\nSend: `n`'
        )
        if "y" in confirm.text.lower():
            break
    try:
        temp_client = Client(
            ":memory:", api_id=6, api_hash="eb06d4abfb49dc3eeb1aeb98ae0f581e"
        )
    except Exception as e:
        await app.send_message(chat.id, f"**ERROR:** `{str(e)}`")
        return
    try:
        await temp_client.connect()
    except ConnectionError:
        await temp_client.disconnect()
        await temp_client.connect()
    try:
        code = await temp_client.send_code(phone)
        await asyncio.sleep(2)
    except PhoneNumberInvalid:
        await message.reply_text("Phone Number is Invalid")
        return

    try:
        otp = await app.ask(
            chat.id,
            (
                "An OTP is sent to your phone number, "
                "Please enter OTP in `1 2 3 4 5` format. __(Space between each numbers!)__"
            ),
            timeout=300,
        )

    except TimeoutError:
        await message.reply_text("Time limit reached of 5 min. Process Cancelled.")
        return
    otp_code = otp.text
    try:
        await temp_client.sign_in(
            phone, code.phone_code_hash, phone_code=" ".join(str(otp_code))
        )
    except PhoneCodeInvalid:
        await message.reply_text("Invalid OTP.")
        return
    except PhoneCodeExpired:
        await message.reply_text("OTP is Expired.")
        return
    except SessionPasswordNeeded:
        try:
            two_step_code = await app.ask(
                chat.id,
                "Your account have Two-Step Verification.\nPlease enter your Password.",
                timeout=300,
            )
        except TimeoutError:
            await message.reply_text("Time limit reached of 5 min.")
            return
        new_code = two_step_code.text
        try:
            await temp_client.check_password(new_code)
        except Exception as e:
            await message.reply_text(f"**ERROR:** `{str(e)}`")
            return
    except Exception as e:
        await app.send_message(chat.id, f"**ERROR:** `{str(e)}`")
        return
    try:
        session_string = await temp_client.export_session_string()
        await temp_client.disconnect()
        await app.send_message(
            chat.id, text=f"**HERE IS YOUR STRING SESSION:**\n```{session_string}```"
        )
    except Exception as e:
        await app.send_message(chat.id, f"**ERROR:** `{str(e)}`")
        return


_help = """
 * String Generator Generate Only Pyrogram String Session*
 ✪ /genstr : Type in Pm of bot to generate Pyrogram string session. 
"""

_mod_name_ = "String Generator

import asyncio
from asyncio.exceptions import TimeoutError

from pyrogram import Client, filters
from pyrogram.errors import (
    PhoneCodeExpired,
    PhoneCodeInvalid,
    PhoneNumberInvalid,
    SessionPasswordNeeded,
)

from StringGen.dyrogram import devil as app


@app.on_message(filters.command("genstr") & filters.private)
async def genstr(_, message):
    chat = message.chat
    while True:
        number = await app.ask(
            chat.id, "Send Your Phone Number In International Format."
        )
        if not number.text:
            continue
        phone = number.text.strip()
        confirm = await app.ask(
            chat.id, f'`Is "{phone}" correct?` \n\nSend: `y`\nSend: `n`'
        )
        if "y" in confirm.text.lower():
            break
    try:
        temp_client = Client(
            ":memory:", api_id=6, api_hash="eb06d4abfb49dc3eeb1aeb98ae0f581e"
        )
    except Exception as e:
        await app.send_message(chat.id, f"**ERROR:** `{str(e)}`")
        return
    try:
        await temp_client.connect()
    except ConnectionError:
        await temp_client.disconnect()
        await temp_client.connect()
    try:
        code = await temp_client.send_code(phone)
        await asyncio.sleep(2)
    except PhoneNumberInvalid:
        await message.reply_text("Phone Number is Invalid")
        return

    try:
        otp = await app.ask(
            chat.id,
            (
                "An OTP is sent to your phone number, "
                "Please enter OTP in `1 2 3 4 5` format. __(Space between each numbers!)__"
            ),
            timeout=300,
        )

    except TimeoutError:
        await message.reply_text("Time limit reached of 5 min. Process Cancelled.")
        return
    otp_code = otp.text
    try:
        await temp_client.sign_in(
            phone, code.phone_code_hash, phone_code=" ".join(str(otp_code))
        )
    except PhoneCodeInvalid:
        await message.reply_text("Invalid OTP.")
        return
    except PhoneCodeExpired:
        await message.reply_text("OTP is Expired.")
        return
    except SessionPasswordNeeded:
        try:
            two_step_code = await app.ask(
                chat.id,
                "Your account have Two-Step Verification.\nPlease enter your Password.",
                timeout=300,
            )
        except TimeoutError:
            await message.reply_text("Time limit reached of 5 min.")
            return
        new_code = two_step_code.text
        try:
            await temp_client.check_password(new_code)
        except Exception as e:
            await message.reply_text(f"**ERROR:** `{str(e)}`")
            return
    except Exception as e:
        await app.send_message(chat.id, f"**ERROR:** `{str(e)}`")
        return
    try:
        session_string = await temp_client.export_session_string()
        await temp_client.disconnect()
        await app.send_message(
            chat.id, text=f"**HERE IS YOUR STRING SESSION:**\n```{session_string}```"
        )
    except Exception as e:
        await app.send_message(chat.id, f"**ERROR:** `{str(e)}`")
        return

from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from StringGen.filters import command, other_filters, other_filters2


@Client.on_message(command("start") & other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""🙃 Hi {message.from_user.first_name}!
✨ Hey I am DaisyX String Generator Bot. 
🥳 I can Generator String Session for You 😉
⚜️ Use these buttons below to know more. 👇
🔥 Source Code Made by Devil With Help Of Other Bots 🔥
👉 Type /genstr for Generating String Session 👈""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚒ Source code", url="https://github.com/SkemTools"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/DaisySupport_Official"
                    ),
                    InlineKeyboardButton(
                        "Channel 🔈", url="https://t.me/DaisyXUpdates"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "❌ Close ❌", callback_data="close"
                    )
                ]
            ]
        )
    )




