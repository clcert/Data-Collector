import unittest
from data.metadata import Metadata
from http.www_auth.SonyVideoCommunication import SonyVideoCommunication


class SonyVideoCommunicationTest(unittest.TestCase):
    def test_one(self):
        data = {'header': {'www_authenticate': ' "Basic realm=""PCS-G50 Web Control"""'}}
        metadata = SonyVideoCommunication().process(data, Metadata())

        self.assertEqual(metadata.device.manufacturer, 'Sony')
        self.assertEqual(metadata.device.product, 'PCS-G50')
        self.assertEqual(metadata.device.type, 'Video Communication System')


if __name__ == '__main__':
    unittest.main()