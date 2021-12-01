import sqlite3


# Connection
class Database:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.get_conn()
        self.create_database()

    # instance of connection to optimize
    def get_conn(self):
        conn = sqlite3.connect('boreal_app.db')
        cursor = conn.cursor()
        self.conn = conn
        self.cursor = cursor

    # create database, table and fields on start app
    def create_database(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS user (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,username,password)")
        # self.cursor.execute(
        #     "CREATE TABLE IF NOT EXISTS user_token (id INTEGER NOT NULL PRIMARY KEY, token)")
        self.conn.commit()
        self.cursor.close()

    # def to insert any data in any column, since data and column are corects
    # exemple: insert_data(id,token) - its possible manipulate more than one table
    def insert_data(self, table_name: str, fields: tuple, data: tuple):
        """
        :param table_name:
        :param fields:
        :param data:
        :return:
        """
        query = "INSERT INTO %s %s VALUES %s;" % (table_name, fields, data)
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(query)
            self.conn.commit()
            self.cursor.close()

        except Exception as error:
            raise sqlite3.Error(error)

        return self.cursor.lastrowid

    # return data of a specific user
    def get_user_data(self, data: str):
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM user WHERE username=:name", {"name": data})
        result = self.cursor.fetchall()
        self.cursor.close()
        if result:
            return result[0][0], result[0][1], result[0][2]

        return result

