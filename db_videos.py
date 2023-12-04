from database import Database


class DB_Videos:
    @staticmethod
    def get_videos():
        connection = None
        cursor = None
        try:
            connection = Database.connect_mysql()
            cursor = connection.cursor(dictionary=True)
            cursor.execute('SELECT * FROM video')
            return cursor.fetchall()
        except Exception as e:
            raise e
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()

    @staticmethod
    def get_video(video_id):
        connection = None
        cursor = None
        try:
            connection = Database.connect_mysql()
            cursor = connection.cursor(dictionary=True)
            cursor.execute('''
                SELECT * FROM video
                WHERE video_id = %s
                ''', (video_id,))
            rs = cursor.fetchone()
            if rs is None:
                raise Exception(f'Victim ID {video_id} does not exist')
            return rs
        except Exception as e:
            raise e
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()

    @staticmethod
    def get_videos_by_body_cam(body_cam_id):
        connection = None
        cursor = None
        try:
            connection = Database.connect_mysql()
            cursor = connection.cursor(dictionary=True)
            cursor.execute('''
                SELECT * FROM video v
                WHERE v.BODY_CAM_body_cam_id = %s
                ''', (body_cam_id,))
            return cursor.fetchall()
        except Exception as e:
            raise e
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()

    @staticmethod
    def add_video(video):
        connection = None
        cursor = None
        try:

            connection = Database.connect_mysql()
            cursor = connection.cursor()
            cursor.execute(
                '''
                INSERT INTO video (video_id, link, size, recording_date, BODY_CAM_body_cam_id)
                VALUES (%s, %s, %s, %s, %s)''',
                (int(video['video_id']), video["link"], video["size"],
                 video["recording_date"], video['BODY_CAM_body_cam_id']))
            connection.commit()
        except Exception as e:
            raise e
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()

    @staticmethod
    def edit_video(video_id, video):
        connection = None
        cursor = None
        try:
            connection = Database.connect_mysql()
            cursor = connection.cursor()
            cursor.execute(
                '''
                UPDATE video
                SET link = %s, size = %s,
                recording_date = %s, BODY_CAM_body_cam_id = %s
                WHERE video_id = %s''',
                (video["link"], video["size"],
                 video["recording_date"], video['BODY_CAM_body_cam_id'],
                 int(video_id)))
            connection.commit()
        except Exception as e:
            raise e
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()

    @staticmethod
    def delete_video(video_id):
        connection = None
        cursor = None
        try:
            connection = Database.connect_mysql()
            cursor = connection.cursor()
            cursor.execute('''
                DELETE FROM video
                WHERE video_id = %s''', (video_id,))
            connection.commit()
        except Exception as e:
            raise e
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()
