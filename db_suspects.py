from database import Database


class DB_Suspects:
    @staticmethod
    def get_suspects():
        connection = None
        cursor = None
        try:
            connection = Database.connect_mysql()
            cursor = connection.cursor(dictionary=True)
            cursor.execute('SELECT * FROM suspect')
            return cursor.fetchall()
        except Exception as e:
            raise e
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()

    @staticmethod
    def get_suspect(suspect_id):
        connection = None
        cursor = None
        try:
            connection = Database.connect_mysql()
            cursor = connection.cursor(dictionary=True)
            cursor.execute('''
            SELECT * FROM suspect
            WHERE suspect_id = %s
            ''', (suspect_id,))
            rs = cursor.fetchone()
            if rs is None:
                raise Exception(f'Suspect ID {suspect_id} does not exist')
            return rs
        except Exception as e:
            raise e
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()

    @staticmethod
    def get_suspects_by_case(case_id):
        connection = None
        cursor = None
        try:
            connection = Database.connect_mysql()
            cursor = connection.cursor(dictionary=True)
            cursor.execute('''
            SELECT s.* FROM suspect s
            INNER JOIN accused_in a ON s.suspect_id = a.SUSPECT_suspect_id
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
    def get_suspects_not_in_case(case_id):
        connection = None
        cursor = None
        try:
            connection = Database.connect_mysql()
            cursor = connection.cursor(dictionary=True)
            cursor.execute('''
            SELECT s1.*
            FROM suspect s1
            EXCEPT
            SELECT s2.*
            FROM suspect s2
            INNER JOIN accused_in a ON s2.suspect_id = a.SUSPECT_suspect_id
            WHERE a.CASE_case_id = %s
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
    def get_suspects_by_name(name):
        connection = None
        cursor = None
        try:
            connection = Database.connect_mysql()
            cursor = connection.cursor(dictionary=True)
            cursor.execute(f'''
            SELECT * FROM suspect s
            WHERE s.name like "%{name}%"
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
    def add_suspect(suspect):
        connection = None
        cursor = None
        try:

            connection = Database.connect_mysql()
            cursor = connection.cursor()
            cursor.execute(
                '''
                INSERT INTO suspect (suspect_id, name, date_of_birth)
                VALUES (%s, %s, %s)
                ''',
                (int(suspect['suspect_id']), suspect["name"], suspect["date_of_birth"]))
            connection.commit()
        except Exception as e:
            raise e
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()

    @staticmethod
    def add_suspect_to_case(suspect_id, case_id):
        connection = None
        cursor = None
        try:
            connection = Database.connect_mysql()
            cursor = connection.cursor(dictionary=True)
            cursor.execute('''
                INSERT INTO accused_in (SUSPECT_suspect_id, CASE_case_id) VALUES (%s, %s)
            ''', (suspect_id, case_id))
            connection.commit()
        except Exception as e:
            raise e
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()

    @staticmethod
    def delete_suspect_from_case(suspect_id, case_id):
        connection = None
        cursor = None
        try:
            connection = Database.connect_mysql()
            cursor = connection.cursor(dictionary=True)
            cursor.execute('''
                DELETE FROM accused_in
                WHERE
                SUSPECT_suspect_id = %s
                AND
                CASE_case_id = %s
            ''', (suspect_id, case_id))
            connection.commit()
        except Exception as e:
            raise e
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()

    @staticmethod
    def edit_suspect(suspect_id, suspect):
        connection = None
        cursor = None
        try:
            connection = Database.connect_mysql()
            cursor = connection.cursor()
            cursor.execute(
                '''
                UPDATE suspect
                SET name = %s, date_of_birth = %s
                WHERE suspect_id = %s''',
                (suspect["name"], suspect["date_of_birth"], int(suspect_id)))
            connection.commit()
        except Exception as e:
            raise e
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()

    @staticmethod
    def delete_suspect(suspect_id):
        connection = None
        cursor = None
        try:
            connection = Database.connect_mysql()
            cursor = connection.cursor()
            cursor.execute('''
            DELETE FROM suspect
            WHERE suspect_id = %s''', (suspect_id,))
            connection.commit()
        except Exception as e:
            raise e
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()
