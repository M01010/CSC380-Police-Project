from database import Database


class DB_Officers:
    @staticmethod
    def add_officer(officer):
        connection = None
        cursor = None
        try:
            connection = Database.connect_mysql()
            cursor = connection.cursor()
            cursor.execute(
                '''
                INSERT INTO OFFICER (officer_id, name, badge_number, rank , date_of_birth, BODY_CAM_body_cam_id)
                VALUES (%s, %s, %s, %s ,%s, %s)
                ''',
                (int(officer["officer_id"]), officer["name"], officer["badge_number"], officer["rank"],
                 officer["date_of_birth"], officer['BODY_CAM_body_cam_id']))
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
            cursor.execute('''
            SELECT *
            FROM OFFICER
            WHERE officer_id = %s''', (officer_id,))
            rs = cursor.fetchone()
            if rs is None:
                raise Exception(f'Officer ID {officer_id} does not exist')
            return rs
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
                '''
                UPDATE OFFICER
                SET name = %s, badge_number = %s,
                rank = %s, date_of_birth = %s,
                BODY_CAM_body_cam_id = %s
                WHERE officer_id = %s''',
                (officer["name"], officer["badge_number"],
                 officer["rank"], officer["date_of_birth"],
                 officer['BODY_CAM_body_cam_id'],
                 int(officer_id))
            )
            connection.commit()
        except Exception as e:
            raise e
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()

    @staticmethod
    def get_officers_by_name(name):
        connection = None
        cursor = None
        try:
            connection = Database.connect_mysql()
            cursor = connection.cursor(dictionary=True)
            cursor.execute(f'''
            SELECT * FROM officer o
            WHERE o.name like "%{name}%"
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
    def delete_officer(officer_id):
        connection = None
        cursor = None
        try:
            connection = Database.connect_mysql()
            cursor = connection.cursor()
            cursor.execute('''
            DELETE FROM OFFICER
            WHERE officer_id = %s''', (officer_id,))
            connection.commit()
        except Exception as e:
            raise e
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()
