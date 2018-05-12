from settings import TOKEN
import requests


class DiskException(Exception):
    def __init__(self, json_obj):
        self.message = json_obj['message']
        self.description = json_obj['description']
        self.error = json_obj['error']


class Disk(object):
    def __init__(self, token, headers=None, version_api='v1'):
        self.token = token
        self.headers = {'Authorization': 'OAuth {}'.format(self.token)}
        if headers:
            self.headers.update(headers)
        self.version_api = version_api
        self.api_url = 'https://cloud-api.yandex.net/{}/'.format(version_api)

    def get_info(self):
        response = requests.get(url='{}disk'.format(self.api_url), headers=self.headers)
        if response.status_code != 200:
            raise DiskException(response.json())
        return response.json()

    def get_resources_metainfo(self, path):
        response = requests.get(url='{}disk/resources'.format(self.api_url), params={'path': path}, headers=self.headers)
        if response.status_code != 200:
            raise DiskException(response.json())
        return response.json()

if __name__ == '__main__':
    disk = Disk(token=TOKEN)
    print(disk.get_info())


