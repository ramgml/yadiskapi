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
        """Возвращает информацию о диске"""
        response = requests.get(url='{}disk'.format(self.api_url), headers=self.headers)
        if response.status_code != 200:
            raise DiskException(response.json())
        return response.json()

    def get_resources_metainfo(self, path):
        """Возвращает мета-информацию о ресурсе"""
        response = requests.get(url='{}disk/resources'.format(self.api_url), params={'path': path},
                                headers=self.headers)
        if response.status_code != 200:
            raise DiskException(response.json())
        return response.json()

    def create_dir(self, path):
        """Создает папку"""
        response = requests.put(url='{}disk/resources'.format(self.api_url), params={'path': path},
                                headers=self.headers)
        if response.status_code != 201:
            raise DiskException(response.json())
        return response.json()

    def delete_resources(self, path):
        """Удаляет папку"""
        response = requests.delete(url='{}disk/resources'.format(self.api_url), params={'path': path},
                                   headers=self.headers)
        if response.status_code not in [202, 204]:
            raise DiskException(response.json())
        return {'success': True}

    def change_resources_metainfo(self, path, custom_properties):
        """Изменяет метаинформацию о ресурсе
        custom_properties - словарь, где ключ - имя поля в виде строки"""
        response = requests.patch(url='{}disk/resources'.format(self.api_url),
                                  params={'path': path, 'custom_properties': custom_properties}, headers=self.headers)
        if response.status_code != 200:
            raise DiskException(response.json())
        return response.json()

    def copy_resources(self, from_resource, path_to_copy, force_async=False, owerwrite=False):
        """Копирует ресурс"""
        response = requests.post(url='{}disk/resources/copy'.format(self.api_url),
                                 params={'from': from_resource, 'path': path_to_copy, 'force_async': force_async,
                                         'owerwrite': owerwrite},
                                 headers=self.headers)
        if response.status_code not in [201, 202]:
            raise DiskException(response.json())
        return response.json()

    def download(self, path):
        """Возвращает ссылку на скачивание файла или папки"""
        response = requests.get(url='{}disk/resources/download'.format(self.api_url),
                                params={'path': path}, headers=self.headers)
        if response.status_code != 200:
            raise DiskException(response.json())
        return response.json()

    def get_files(self, media_type=None, preview_size=None, sort=None, limit=20, preview_crop=False, offset=0):
        """Возвращает список файлов
        media_type принимает следующие значения:
            audio — аудио-файлы.
            backup — файлы резервных и временных копий.
            book — электронные книги.
            compressed — сжатые и архивированные файлы.
            data — файлы с базами данных.
            development — файлы с кодом (C++, Java, XML и т. п.), а также служебные файлы IDE.
            diskimage — образы носителей информации и сопутствующие файлы (например, ISO и CUE).
            document — документы офисных форматов (Word, OpenOffice и т. п.).
            encoded — зашифрованные файлы.
            executable — исполняемые файлы.
            flash — файлы с флэш-видео или анимацией.
            font — файлы шрифтов.
            image — изображения.
            settings — файлы настроек для различных программ.
            spreadsheet — файлы офисных таблиц (Excel, Numbers, Lotus).
            text — текстовые файлы.
            unknown — неизвестный тип.
            video — видео-файлы.
            web — различные файлы, используемые браузерами и сайтами (CSS, сертификаты, файлы закладок).
        sort принимает следующие значения:
            resource_id — Идентификатор ресурса,
            size — Размер файла,
            media_type — Определённый Диском тип файла,
            sha256 — SHA256-хэш,
            revision — Ревизия Диска в которой этот ресурс был изменён последний раз,
            path — Путь к ресурсу,
            md5 — MD5-хэш,
            name — Имя,
            created — Дата создания,
            modified — Дата изменения"""
        response = requests.get(url='{}disk/resources/files'.format(self.api_url),
                                params={'media_type': media_type, 'offset': offset, 'preview_size': preview_size,
                                        'sort': sort, 'limit': limit, 'preview_crop': preview_crop},
                                headers=self.headers)
        if response.status_code != 200:
            raise DiskException(response.json())
        return response.json()

    def move(self, from_resource, path_to_copy, force_async=False, owerwrite=False):
        """Перемещает ресурс по указанному пути"""
        response = requests.post(url='{}disk/resources/move'.format(self.api_url),
                                 params={'from': from_resource, 'path': path_to_copy, 'force_async': force_async,
                                         'owerwrite': owerwrite},
                                 headers=self.headers)
        if response.status_code not in [201, 202]:
            raise DiskException(response.json())
        return response.json()

    def get_public_resources(self, resources_type, preview_size, offset=0, limit=20, preview_crop=False, ):
        """Возвращает список опубликованных ресурсов
        resources_type принимает следующие значения:
            file
            dir"""
        response = requests.get(url='{}disk/resources/public'.format(self.api_url),
                                params={'offset': offset, 'preview_size': preview_size,
                                        'limit': limit, 'preview_crop': preview_crop, 'type': resources_type},
                                headers=self.headers)
        if response.status_code != 200:
            raise DiskException(response.json())
        return response.json()

    def publish_resources(self, path):
        """Опубликовать ресурс"""
        response = requests.put(url='{}disk/resources/publish'.format(self.api_url), params={'path': path},
                                headers=self.headers)
        if response.status_code != 200:
            raise DiskException(response.json())
        return response.json()

    def unpublish_resources(self, path):
        """Отменить публикацию ресурса"""
        response = requests.put(url='{}disk/resources/unpublish'.format(self.api_url), params={'path': path},
                                headers=self.headers)
        if response.status_code != 200:
            raise DiskException(response.json())
        return response.json()

    def upload(self, path):
        """Получить ссылку для загрузки файла"""
        response = requests.get(url='{}disk/resources/upload'.format(self.api_url), params={'path': path},
                                headers=self.headers)
        if response.status_code != 200:
            raise DiskException(response.json())
        return response.json()
