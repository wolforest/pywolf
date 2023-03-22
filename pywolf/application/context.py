
from pywolf.application.bootstrap import Bootstrap
from pywolf.application.config import Config
from pywolf.application.application import Application

class ApplicationContext():

    def __init__(self):
        self.context = {}

    def set_application(self, app: Application):
        self.app = app
        return self
        
    def get_application(self):
        return self.app

    def set_config(self, config: Config):
        self.context['config'] = config
        return self

    def get_config(self) -> Config:
        return self.context.get('config')

    def set_root_path(self, path):
        self.rootPath = path

    def get_root_path(self):
        return self.rootPath

    def get(self, key):
        return self.context.get(key)



applicationContext = ApplicationContext()
context = applicationContext

