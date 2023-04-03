import redis.asyncio as redis

from pywolf.middleware.cache.config import Validator


class Cache(object):
    config: dict = None
    conn_dict: dict = None
    conn = None

    def __init__(self):
        self.conn_dict = {}
        self.conn = None

    def init_config(self, config: dict):
        if not Validator.validate(config):
            raise SyntaxError("invalid cache config")

        self.config = config

    def connect(self, dbname: str = 'default'):
        if dbname in self.conn_dict:
            self.conn = self.conn_dict.get(dbname)

        if dbname not in self.config:
            raise SyntaxError(f'cache connection: {dbname} does not exists')

        self.conn = redis.from_url(self.config[dbname]['url'])
        self.conn_dict[dbname] = self.conn

    async def get(self, key):
        return await self.conn.get(key)

    async def set(self, key, value):
        return await self.conn.set(key, value)


cache = Cache()
