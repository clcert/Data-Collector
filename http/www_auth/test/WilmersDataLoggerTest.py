import unittest
from data.metadata import Metadata
from http.www_auth.WilmersDataLogger import WilmersDataLogger


class WilmersDataLoggerTest(unittest.TestCase):
    def test_one(self):
        data = {'header': {'www_authenticate': '"Basic realm=""NDL485-2159917979"""'}}
        metadata = WilmersDataLogger().process(data, Metadata())

        self.assertEqual(metadata.device.manufacturer, 'Wilmers')
        self.assertEqual(metadata.device.product, 'blueberry NDL 485')
        self.assertEqual(metadata.device.type, 'Data Logger')


if __name__ == '__main__':
    unittest.main()