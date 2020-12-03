# coding: utf-8

import os
import sys
import pyodbc
import json


class DatabaseManager():

    def __init__(self, host, port, database, uid, pwd):
        self._connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};' +\
            f'SERVER={host},{port};' + \
            f'DATABASE={database};' + \
            f'UID={uid};' + \
            f'PWD={pwd}'

    def connect_test(self):
        try:
            cnxn = pyodbc.connect(self._connection_string)
            cnxn.close()
            return True
        except pyodbc.DatabaseError as err:
            print(err, file=sys.stderr)
            return False

    def execute(self, sql):
        try:
            cnxn = pyodbc.connect(self._connection_string)
            cursor = cnxn.cursor()
            cursor.execute(sql)
            cnxn.commit()
            return True
        except pyodbc.DatabaseError as err:
            print(err, file=sys.stderr)
            cnxn.rollback()
            return False

    def query(self, sql):
        try:
            cnxn = pyodbc.connect(self._connection_string)
            cursor = cnxn.cursor()
            rc = cursor.execute(sql)
            records = cursor.fetchall()
            cnxn.commit()

            result = {
                "columns" : [ c[0] for c in rc.description ],
                "records" : [ [ v for v in r ] for r in records  ]
            }
            return result
        except pyodbc.DatabaseError as err:
            print(err, file=sys.stderr)
            cnxn.rollback()
            return None


if __name__ == '__main__':

    dbm = DatabaseManager(
        host="xxx.xxx.xxx.xxx",
        port="1433",
        database="database_name",
        uid="user_id",
        pwd="password"
    )

    # 接続テスト
    result = dbm.connect_test()
    print(result)

    # クエリ（SELECT）
    result = dbm.query("""
        select
                schemas.name as schema_name
            ,   tables.name  as table_name
        from sys.objects tables
            inner join sys.schemas schemas
                on tables.schema_id = schemas.schema_id
        where
                type = 'U'
            and schemas.name + '.' + tables.name = 'dbo.sample_table'
    """)
    print(json.dumps(result, indent=2))
    
    # 更新
    result = dbm.execute("""
        update dbo.sample_table
        set id = 1
        where 1 = 0;
    """)
    print(result)

    sys.exit(0)
