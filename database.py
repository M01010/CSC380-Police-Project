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
