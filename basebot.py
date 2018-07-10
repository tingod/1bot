# coding: utf-8

from telegram.ext import Updater

from utils.utils import logger


class BaseBot(object):

    def __init__(self, token, **kwargs):
        self.TOKEN = token
        self.updater = Updater(token, **kwargs)
        self.updater.dispatcher.add_error_handler(self.error)

    def error(self, bot, update, error):
        logger.warning('Update "%s" caused error "%s"', update, error)

    @property
    def dp(self):
        return self.updater.dispatcher


    # decorater:不用每定义一个函数都要用handler以及add_handler
    def handler(self, h, cmd=None, **kw):
        def d(func):
            def wrapper(*args, **kw):
                return func(*args, **kw)

            if not cmd:
                func_handler = h(func, **kw)
            else:
                func_handler = h(cmd, func, **kw)
            self.updater.dispatcher.add_handler(func_handler)
            return wrapper

        return d

    def go(self, webhook_url=None, port=None):
        if webhook_url:
            # Start the webhook
            self.updater.start_webhook(listen="0.0.0.0",
                                  port=int(port),
                                  url_path=self.TOKEN)
            self.updater.bot.setWebhook(webhook_url)
        else:
            self.updater.start_polling()

        self.updater.idle()

