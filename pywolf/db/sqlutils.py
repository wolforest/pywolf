from pywolf.lang import strutils

def is_select(sql: str) -> bool:
    return strutils.starts_with(sql, "select")

def is_update(sql: str) -> bool:
    return strutils.starts_with(sql, "update")

def is_delete(sql: str) -> bool:
    return strutils.starts_with(sql, "delete")

def is_insert(sql: str) -> bool:
    return strutils.starts_with(sql, "insert")