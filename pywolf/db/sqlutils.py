from pywolf.lang import strutils

def is_select(sql: str) -> bool:
    return strutils.starts_with(sql, "select")

def is_update(sql: str) -> bool:
    return strutils.starts_with(sql, "update")

def is_delete(sql: str) -> bool:
    return strutils.starts_with(sql, "delete")

def is_insert(sql: str) -> bool:
    return strutils.starts_with(sql, "insert")

def get_first_insert_row(values):
    if not values:
        raise SyntaxError('invalid insert values')

    if isinstance(values, dict):
        return values
    elif isinstance(values, list) and len(values) > 0 and isinstance(values[0], dict):
        return values[0]
    else :
        raise SyntaxError('invalid insert values')

def build_insert_sql(table: str, values):
    if not table or not values:
        raise SyntaxError('invalid insert syntax')
    
    first_row = get_first_insert_row(values)
    columns = first_row.keys()

    sql = 'INSERT INTO '. join(table, '(', ') values (', ')')


def join_columns(columns: list) -> str:
    return '`' + '`, `'.join(columns) + '`'
    
def join_values(columns: list) -> str:
    return ':' + ', :'.join(columns)


 