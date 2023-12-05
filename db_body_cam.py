from database import Database


class DB_BodyCam:
    @staticmethod
    def add_body_cam(body_cam_data):
        connection = None
        cursor = None
        try:
            connection = Database.connect_mysql()
            cursor = connection.cursor()
            query = ('''
                INSERT INTO body_cam (body_cam_id, serial_number, model)
                VALUES (%s, %s, %s)
                ''')
            cursor.execute(query,
                           (body_cam_data["body_cam_id"], body_cam_data["serial_number"], body_cam_data["model"]))
            connection.commit()
        except Exception as e:
            raise e
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()

    @staticmethod
    def edit_body_cam(body_cam_id, body_cam_data):
        connection = None
        cursor = None
        try:
            connection = Database.connect_mysql()
            cursor = connection.cursor()

            cursor.execute('''
            UPDATE body_cam
            SET serial_number = %s, model = %s
            WHERE body_cam_id = %s
            ''', (body_cam_data["serial_number"], body_cam_data["model"], body_cam_id))

            connection.commit()
        except Exception as e:
            raise e
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()

    @staticmethod
    def get_body_cam(body_cam_id):
        connection = None
        cursor = None
        try:
            connection = Database.connect_mysql()
            cursor = connection.cursor(dictionary=True)
            cursor.execute('''
            SELECT * FROM `body_cam`
            WHERE body_cam_id = %s''', (body_cam_id,))
            rs = cursor.fetchone()
            if rs is None:
                raise Exception(f'body cam ID {body_cam_id} does not exist')
            return rs
        except Exception as e:
            raise e
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()

    @staticmethod
    def get_body_cam_by_video_id(video_id):
        connection = None
        cursor = None
        try:
            connection = Database.connect_mysql()
            cursor = connection.cursor(dictionary=True)
            cursor.execute('''
            SELECT b.* FROM `body_cam` b
            INNER JOIN video v on v.BODY_CAM_body_cam_id=b.body_cam_id
            WHERE v.video_id = %s''', (video_id,))
            rs = cursor.fetchone()
            if rs is None:
                raise Exception(f'body cam ID {video_id} does not exist')
            return rs
        except Exception as e:
            raise e
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()

    @staticmethod
    def get_body_cams():
        connection = None
        cursor = None
        try:
            connection = Database.connect_mysql()
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM body_cam")
            return cursor.fetchall()
        except Exception as e:
            raise e
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()

    @staticmethod
    def get_free_body_cams():
        connection = None
        cursor = None
        try:
            connection = Database.connect_mysql()
            cursor = connection.cursor(dictionary=True)
            cursor.execute(
                "SELECT * FROM body_cam WHERE body_cam_id NOT IN (SELECT o.BODY_CAM_body_cam_id from officer o);")
            return cursor.fetchall()
        except Exception as e:
            raise e
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()

    @staticmethod
    def get_body_cam_for_officer(officer_id):
        connection = None
        cursor = None
        try:
            connection = Database.connect_mysql()
            cursor = connection.cursor(dictionary=True)
            cursor.execute('''
            SELECT b.* FROM body_cam b
            inner join officer o on b.body_cam_id = o.BODY_CAM_body_cam_id
            where o.officer_id = %s
            ''', (officer_id,))
            return cursor.fetchone()
        except Exception as e:
            raise e
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()

    @staticmethod
    def delete_body_cam(body_cam_id):
        connection = None
        cursor = None
        try:
            connection = Database.connect_mysql()
            cursor = connection.cursor()
            cursor.execute('''
            DELETE FROM body_cam
            WHERE body_cam_id = %s''', (body_cam_id,))
            connection.commit()
        except Exception as e:
            raise e
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()
