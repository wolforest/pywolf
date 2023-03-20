
import yaml

from pywolf.lang import fileutils

class Config(dict):
    def __init__(self, path):
        self.path = path
    
    def load(self):
        self.load_main_config()
        self.load_env_config()

    def load_main_config(self):
        main_config_file = self.path + 'app.yaml'
        if not fileutils.exists(main_config_file):
            return

    def load_env_config(self):
        if not self.get('env'):
            return
        
        env_config_file = self.path + 'app' + self.get('env')  +'.yaml'

    def get(self, key:str):
        return super.get(key)
    
    def get_dict(self, key: str):
        pass