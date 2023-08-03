from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضف البوت في المجموعة ➕ ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="☆مساعدة☆",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="🔗الاعدادات🔗", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضف البوت في المجموعة ➕ ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="☆مساعدة☆", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="❣ الدعم ❣", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="🥀🍷 المالك 🍷🥀", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="✨📍قناة المطور📍✨", url=config.UPSTREAM_REPO
            )
        ],
     ]
    return buttons
