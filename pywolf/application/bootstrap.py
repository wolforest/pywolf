import logging

from pywolf.application.config import Config
from pywolf.application.context import context

from pywolf.db.db import db
from pywolf.middleware.cache.cache import cache


class Bootstrap(object):

    def boot(self, path):
        context.set_root_path(path)

        self.load_config()
        self.init_logging_config()
        self.init_db_config()

    @staticmethod
    def load_config():
        config_path = context.get_root_path() + 'config/'
        config = Config(config_path).load()

        context.set_config(config)

    @staticmethod
    def init_logging_config():
        logging.basicConfig(level=logging.INFO)

    @staticmethod
    def init_db_config():
        db_config = context.get_config().get('wolf.db')
        if not db_config:
            return

        db.init_config(db_config)

    @staticmethod
    def init_cache_config():
        cache_config = context.get_config().get('wolf.cache')
        if not cache_config:
            return

        cache.init_config(cache_config)
