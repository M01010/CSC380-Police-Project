import sqlite3


class Database:

    @staticmethod
    def connect_sqlite():
        con = sqlite3.connect('police.db')
        con.row_factory = sqlite3.Row
        return con

    class Victims:
        @staticmethod
        def get_victims():
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
        def get_victim(victim_id):
            connection = None
            cursor = None
            try:
                connection = Database.connect_sqlite()
                cursor = connection.cursor()
                cursor.execute(f'select * from test where id={victim_id}')
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
        def add_victim(victim):
            connection = None
            cursor = None
            try:
                connection = Database.connect_sqlite()
                cursor = connection.cursor()
                cursor.execute(f'insert into test values ("{victim["id"]}", "{victim["name"]}")')
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
        def edit_victim(victim_id, victim):
            connection = None
            cursor = None
            try:
                connection = Database.connect_sqlite()
                cursor = connection.cursor()
                cursor.execute(f'update test set id ={victim["id"]}, name="{victim["name"]}" where id={victim_id}')
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
        def delete_victim(victim_id):
            connection = None
            cursor = None
            try:
                connection = Database.connect_sqlite()
                cursor = connection.cursor()
                cursor.execute(f'delete from test where id={victim_id}')
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
