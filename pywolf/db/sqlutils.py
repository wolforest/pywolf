from pywolf.lang import strutils


def is_select(sql: str) -> bool:
    return strutils.starts_with(sql, "select")


def is_update(sql: str) -> bool:
    return strutils.starts_with(sql, "update")


def is_delete(sql: str) -> bool:
    return strutils.starts_with(sql, "delete")


def is_insert(sql: str) -> bool:
    return strutils.starts_with(sql, "insert")


def get_first_insert_row(values) -> dict:
    if not values:
        raise SyntaxError('invalid insert values')

    if isinstance(values, dict):
        return values
    elif isinstance(values, list) and len(values) > 0 and isinstance(values[0], dict):
        return values[0]
    else:
        raise SyntaxError('invalid insert values')


def build_insert_sql(table: str, values) -> str:
    if not table or not values:
        raise SyntaxError('invalid insert syntax')

    first_row = get_first_insert_row(values)
    columns = list(first_row.keys())

    sql = f'INSERT INTO {table} ({join_columns(columns)}) values ({join_values(columns)})'
    return sql


def join_columns(columns: list) -> str:
    return '`' + '`, `'.join(columns) + '`'


def join_values(columns: list) -> str:
    return ':' + ', :'.join(columns)


def get_count_from_response(resp) -> int:
    """
        get count(*), count(*) as count value from db response
    """
    if not isinstance(resp, list):
        return -1

    if 1 != len(resp):
        return -1

    row = resp[0]
    if 'count(*)' in row:
        return row['count(*)']

    if 'count' in row:
        return row['count']

    return -1
