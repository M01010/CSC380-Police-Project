from database import Database


class DB_Cases:
    @staticmethod
    def add_case(case_data):
        connection = None
        cursor = None
        try:
            connection = Database.connect_mysql()
            cursor = connection.cursor()
            query = (
                '''
                INSERT INTO `CASE` (case_id, case_type, status, date_reported, OFFICER_officer_id)
                VALUES (%s, %s, %s, %s, %s)''')
            cursor.execute(query,
                           (case_data["case_id"], case_data["case_type"], case_data["status"],
                            case_data["date_reported"], case_data["officer_id"]))
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
            query = ('''
            UPDATE `CASE` SET case_type = %s, status = %s,
            date_reported = %s, OFFICER_officer_id = %s
            WHERE case_id = %s''')
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
            cursor.execute('''
            SELECT * FROM `CASE`
            WHERE case_id = %s''', (case_id,))
            rs = cursor.fetchone()
            if rs is None:
                raise Exception(f'Case ID {case_id} does not exist')
            return rs
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
            cursor.execute('''
            DELETE FROM `CASE`
            WHERE case_id = %s''', (case_id,))
            connection.commit()
        except Exception as e:
            raise e
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()
