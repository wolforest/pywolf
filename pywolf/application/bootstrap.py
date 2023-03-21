from pywolf.application.context import ApplicationContext
from pywolf.application.config import Config
from pywolf.db.db import db

class Bootstrap(object):

    def boot(self, context: ApplicationContext):
        self.context = context
        self.load_config()
        self.init_db_config()


    def load_config(self):
        config_path = self.context.get_root_path() + 'config/'
        Config(config_path).load()

    def init_db_config(self):
        db_config = self.context.get_config().get('wolf.db')
        if not db_config:
            return
        
        db.init_config(db_config)