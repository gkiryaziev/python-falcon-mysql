import falcon
import json


class Index():
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps([{"message": "Привет Мир !!!"}], ensure_ascii=False)
