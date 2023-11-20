# import sqlite3
#
#
# class Database:
#
#     @staticmethod
#     def connect_sqlite():
#         con = sqlite3.connect('police.db')
#         con.row_factory = sqlite3.Row
#         return con
#
#     class Victims:
#         @staticmethod
#         def get_victims():
#             connection = None
#             cursor = None
#             try:
#                 connection = Database.connect_sqlite()
#                 cursor = connection.cursor()
#                 cursor.execute('select * from test')
#                 return cursor.fetchall()
#             except Exception as e:
#                 raise e
#             finally:
#                 try:
#                     cursor.close()
#                     connection.close()
#                 except Exception as e:
#                     print(e)
#
#         @staticmethod
#         def get_victim(victim_id):
#             connection = None
#             cursor = None
#             try:
#                 connection = Database.connect_sqlite()
#                 cursor = connection.cursor()
#                 cursor.execute(f'select * from test where id={victim_id}')
#                 rs = cursor.fetchone()
#                 if rs is None:
#                     raise Exception(f'id {victim_id} doesnt exist')
#                 return rs
#             except Exception as e:
#                 raise e
#             finally:
#                 try:
#                     cursor.close()
#                     connection.close()
#                 except Exception as e:
#                     print(e)
#
#         @staticmethod
#         def add_victim(victim):
#             connection = None
#             cursor = None
#             try:
#                 connection = Database.connect_sqlite()
#                 cursor = connection.cursor()
#                 cursor.execute(f'insert into test values ("{victim["id"]}", "{victim["name"]}")')
#                 connection.commit()
#             except Exception as e:
#                 raise e
#             finally:
#                 try:
#                     cursor.close()
#                     connection.close()
#                 except Exception as e:
#                     print(e)
#
#         @staticmethod
#         def edit_victim(victim_id, victim):
#             connection = None
#             cursor = None
#             try:
#                 connection = Database.connect_sqlite()
#                 cursor = connection.cursor()
#                 cursor.execute(f'update test set id ={victim["id"]}, name="{victim["name"]}" where id={victim_id}')
#                 connection.commit()
#             except Exception as e:
#                 raise e
#             finally:
#                 try:
#                     cursor.close()
#                     connection.close()
#                 except Exception as e:
#                     print(e)
#
#         @staticmethod
#         def delete_victim(victim_id):
#             connection = None
#             cursor = None
#             try:
#                 connection = Database.connect_sqlite()
#                 cursor = connection.cursor()
#                 cursor.execute(f'select id from test where id={victim_id}')
#                 if cursor.fetchone() is None:
#                     raise Exception(f'id {victim_id} doesnt exist')
#                 cursor.execute(f'delete from test where id={victim_id}')
#                 connection.commit()
#                 return
#             except Exception as e:
#                 raise e
#             finally:
#                 try:
#                     cursor.close()
#                     connection.close()
#                 except Exception as e:
#                     print(e)


import mysql.connector

class Database:

    @staticmethod
    def connect_mysql():
        return mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="policedb"
        )

    class Victims:
        @staticmethod
        def get_victims():
            connection = None
            cursor = None
            try:
                connection = Database.connect_mysql()
                cursor = connection.cursor(dictionary=True)
                cursor.execute('SELECT * FROM VICTIM')
                return cursor.fetchall()
            except Exception as e:
                raise e
            finally:
                if cursor is not None:
                    cursor.close()
                if connection is not None:
                    connection.close()

        @staticmethod
        def get_victim(victim_id):
            connection = None
            cursor = None
            try:
                connection = Database.connect_mysql()
                cursor = connection.cursor(dictionary=True)
                cursor.execute('SELECT * FROM VICTIM WHERE victim_id = %s', (victim_id,))
                rs = cursor.fetchone()
                if rs is None:
                    raise Exception(f'Victim ID {victim_id} does not exist')
                return rs
            except Exception as e:
                raise e
            finally:
                if cursor is not None:
                    cursor.close()
                if connection is not None:
                    connection.close()

        @staticmethod
        def add_victim(victim):
            connection = None
            cursor = None
            try:
                connection = Database.connect_mysql()
                cursor = connection.cursor()
                cursor.execute(
                    'INSERT INTO VICTIM (victim_id, name, date_of_birth, contact_info) VALUES (%s, %s, %s, %s)',
                    (victim["victim_id"], victim["name"], victim["date_of_birth"], victim["contact_info"]))
                connection.commit()
            except Exception as e:
                raise e
            finally:
                if cursor is not None:
                    cursor.close()
                if connection is not None:
                    connection.close()

        @staticmethod
        def edit_victim(victim_id, victim):
            connection = None
            cursor = None
            try:
                connection = Database.connect_mysql()
                cursor = connection.cursor()
                cursor.execute(
                    'UPDATE VICTIM SET name = %s, date_of_birth = %s, contact_info = %s WHERE victim_id = %s',
                    (victim["name"], victim["date_of_birth"], victim["contact_info"], victim_id))
                connection.commit()
            except Exception as e:
                raise e
            finally:
                if cursor is not None:
                    cursor.close()
                if connection is not None:
                    connection.close()

        @staticmethod
        def delete_victim(victim_id):
            connection = None
            cursor = None
            try:
                connection = Database.connect_mysql()
                cursor = connection.cursor()
                cursor.execute('DELETE FROM VICTIM WHERE victim_id = %s', (victim_id,))
                connection.commit()
            except Exception as e:
                raise e
            finally:
                if cursor is not None:
                    cursor.close()
                if connection is not None:
                    connection.close()

    class Officers:
        @staticmethod
        def add_officer(officer):
            connection = None
            cursor = None
            try:
                connection = Database.connect_mysql()
                cursor = connection.cursor()
                cursor.execute(
                    'INSERT INTO OFFICER (officer_id, name, badge_number, rank , date_of_birth) VALUES (%s, %s, %s, %s ,%s)',
                    (officer["officer_id"], officer["name"], officer["badge_number"], officer["rank"], officer["date_of_birth"]))
                connection.commit()
            except Exception as e:
                raise e
            finally:
                if cursor is not None:
                    cursor.close()
                if connection is not None:
                    connection.close()

        @staticmethod
        def get_officers():
            connection = None
            cursor = None
            try:
                connection = Database.connect_mysql()
                cursor = connection.cursor(dictionary=True)
                cursor.execute('SELECT * FROM OFFICER')
                return cursor.fetchall()
            except Exception as e:
                raise e
            finally:
                if cursor is not None:
                    cursor.close()
                if connection is not None:
                    connection.close()

        @staticmethod
        def get_officer(officer_id):
            connection = None
            cursor = None
            try:
                connection = Database.connect_mysql()
                cursor = connection.cursor(dictionary=True)
                cursor.execute('SELECT * FROM OFFICER WHERE officer_id = %s', (officer_id,))
                return cursor.fetchone()
            except Exception as e:
                raise e
            finally:
                if cursor is not None:
                    cursor.close()
                if connection is not None:
                    connection.close()

        @staticmethod
        def edit_officer(officer_id, officer):
            connection = None
            cursor = None
            try:
                connection = Database.connect_mysql()
                cursor = connection.cursor()
                cursor.execute(
                    'UPDATE OFFICER SET name = %s, badge_number = %s, rank = %s, date_of_birth = %s WHERE officer_id = %s',
            (officer["name"], officer["badge_number"], officer["rank"], officer["date_of_birth"], officer_id))
                connection.commit()
            except Exception as e:
                raise e
            finally:
                if cursor is not None:
                    cursor.close()
                if connection is not None:
                    connection.close()

        @staticmethod
        def delete_officer(officer_id):
            connection = None
            cursor = None
            try:
                connection = Database.connect_mysql()
                cursor = connection.cursor()
                cursor.execute('DELETE FROM OFFICER WHERE officer_id = %s', (officer_id,))
                connection.commit()
            except Exception as e:
                raise e
            finally:
                if cursor is not None:
                    cursor.close()
                if connection is not None:
                    connection.close()

    class Cases:
        @staticmethod
        def add_case(case_data):
            connection = None
            cursor = None
            try:
                connection = Database.connect_mysql()
                cursor = connection.cursor()
                query = ("INSERT INTO `CASE` (case_id, case_type, status, date_reported, OFFICER_officer_id) "
                         "VALUES (%s, %s, %s, %s, %s)")
                cursor.execute(query, (case_data["case_id"], case_data["case_type"],
                                       case_data["status"], case_data["date_reported"],
                                       case_data["officer_id"]))
                connection.commit()
            except Exception as e:
                raise e
            finally:
                if cursor is not None:
                    cursor.close()
                if connection is not None:
                    connection.close()

        @staticmethod
        def edit_case(case_id, case_data):
            connection = None
            cursor = None
            try:
                connection = Database.connect_mysql()
                cursor = connection.cursor()
                query = ("UPDATE `CASE` SET case_type = %s, status = %s, "
                         "date_reported = %s, OFFICER_officer_id = %s WHERE case_id = %s")
                cursor.execute(query, (case_data["case_type"], case_data["status"],
                                       case_data["date_reported"], case_data["officer_id"], case_id))
                connection.commit()
            except Exception as e:
                raise e
            finally:
                if cursor is not None:
                    cursor.close()
                if connection is not None:
                    connection.close()

        @staticmethod
        def get_case(case_id):
            connection = None
            cursor = None
            try:
                connection = Database.connect_mysql()
                cursor = connection.cursor(dictionary=True)
                cursor.execute("SELECT * FROM `CASE` WHERE case_id = %s", (case_id,))
                return cursor.fetchone()
            except Exception as e:
                raise e
            finally:
                if cursor is not None:
                    cursor.close()
                if connection is not None:
                    connection.close()

        @staticmethod
        def get_cases():
            connection = None
            cursor = None
            try:
                connection = Database.connect_mysql()
                cursor = connection.cursor(dictionary=True)
                cursor.execute("SELECT * FROM `CASE`")
                return cursor.fetchall()
            except Exception as e:
                raise e
            finally:
                if cursor is not None:
                    cursor.close()
                if connection is not None:
                    connection.close()

        @staticmethod
        def delete_case(case_id):
            connection = None
            cursor = None
            try:
                connection = Database.connect_mysql()
                cursor = connection.cursor()
                cursor.execute("DELETE FROM `CASE` WHERE case_id = %s", (case_id,))
                connection.commit()
            except Exception as e:
                raise e
            finally:
                if cursor is not None:
                    cursor.close()
                if connection is not None:
                    connection.close()