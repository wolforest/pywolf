
from pywolf.application.bootstrap import Bootstrap
from pywolf.application.config import Config

class ApplicationContext():

    def __init__(self):
        self.context = {}
        pass

    def bootstrap(self, path):
        self.rootPath = path

        Bootstrap().boot(self)
        
    def set_config(self, config: Config):
        self.context['config'] = config

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

