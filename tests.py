from unittest import main, TestCase
from settings import TOKEN
from yadiskapi import Disk

class TestDiskApi(TestCase):
    def setUp(self):
        self.disk = Disk(token=TOKEN)

    def test_get_info(self):
        response = self.disk.get_info()
        self.assertEqual(response.get('error'), None,
                         'Ошибка при вызове функции get_info: {}'.format(response.get('message')))

    def test_get_resources_metainfo(self):
        response = self.disk.get_resources_metainfo('app:/')
        self.assertEqual(response.get('error'), None,
                         'Ошибка при вызове функции get_resources_metainfo: {}'.format(response.get('message')))

    def test_create_and_delete_dir(self):
        response = self.disk.create_dir('app:/test')
        self.assertEqual(response.get('error'), None,
                         'Ошибка при вызове функции create_dir: {}'.format(response.get('message')))
        response = self.disk.delete_dir('app:/test')
        self.assertEqual(response.get('error'), None,
                         'Ошибка при вызове функции delete_dir: {}'.format(response.get('message')))

    def test_change_resources_metainfo(self):
        self.disk.create_dir('app:/test')
        response = self.disk.change_resources_metainfo('app:/test', {'test1': '1', 'test2': '2'})
        self.assertEqual(response.get('error'), None,
                         'Ошибка при вызове функции change_resources_metainfo: {}'.format(response.get('message')))
        self.disk.delete_dir('app:/test')

    def test_copy_resources(self):
        self.disk.create_dir('app:/test')
        response = self.disk.copy_resources('app:/test', 'app:/test1')
        self.assertEqual(response.get('error'), None,
                         'Ошибка при вызове функции copy_resources: {}'.format(response.get('message')))
        self.disk.delete_dir('app:/test')
        self.disk.delete_dir('app:/test1')

    def test_download(self):
        self.disk.create_dir('app:/test')
        response = self.disk.download('app:/test')
        self.assertEqual(response.get('error'), None,
                         'Ошибка при вызове функции download: {}'.format(response.get('message')))
        self.disk.delete_dir('app:/test')

    def test_get_files(self):
        response = self.disk.get_files(media_type='image', offset=0, preview_size='100x100', sort='resource_id')
        self.assertEqual(response.get('error'), None,
                         'Ошибка при вызове функции get_files: {}'.format(response.get('message')))

if __name__ == '__main__':
    main()