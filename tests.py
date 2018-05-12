from unittest import main, TestCase
from settings import TOKEN
from yadiskapi import Disk

class TestDiskApi(TestCase):
    def setUp(self):
        self.disk = Disk(token=TOKEN)

    def test_get_info(self):
        info = self.disk.get_info()
        self.assertEqual(info.get('error'), None,
                         'Ошибка при вызове функции get_info: {}'.format(info.get('message')))

    def test_get_resources_metainfo(self):
        info = self.disk.get_resources_metainfo('app:/')
        self.assertEqual(info.get('error'), None,
                         'Ошибка при вызове функции get_resources_metainfo: {}'.format(info.get('message')))

if __name__ == '__main__':
    main()