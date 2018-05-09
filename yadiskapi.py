from settings import TOKEN
import requests


headers = {'Authorization': 'OAuth {0}'.format(TOKEN)}
try:
    resp = requests.get(url='https://cloud-api.yandex.net/v1/disk/resources/upload',
                        params={'path': 'disk:/Приложения/<имя приложения>/doc'}, headers=headers)
    if resp.status_code != 200:
        print(resp.status_code)
        print(resp.json())
    ref = resp.json()['href']
    with open('<путь до файла>', 'rb') as upload:
        resp = requests.put(url=ref, data=upload.read())
        print(resp.status_code)
        print(resp.content)
except Exception as e:
    print(type(e))
    print(e)




