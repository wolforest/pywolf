from databases import Database

from pywolf.db.config import Validator
from pywolf.db.executor import Executor


class Db(object):
    def __init__(self):
        self.conn_dict = {}
        self.config = None

    def init_config(self, config: dict):
        if not Validator.validate(config):
            raise SyntaxError("invalid database config")

        self.config = config

    async def connect(self, dbname: str = 'default'):
        if dbname in self.conn_dict:
            conn = self.conn_dict.get(dbname)
            return Executor(conn)

        if dbname not in self.config:
            raise SyntaxError(f'db connection: {dbname} does not exists')

        conn = Database(self.config.get(dbname).get('url'))
        await conn.connect()
        self.conn_dict[dbname] = conn

        return Executor(conn)

    async def disconnect(self):
        pass

    # alias of method disconnect
    async def close(self):
        await self.disconnect()


db = Db()
