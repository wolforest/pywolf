from databases import Database
from pywolf.db.result import Result
from pywolf.db import sqlutils

class Executor(object):
    def __init__(self, conn: Database):
        self.conn = conn

    async def execute(self, sql: str, values=None) -> Result:
        if not sql:
            raise SystemError('invalid sql: ' + sql)
        
        if sqlutils.is_select(sql):
            return await self.select(sql)

        resp = await self.conn.execute(sql)
        if not resp:
            return Result.from_affected_rows(0)

        if sqlutils.is_insert(sql):
            return Result.from_last_id(resp)

        return Result.from_affected_rows(resp)
    
    async def insert(self, table:str, values) -> Result:
        sql = sqlutils.build_insert_sql(table, values)
        if isinstance(values, dict):
            return await self.execute(sql, values)
        
        await self.conn.execute_many(sql, values)
        return Result.from_affected_rows(len(values))

    async def select(self, sql: str, values:dict=None) -> Result:
        resp = await self.conn.fetch_all(sql, values)

        if 1 == len(resp):
            count = sqlutils.get_count_from_response(resp)
            if count >= 0:
                return Result.from_count(count)

        return Result.from_rows(resp)

    async def count(self, sql: str, values:dict=None) -> int:
        result = await self.select(sql, values)
        return result.get_count()