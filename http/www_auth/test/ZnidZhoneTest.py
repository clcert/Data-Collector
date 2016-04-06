import unittest

from data.metadata import Metadata
from http.www_auth.ZnidZhone import ZnidZhone


class ZnidZhoneTest(unittest.TestCase):
    def test(self):
        data = {'header': {'www_authenticate': '"Basic realm=""ZNID24xx-Router"""'}}
        metadata = ZnidZhone().process(data, Metadata())

        self.assertEqual(metadata.device.product, 'zNID 24xx Series')
        self.assertEqual(metadata.device.manufacturer, 'Zhone')


if __name__ == '__main__':
    unittest.main()