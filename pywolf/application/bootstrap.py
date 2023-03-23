from pywolf.application.config import Config
from pywolf.application.context import context

from pywolf.db.db import db

class Bootstrap(object):

    def boot(self, path):
        context.set_root_path(path)

        self.load_config()
        self.init_db_config()


    def load_config(self):
        config_path = context.get_root_path() + 'config/'
        config = Config(config_path).load()

        context.set_config(config)

    def init_db_config(self):
        db_config = context.get_config().get('wolf.db')
        if not db_config:
            return
        
        db.init_config(db_config)