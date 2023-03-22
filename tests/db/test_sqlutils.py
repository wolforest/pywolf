import pytest

from pywolf.db import sqlutils


def test_join_columns():
    columns = ['id', 'name', 'gender']
    expect = '`id`, `name`, `gender`'
    sql = sqlutils.join_columns(columns)

    assert expect == sql


def test_join_values():
    columns = ['id', 'name', 'gender']
    expect = ':id, :name, :gender'
    sql = sqlutils.join_values(columns)
    
    assert expect == sql


def test_build_insert():
    table = 'customer'
    values = {
        'id': 1,
        'name': 'somename',
        'gender': 1,
    }

    expect = 'INSERT INTO customer (`id`, `name`, `gender`) values (:id, :name, :gender)'
    sql = sqlutils.build_insert_sql(table, values)

    assert expect == sql
