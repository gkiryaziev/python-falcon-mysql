import mysql.connector
from mysql.connector import cursor


class MySQLData:
    pass

    conn = None

    def connect_to_db(self, host, uid, pwd, db):
        self.conn = mysql.connector.connect(host=host, user=uid, password=pwd, database=db)

    def get_data(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        result = []
        columns = tuple([i[0] for i in cursor.description])

        for row in cursor:
            result.append(dict(zip(columns, row)))

        cursor.close()
        return result

    def disconnect_from_db(self):
        self.conn.close()