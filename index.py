#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple Bot to reply to Telegram messages
# This program is dedicated to the public domain under the CC0 license.

import logging
import telegram
from telegram.error import NetworkError, Unauthorized
from time import sleep

def main():
    bot = telegram.Bot('212766013:AAH4tIpm6hHZREsxYNuYdCdNbw6CDlwV094')
    try:
        update_id = bot.getUpdates()[0].update_id
    except IndexError:
        update_id = None
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    while True:
        try:
            update_id = echo(bot, update_id)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            update_id += 1

def echo(bot, update_id):
    for update in bot.getUpdates(offset=update_id, timeout=10):
        chat_id = update.message.chat_id
        update_id = update.update_id + 1
        voice = update.message.voice
        if voice:
            newFile = bot.getFile(voice.file_id)
            newFile.download('voice.ogg')
            bot.sendMessage(chat_id=chat_id, text="Voice!")
    return update_id

if __name__ == '__main__':
    main()
