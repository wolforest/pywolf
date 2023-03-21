from databases import Database

class Db(object):
    def init_config(self, config):
        self.validate_config(config)
        self.config = config
        

    async def connect(self, dbname):
        return self
    
    async def disconnect(self):
        pass

    # alias of method disconnect
    async def close(self):
        await self.disconnect

    def validate_config(self, config):
        pass


db = Db()
