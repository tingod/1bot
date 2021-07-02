# coding: utf-8

import os

from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from basebot import BaseBot
from models import tuling, toutiao, qiubai, yiguan
from utils.utils import logger

bb = BaseBot()



############################ Keyboards #########################################
def main_menu_keyboard():
  keyboard = [[InlineKeyboardButton('糗事百科', callback_data='m1')],
              [InlineKeyboardButton('一罐', callback_data='m2')],
              [InlineKeyboardButton('Option 3', callback_data='m3')]]
  return InlineKeyboardMarkup(keyboard)

def first_menu_keyboard():
  keyboard = [[InlineKeyboardButton('糗事', callback_data='m1_1')],
              [InlineKeyboardButton('糗图', callback_data='m1_2')],
              [InlineKeyboardButton('Main menu', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

def second_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Submenu 2-1', callback_data='m2_1')],
              [InlineKeyboardButton('Submenu 2-2', callback_data='m2_2')],
              [InlineKeyboardButton('Main menu', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

############################# Messages #########################################
def main_menu_message():
  return 'Choose the option in main menu:'

def first_menu_message():
  return 'Choose the submenu in first menu:'

def second_menu_message():
  return 'Choose the submenu in second menu:'


@bb.h(CallbackQueryHandler, required=None, pattern='main')
def main_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=main_menu_message(),
                        reply_markup=main_menu_keyboard())

@bb.h(CallbackQueryHandler, required=None, pattern='m1')
def first_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=first_menu_message(),
                        reply_markup=first_menu_keyboard())


@bb.h(CallbackQueryHandler, required=None, pattern='m2')
def second_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=second_menu_message(),
                        reply_markup=second_menu_keyboard())


@bb.h(CallbackQueryHandler, required=None, pattern='m1_1')
# and so on for every callback_data option
def first_submenu(bot, update):
    def qb(bot, update):
        # update.effective_message.text
        qb = qiubai.Qiubai()
        r = qb.text()
        reply = '[[{votes}]] ' \
                '{content}' \
                ' by {login}'
        for d in r['items']:
            bot.sendMessage(chat_id=update.message.chat_id, text=reply.format(votes=d['votes']['up'], content=d['content'], login=d['user']['login']))
            # update.message.reply_markdown(
            #     reply.format(votes=d['votes']['up'], content=d['content'], login=d['user']['login']))


@bb.h(CallbackQueryHandler, required=None, pattern='m2_1')
def second_submenu(bot, update):
    def qbimg(bot, update):
        # update.effective_message.text
        qb = qiubai.Qiubai()
        r = qb.image()
        reply = '[[{img_url}]] ' \
                '{content}' \
                ' by {author}'
        for d in r:
            # update.message.reply_photo(photo='http:'+d['img_url'])
            # update.message.reply_text('http:' + d['img_url'])
            return 'http:' + d['img_url']


"""
Add handlers here
"""


@bb.h(CommandHandler, 'qiubai')
def qb(bot, update):
    # update.effective_message.text
    qb = qiubai.Qiubai()
    r = qb.text()
    reply='[[{votes}]] ' \
          '{content}' \
          ' by {login}'
    for d in r['items']:
        update.message.reply_markdown(reply.format(votes=d['votes']['up'],content=d['content'], login=d['user']['login']))


@bb.h(CommandHandler, 'qiubaiimg')
def qbimg(bot, update):
    # update.effective_message.text
    qb = qiubai.Qiubai()
    r = qb.image()
    reply='[[{img_url}]] ' \
          '{content}' \
          ' by {author}'
    for d in r:
        # update.message.reply_photo(photo='http:'+d['img_url'])
        update.message.reply_text('http:'+d['img_url'])


@bb.h(CommandHandler, 'toutiao')
def tt(bot, update):
    # update.effective_message.text
    tt = toutiao.Toutiao()
    r = tt.fetch('news_hot')
    reply = '*{source}*\n' \
            '[{title}]({article_url})\n' \
            '{abstract}'
    for d in r['data']:
        update.message.reply_markdown(
            reply.format(title=d['title'], abstract=d['abstract'], source=d['source'], article_url=d['article_url']))


@bb.h(CommandHandler, '1guan')
def yg(bot, update):
    yg = yiguan.YiGuan()
    r = yg.feed()
    for i in r['data']:
        for img in i['photos']:
            update.message.reply_photo(
                photo=img['url']
            )


# /start command
@bb.h(CommandHandler, 'start')
def start(bot, update):
    menu_main = [[InlineKeyboardButton('糗事百科', callback_data='m1')],
                 [InlineKeyboardButton('一罐', callback_data='m2')],
                 [InlineKeyboardButton('Option 3', callback_data='m3')]]
    reply_markup = InlineKeyboardMarkup(menu_main)
    update.message.reply_text('Choose the option:', reply_markup=reply_markup)

# Filter special text
@bb.h(MessageHandler, Filters.regex('test'))
def test(bot, update):
    update.message.reply_text('test ok')


# 图灵机器人
@bb.h(MessageHandler, Filters.text)
def tl(bot, update):
    data = {
        'info': update.effective_message.text,
    }
    r = tuling.Tuling().text(data)
    update.effective_message.reply_text(r)


# Unset command
@bb.h(MessageHandler, Filters.command)
def unknown(bot, update):
    update.message.reply_text('No such command:{c}'.format(c=update.effective_message.text))


# Run bot
bb.go()
