from pyrogram import filters

import config
from strings import get_command
from AnonX import app
from AnonX.misc import SUDOERS
from AnonX.utils.database import autoend_off, autoend_on
from AnonX.utils.decorators.language import language

# Commands
AUTOEND_COMMAND = get_command("AUTOEND_COMMAND")


@app.on_message(filters.command(AUTOEND_COMMAND) & SUDOERS)
async def auto_end_stream(client, message):
    usage = "**الاستخدام :**\n\n/autoend [enable|disable]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "تم تمكين تشغيل النهاية التلقائي .\n\nسيترك المساعد تلقائيًا محادثة الفيديو بعد دقائق قليلة عندما لا يستمع أحد برسالة تحذير ."
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("تم تعطيل تشغيل النهاية التلقائي .")
    else:
        await message.reply_text(usage)
