import unittest
from data.metadata import Metadata
from http.www_auth.AirLinkCamera import AirLinkCamera


class AirLinkCameraTest(unittest.TestCase):
    def test_one(self):
        data = {'header': {'www_authenticate': '"Basic realm=""SkyIPCam""'}}
        metadata = AirLinkCamera().process(data, Metadata())

        self.assertEqual(metadata.device.manufacturer, 'AirLink')
        self.assertEqual(metadata.device.type, 'Camera')


if __name__ == '__main__':
    unittest.main()