import unittest
from data.metadata import Metadata
from http.www_auth.BelkinNetCam import BelkinNetCam


class BelkinNetCamTest(unittest.TestCase):
    def test_one(self):
        data = {'header': {'www_authenticate': '"Basic realm=""Netcam"""'}}
        metadata = BelkinNetCam().process(data, Metadata())

        self.assertEqual(metadata.device.manufacturer, 'Belkin')
        self.assertEqual(metadata.device.type, 'Camera')


if __name__ == '__main__':
    unittest.main()