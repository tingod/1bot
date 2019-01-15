# coding: utf-8
import os
from telegram.ext import Updater

from utils.utils import logger, get_local_token


# Set these variable to the appropriate values
class BaseBot(object):
    # Please set your token in Heroku app settings with key 'TELEGRAM_TOKEN'
    TOKEN = os.environ.get('TELEGRAM_TOKEN')
    IS_HEROKU_MODE = True

    def __init__(self, **kwargs):
        # Change to local mode if can't get TOKEN value from Heroku settings
        if not self.TOKEN:
            self.IS_HEROKU_MODE = False
            # Please put your TOKEN in utils/token.txt file.
            self.TOKEN = get_local_token()
            # Config your proxy if necessary, else you can comment out this line
            kwargs['request_kwargs'] = {'proxy_url': 'socks5://127.0.0.1:1086/', }
        # logger.info(self.TOKEN)
        self.updater = Updater(self.TOKEN, **kwargs)
        self.updater.dispatcher.add_error_handler(self.error)

    def error(self, bot, update, error):
        logger.error('Update "%s" caused error "%s"', update, error)

    @property
    def dp(self):
        return self.updater.dispatcher

    # decorator:不用每定义一个函数都要用handler以及add_handler
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

    def go(self):

        if self.IS_HEROKU_MODE:
            logger.info('Heroku Mode start')
            # Get Heroku app name from config vars.
            name = os.environ.get('APP_NAME')
            # Get Heroku app port from config vars.
            port = os.environ.get('PORT')
            webhook_url = "https://{}.herokuapp.com/{}".format(name, self.TOKEN)
            self.updater.start_webhook(listen="0.0.0.0",
                                       port=int(port),
                                       url_path=self.TOKEN)
            self.updater.bot.setWebhook(webhook_url)
        else:
            logger.info('Local Mode start')
            self.updater.start_polling()

        self.updater.idle()
