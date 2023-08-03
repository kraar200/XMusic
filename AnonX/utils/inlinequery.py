from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title=" توقف ",
            description=f"توقف البث الجاري تشغيله مؤقتًا على دردشة الفيديو .",
            thumb_url="https://graph.org/file/de157cb85e61292d4bef1.jpg",
            input_message_content=InputTextMessageContent("/pause", "اسكت", "توقف"),
        ),
        InlineQueryResultArticle(
            title=" استئناف ",
            description=f"استئناف البث المتوقف مؤقتًا على دردشة الفيديو .",
            thumb_url="https://graph.org/file/de157cb85e61292d4bef1.jpg",
            input_message_content=InputTextMessageContent("/resume", "استئناف", "كمل", "غرد"),
        ),
        InlineQueryResultArticle(
            title=" تخطي ",
            description=f"تخطي التشغيل الحالي على دردشة الفيديو والانتقال إلى البث التالي .",
            thumb_url="https://graph.org/file/de157cb85e61292d4bef1.jpg",
            input_message_content=InputTextMessageContent("/skip", "تخطي"),
        ),
        InlineQueryResultArticle(
            title=" انهاء ",
            description="إنهاء التشغيل الحالي على دردشة الفيديو .",
            thumb_url="https://graph.org/file/de157cb85e61292d4bef1.jpg",
            input_message_content=InputTextMessageContent("/end", "ايقاف", "انهاء"),
        ),
        InlineQueryResultArticle(
            title=" ترتيب ",
            description="ترتيب الأغاني في قائمة الانتظار في قائمة التشغيل عشوائيًا .",
            thumb_url="https://graph.org/file/de157cb85e61292d4bef1.jpg",
            input_message_content=InputTextMessageContent("/shuffle", "ترتيب"),
        ),
        InlineQueryResultArticle(
            title=" تكرار ",
            description="تكرار مسار التشغيل الحالي على دردشة الفيديو .",
            thumb_url="https://graph.org/file/de157cb85e61292d4bef1.jpg",
            input_message_content=InputTextMessageContent("/loop 3", "تكرار 3", "كرر"),
        ),
    ]
)
