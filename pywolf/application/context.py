
from pywolf.application.config import Config
class ApplicationContext():

    def __init__(self):
        self.context = {}


    def set_application(self, app):
        self.app = app
        return self
        
    def get_application(self):
        return self.app

    def set_config(self, config: Config):
        self.context['config'] = config
        return self

    def get_config(self) -> Config:
        config = self.context.get('config')
        if not config:
            raise SystemError('config has not been set')
        
        return config

    def set_root_path(self, path):
        self.rootPath = path

    def get_root_path(self):
        return self.rootPath

    def get(self, key):
        return self.context.get(key)



applicationContext = ApplicationContext()
context = applicationContext

