import unittest
from data.metadata import Metadata
from http.www_auth.AirnetRouter import AirnetRouter


class AirnetRouterTest(unittest.TestCase):
    def test_one(self):
        data = {'header': {'www_authenticate': '"Basic realm=""AIRNET Wireless N Router AIR-RT300GNH"""'}}
        metadata = AirnetRouter().process(data, Metadata())

        self.assertEqual(metadata.device.manufacturer, 'Airnet')
        self.assertEqual(metadata.device.product, 'AIR-RT300GNH')
        self.assertEqual(metadata.device.type, 'Wireless Router')


if __name__ == '__main__':
    unittest.main()