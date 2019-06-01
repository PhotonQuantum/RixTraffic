import requests
import json


class RixCloud:
    base_url = "https://api.rixcloud.io/v2"
    def __init__(self, username, password):
        if isinstance(username, str) and isinstance(password, str):
            self.username = username
            self.password = password
        else:
            raise TypeError("username and password must be set to strs")
    def get_service_list(self):
        r = requests.get(self.base_url + "/profile/services", auth=(self.username, self.password))
        return r.text
    def get_nodes(self, service_id):
        if isinstance(service_id, int):
            r = requests.get(self.base_url + "/profile/service/%d/nodes" % (service_id), auth=(self.username, self.password))
            return json.loads(r.text)['data']
        else:
            raise TypeError("service_id must be set to an integer")
    def get_traffic(self, service_id):
        if isinstance(service_id, int):
            r = requests.get(self.base_url + "/profile/service/%d/traffic" % (service_id), auth=(self.username, self.password))
            return json.loads(r.text)['data']
    def get_traffic_log(self, service_id):
        if isinstance(service_id, int):
            r = requests.get(self.base_url + "/profile/service/%d/traffic/log" % (service_id), auth=(self.username, self.password))
            return json.loads(r.text)['data']

