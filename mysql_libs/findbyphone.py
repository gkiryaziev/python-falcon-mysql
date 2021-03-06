import json
import falcon
from mysql_libs import mysql_data


class FindByPhone():
    def on_get(self, req, resp, user_phone):
        md = mysql_data.MySQLData()
        md.connect_to_db('localhost', 'admin', 'admin', 'phones_nv')

        result = md.get_data('select * from maindb where phone = ' + user_phone)

        resp.set_header('Content-Type', 'application/json; charset=utf-8')
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(result, ensure_ascii=False)

        md.disconnect_from_db()