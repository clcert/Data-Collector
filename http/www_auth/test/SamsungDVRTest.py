import unittest
from data.metadata import Metadata
from http.www_auth.SamsungDVR import SamsungDVR


class SamsungDVRTest(unittest.TestCase):
    def test_one(self):
        data = {'header': {'www_authenticate': '"Basic realm=""SAMSUNG DVR"""'}}
        metadata = SamsungDVR().process(data, Metadata())

        self.assertEqual(metadata.device.manufacturer, 'Samsung')
        self.assertEqual(metadata.device.type, 'DVR')


if __name__ == '__main__':
    unittest.main()