import requests
from .auth import check_http_return, generate_api_session


class Call:
    def __init__(self, host, client_id, client_secret, params):
        self.host = host
        self.token = generate_api_session(host, client_id, client_secret)
        self.params = params

        self.headers = {
            'Authorization': 'Bearer {}'.format(self.token),
        }

    def refreshToken(self):
        self.token = generate_api_session(self.host, self.client_id, self.client_secret)

    def getPerformance(self, limit=100, offset=0):
        api_url = 'https://{}/api/v1/devices/performance?offset={}&limit={}'.format(self.host, offset, limit)

        r = requests.get(api_url, headers=self.headers, params=self.params, verify=False)
        check_http_return("API", api_url, r.status_code, r)
        return r.json()

    def getDevices(self, limit=100, offset=0):
        api_url = 'https://{}/api/v1/devices?offset={}&limit={}'.format(self.host, offset, limit)

        r = requests.get(api_url, headers=self.headers, params={}, verify=False)
        check_http_return("API", api_url, r.status_code, r)
        return r.json()
