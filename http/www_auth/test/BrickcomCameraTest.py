import unittest
from data.metadata import Metadata
from http.www_auth.BrickComCamera import BrickComCamera


class BrickComCameraTest(unittest.TestCase):
    def test_one(self):
        data = {'header': {'www_authenticate': '"Basic realm=""Brickcom MD-300Np-360P""" '}}
        metadata = BrickComCamera().process(data, Metadata())

        self.assertEqual(metadata.device.manufacturer, 'Brickcom')
        self.assertEqual(metadata.device.product, 'MD-300Np')
        self.assertEqual(metadata.device.type, 'Camera')


if __name__ == '__main__':
    unittest.main()