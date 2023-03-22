
from pywolf.db.result import Result
from pywolf.db import sqlutils

class Executor(object):
    def __init__(self, conn) -> None:
        self.conn = conn

    async def execute(self, sql: str) -> Result:
        if not sql:
            raise SystemError('invalid sql: ' + sql)
        
        if sqlutils.is_select(sql):
            return await self.select(sql)


        resp = await self.conn.execute(sql)
        if not resp:
            return Result.from_affected_rows(resp)

        return Result.from_affected_rows(0)
    
    async def insert(self, table:str, values):
        return None
    
    async def select(self, sql: str):
        return None
    

    
   
    

