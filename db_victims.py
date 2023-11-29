from database import Database


class DB_Victims:
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
            cursor.execute('''
            SELECT * FROM VICTIM
            WHERE victim_id = %s
            ''', (victim_id,))
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
    def get_victims_by_case(case_id):
        connection = None
        cursor = None
        try:
            connection = Database.connect_mysql()
            cursor = connection.cursor(dictionary=True)
            cursor.execute('''
            SELECT * FROM victim v
            INNER JOIN affected_in a ON v.victim_id = a.VICTIM_victim_id
            INNER JOIN `case` c ON a.CASE_case_id = c.case_id
            WHERE c.case_id = %s
            ''', (case_id,))
            return cursor.fetchall()
        except Exception as e:
            raise e
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()

    @staticmethod
    def get_victims_by_name(name):
        connection = None
        cursor = None
        try:
            connection = Database.connect_mysql()
            cursor = connection.cursor(dictionary=True)
            cursor.execute(f'''
            SELECT * FROM victim v
            WHERE v.name like "%{name}%"
            ''')
            return cursor.fetchall()
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
                '''
                INSERT INTO VICTIM (victim_id, name, date_of_birth, contact_info)
                VALUES (%s, %s, %s, %s)
                ''',
                (int(victim['victim_id']), victim["name"], victim["date_of_birth"], victim["contact_info"]))
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
                '''
                UPDATE VICTIM
                SET name = %s, date_of_birth = %s, contact_info = %s
                WHERE victim_id = %s''',
                (victim["name"], victim["date_of_birth"], victim["contact_info"], int(victim_id)))
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
            cursor.execute('''
            DELETE FROM VICTIM
            WHERE victim_id = %s''', (victim_id,))
            connection.commit()
        except Exception as e:
            raise e
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()
