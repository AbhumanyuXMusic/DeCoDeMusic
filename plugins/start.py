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
        await message.reply_photo(

        photo=f"https://telegra.ph/file/de138de8fd880becb9cf1.jpg",

        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━

💥 ʜᴇʟʟᴏ, ɪ ᴀᴍ Qᴜᴇᴇɴ ᴀʟɪꜱʜᴀ sᴜᴘᴇʀ ғᴀsᴛ ᴠᴄ ᴘʟᴀʏᴇʀ

ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs ...

┏━━━━━━━━━━━━━━━━━┓

┣★ ᴄʀᴇᴀᴛᴏʀ : [ᴀʙʜɪᴍɴᴀʏᴜ](https://t.me/Itz_VeNom_xD)

┣★ ᴜᴘᴅᴀᴛᴇs : [ᴄʜᴀɴɴᴇʟ](https://t.me/Pubglovers_shayri_lovers)

┣★ sᴜᴘᴘᴏʀᴛ : [ɢʀᴏᴜᴘ](https://t.me/AlishaSupport)

┣★ ɢʀᴏᴜᴘ  : [ᴄʜᴀᴛ ɢʀᴏᴜᴘ](https://t.me/Lol_tum_bin)

┗━━━━━━━━━━━━━━━━━┛

💞 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ

ᴅᴍ ᴛᴏ ᴍʏ [ᴏᴡɴᴇʀ](https://t.me/Itz_Venom_xD) ...

━━━━━━━━━━━━━━━━━━━━━━━━**""",
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
