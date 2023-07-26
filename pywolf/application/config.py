import yaml

from pywolf.utils import fileutils


class Config(object):

    def __init__(self, path):
        self.path = path
        self.dict = {}

    def load(self):
        self.load_main_config()
        self.load_env_config()
        return self

    def get(self, key: str):
        if '.' not in key:
            return self.dict.get(key)

        keys = key.split('.')
        last = keys.pop()

        d = self.dict
        for k in keys:
            d = self.dict.get(k)
            if not isinstance(d, dict):
                return None

        return d.get(last)

    def get_dict(self):
        return self.dict

    # private methods start
    def load_main_config(self):
        main_config_file = self.path + 'app.yaml'

        if not fileutils.exists(main_config_file):
            return

        data = self.load_yaml_file(main_config_file)
        if not data:
            return

        self.dict = data

    def load_env_config(self):
        if not self.get('wolf.env'):
            return

        env_config_file = self.path + 'app-' + self.get('wolf.env') + '.yaml'
        if not fileutils.exists(env_config_file):
            return

        data = self.load_yaml_file(env_config_file)
        if not data:
            return

        self.dict.update(data)

    def load_yaml_file(self, path):
        contents = fileutils.read_contents(path)
        return yaml.safe_load(contents)
