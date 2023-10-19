import sqlite3

import psycopg2

from credentials import Credentials


class Database:

    @staticmethod
    def connect_supabase():
        con = psycopg2.connect(
            database=Credentials.database,
            host=Credentials.host,
            user=Credentials.user,
            password=Credentials.password,
            port=Credentials.port
        )
        return con

    @staticmethod
    def connect_sqlite():
        con = sqlite3.connect('police.db')
        con.row_factory = sqlite3.Row
        return con

    class Test:
        @staticmethod
        def get_tests():
            connection = None
            cursor = None
            try:
                connection = Database.connect_sqlite()
                cursor = connection.cursor()
                cursor.execute('select * from test')
                return cursor.fetchall()
            except Exception as e:
                raise e
            finally:
                try:
                    cursor.close()
                    connection.close()
                except Exception as e:
                    print(e)

        @staticmethod
        def get_test(test_id):
            connection = None
            cursor = None
            try:
                connection = Database.connect_sqlite()
                cursor = connection.cursor()
                cursor.execute(f'select * from test where id={test_id}')
                return cursor.fetchone()
            except Exception as e:
                raise e
            finally:
                try:
                    cursor.close()
                    connection.close()
                except Exception as e:
                    print(e)

        @staticmethod
        def add_test(test):
            connection = None
            cursor = None
            try:
                connection = Database.connect_sqlite()
                cursor = connection.cursor()
                cursor.execute(f'insert into test values ("{test["id"]}", "{test["name"]}")')
                connection.commit()
            except Exception as e:
                raise e
            finally:
                try:
                    cursor.close()
                    connection.close()
                except Exception as e:
                    print(e)

        @staticmethod
        def edit_test(test_id, test):
            connection = None
            cursor = None
            try:
                connection = Database.connect_sqlite()
                cursor = connection.cursor()
                cursor.execute(f'update test set id ={test["id"]}, name="{test["name"]}" where id={test_id}')
                connection.commit()
            except Exception as e:
                raise e
            finally:
                try:
                    cursor.close()
                    connection.close()
                except Exception as e:
                    print(e)

        @staticmethod
        def delete_test(test_id):
            connection = None
            cursor = None
            try:
                connection = Database.connect_sqlite()
                cursor = connection.cursor()
                cursor.execute(f'delete from test where id={test_id}')
                connection.commit()
                return
            except Exception as e:
                raise e
            finally:
                try:
                    cursor.close()
                    connection.close()
                except Exception as e:
                    print(e)
