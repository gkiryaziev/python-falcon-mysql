import falcon
import json


class ReadJson():
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = "Test Ok"

    def on_post(self, req, resp):
        try:
            raw_json = req.stream.read()
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400, 'Error', ex.message)

        try:
            result_json = json.loads(raw_json.decode('utf8'))
        except ValueError:
            raise falcon.HTTPError(falcon.HTTP_400, 'Bad format of JSON')

        resp.status = falcon.HTTP_202
        resp.body = json.dumps(result_json, ensure_ascii=False)