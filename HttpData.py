import urllib3
import json

class HttpData:
    """
    Toms Http library.
    """

    def __init__(self):
        http = urllib3.PoolManager()

    def GET(self, url, data_type):
        if data_type == "json":
            req = self.http.request('GET', url)
            rtn_data = json.loads(req.data.decode('utf-8'))
            return rtn_data