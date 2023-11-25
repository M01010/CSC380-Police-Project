import mysql.connector


class Database:

    @staticmethod
    def connect_mysql():
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="policedb"
        )
        return connection
