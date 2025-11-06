import requests
import config.settings as config

class Api:

    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint):
        url = self.base_url+"/"+str(endpoint)
        return requests.get(url)
    
    def post(self, endpoint, data):
        url = self.base_url+"/"+str(endpoint)
        return requests.post(url, json=data)
    
    def delete(self, endpoint, item):
        url = self.base_url+"/"+str(endpoint)+"/"+str(item)
        return requests.delete(url)
    
    def update(self, endpoint, data):
        url = self.base_url+"/"+str(endpoint)
        return requests.put(url, json=data)
    