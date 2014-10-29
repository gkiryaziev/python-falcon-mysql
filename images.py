import falcon


class Resource(object):
    def on_get(self, req, resp):
        resp.body = "Hello from <b>Images</b>!"
        resp.status = falcon.HTTP_200

