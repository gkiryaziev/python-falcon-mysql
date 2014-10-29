import json
import falcon
from mysql_libs import mysql_data


class FindAll():
    def on_get(self, req, resp):
        md = mysql_data.MySQLData()
        md.connect_to_db('localhost', 'admin', 'admin', 'phones_nv')

        result = md.get_data('select * from maindb')

        resp.set_header('Content-Type', 'application/json; charset=utf-8')
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(result, ensure_ascii=False)

        md.disconnect_from_db()