import unittest
from data.metadata import Metadata
from http.www_auth.LevelOneNVR import LevelOneNVR


class LevelOneNVRTest(unittest.TestCase):
    def test_one(self):
        data = {'header': {'www_authenticate': '"Basic realm=""NVR-0216  16-CH"""'}}
        metadata = LevelOneNVR().process(data, Metadata())

        self.assertEqual(metadata.device.manufacturer, 'Level One')
        self.assertEqual(metadata.device.product, 'NVR-0216')
        self.assertEqual(metadata.device.type, 'DVR')


if __name__ == '__main__':
    unittest.main()