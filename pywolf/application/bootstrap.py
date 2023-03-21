from pywolf.application.context import ApplicationContext
from pywolf.application.config import Config

class Bootstrap(object):

    def boot(self, app: ApplicationContext):
        self.app = app
        self.load_config()


    def load_config(self):
        config_path = self.app.get_root_path() + 'config/'
        Config(config_path).load()