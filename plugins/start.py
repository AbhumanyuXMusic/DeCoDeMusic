from pyrogram import Client, filters

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn

from helpers.filters import other_filters2

from time import time

from datetime import datetime

from helpers.decorators import authorized_users_only

from config import BOT_USERNAME, ASSISTANT_USERNAME

START_TIME = datetime.utcnow()

START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()

TIME_DURATION_UNITS = (

    ("week", 60 * 60 * 24 * 7),

    ("day", 60 ** 2 * 24),

    ("hour", 60 ** 2),

    ("min", 60),

    ("sec", 1),

)

async def _human_time_duration(seconds):

    if seconds == 0:

        return "inf"

    parts = []

    for unit, div in TIME_DURATION_UNITS:

        amount, seconds = divmod(int(seconds), div)

        if amount > 0:

            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))

    return ", ".join(parts)

@Client.on_message(other_filters2)

async def start(_, message: Message):

        await message.reply_text(

        f"""**Hey, I'm {bn} 🎀

I Cᴀɴ Pʟᴀʏ Mᴜsɪᴄ Iɴ Yᴏᴜʀ Gʀᴏᴜᴩ Vᴏɪᴄᴇ Cʜᴀᴛ. Dᴇᴠᴇʟᴏᴩᴇᴅ Bʏ [🇮🇳𝐀𝐛𝐡𝐢𝐦𝐚𝐧𝐲𝐮 𝐒𝐢𝐧𝐠𝐡 𝐑𝐚𝐧𝐚𝐰𝐚𝐭🇮🇳](https://t.me/Itz_Venom_xD).

Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴩ Aɴᴅ Pʟᴀʏ Mᴜsɪᴄ Fʀᴇᴇʟʏ!**

        """,

        reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        "𝐂𝐡𝐚𝐭 𝐆𝐫𝐨𝐮𝐩🇮🇳", url="https://t.me/Shayri_Music_Lovers")

                  ],[

                    InlineKeyboardButton(

                       " 𝐒𝐮𝐩𝐩𝐨𝐫𝐭🇮🇳", url="https://t.me/AlishaSupport"

                    ),

                    InlineKeyboardButton(

                        "𝐔𝐩𝐝𝐚𝐭𝐞𝐬🇮🇳", url="https://t.me/Lol_Tum_Bin"

                    )

                ],[

                    InlineKeyboardButton(

                        "➕ 𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩➕",

                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",

                    )

                ]

            ]

        ),

     disable_web_page_preview=True

    )
