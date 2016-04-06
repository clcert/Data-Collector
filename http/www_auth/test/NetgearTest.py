import unittest

from data.metadata import Metadata
from http.www_auth.Netgear import Netgear


class NetgearTest(unittest.TestCase):
    def test(self):
        data = {'header': {'www_authenticate': '"Basic realm=""Netgear"""'}}
        metadata = Netgear().process(data, Metadata())

        self.assertEqual(metadata.device.manufacturer, 'Netgear')


if __name__ == '__main__':
    unittest.main()
