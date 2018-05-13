from unittest import main, TestCase
from settings import TOKEN
from yadiskapi import Disk, DiskException
from contextlib import contextmanager
from collections import OrderedDict


class TestDiskApi(TestCase):
    def setUp(self):
        self.disk = Disk(token=TOKEN)

    @contextmanager
    def assertNotRaises(self, funct_name, exception, prepare=None, fin=None):
        if prepare:
            for func, params in prepare.items():
                func(*params)
        try:
            yield None
        except exception as e:
            raise self.failureException('Ошибка при вызове функции: {}, {}'.format(funct_name, e))
        finally:
            if fin:
                for func, params in fin.items():
                    func(*params)

    def test_get_info(self):
        with self.assertNotRaises('get_info', DiskException):
            self.disk.get_info()

    def test_get_resources_metainfo(self):
        with self.assertNotRaises('get_resources_metainfo', DiskException):
            self.disk.get_resources_metainfo('app:/')

    def test_create_and_delete_resources(self):
        with self.assertNotRaises('create_dir', DiskException):
            self.disk.create_dir('app:/test')
        with self.assertNotRaises('delete_resources', DiskException):
            self.disk.delete_resources('app:/test')

    def test_change_resources_metainfo(self):
        with self.assertNotRaises('change_resources_metainfo', DiskException,
                                  prepare={self.disk.create_dir: ('app:/test',)},
                                  fin={self.disk.delete_resources: ('app:/test',)}):
            self.disk.change_resources_metainfo('app:/test', {'test1': '1', 'test2': '2'})

    def test_copy_resources(self):
        with self.assertNotRaises('copy_resources', DiskException,
                                  prepare={self.disk.create_dir: ('app:/test',)},
                                  fin={self.disk.delete_resources: ('app:/test',)}):
            self.disk.copy_resources('app:/test', 'app:/test1')
        self.disk.delete_resources('app:/test1')

    def test_download(self):
        with self.assertNotRaises('download', DiskException,
                                  prepare={self.disk.create_dir: ('app:/test',)},
                                  fin={self.disk.delete_resources: ('app:/test',)}):
            self.disk.download('app:/test')

    def test_get_files(self):
        with self.assertNotRaises('get_files', DiskException):
            self.disk.get_files(media_type='image', offset=0, preview_size='100x100', sort='resource_id')

    def test_move(self):
        with self.assertNotRaises('move', DiskException, prepare={self.disk.create_dir: ('app:/test',)},
                                  fin={self.disk.delete_resources: ('app:/test1',)}):
            self.disk.move('app:/test', 'app:/test1', owerwrite=True)

    def test_get_public_resources(self):
        with self.assertNotRaises('get_public_resources', DiskException):
            self.disk.get_public_resources(resources_type='dir', preview_size='100x100')

    def test_publish_resources(self):
        with self.assertNotRaises('publish_resources', DiskException, prepare={self.disk.create_dir: ('app:/test',)},
                                  fin={self.disk.delete_resources: ('app:/test',)}):
            self.disk.publish_resources('app:/test')

    def test_unpublish_resources(self):
        with self.assertNotRaises('unpublish_resources', DiskException,
                                  prepare=OrderedDict(((self.disk.create_dir, ('app:/test',)),
                                                      (self.disk.publish_resources, ('app:/test',)))),
                                  fin={self.disk.delete_resources: ('app:/test',)}):
            self.disk.unpublish_resources('app:/test')

    def test_upload(self):
        with self.assertNotRaises('upload', DiskException):
            self.disk.upload('app:/test')


if __name__ == '__main__':
    main()
