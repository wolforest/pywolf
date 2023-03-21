from pywolf.lang import strutils

def isSelect(sql: str) -> bool:
    return strutils.starts_with(sql, "select")

def isUpdate(sql: str) -> bool:
    return strutils.starts_with(sql, "update")

def isDelete(sql: str) -> bool:
    return strutils.starts_with(sql, "delete")

def isInsert(sql: str) -> bool:
    return strutils.starts_with(sql, "insert")