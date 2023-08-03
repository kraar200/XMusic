import sys

from pyrogram import Client

import config

from ..logging import LOGGER



class AnonXBot(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Starting Bot...")
        super().__init__(
            "AnonXMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        self.name = get_me.first_name + " " + (get_me.last_name or "")

        try:
            await self.send_message(
                config.LOG_GROUP_ID, f"**» {config.MUSIC_BOT_NAME} ʙᴏᴛ sᴛᴀʀᴛᴇᴅ :**\n\n✨ ɪᴅ : `{self.id}`\n❄ ɴᴀᴍᴇ : {self.name}\n💫 ᴜsᴇʀɴᴀᴍᴇ : @{self.username}"
            )
        except:
            LOGGER(__name__).error(
                "فشل البوت في الوصول إلى مجموعة السجل. تأكد من أنك أضفت الروبوت الخاص بك إلى قناة السجل الخاصة بك وقمت بالترقية كمسؤول !"
            )
            sys.exit()

        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != "administrator":
            LOGGER(__name__).error(
                "يرجى ترقية البوت كمسؤول في Logger Group "
            )
            sys.exit()
        LOGGER(__name__).info(f"MusicBot بدأت كـ @{self.username}")
