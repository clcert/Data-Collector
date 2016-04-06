import unittest

from data.metadata import Metadata
from http.www_auth.Thomson import Thomson


class ThomsonTest(unittest.TestCase):
    def test(self):
        data = {'header': {'www_authenticate': '"Digest realm=""Thomson Gateway"", nonce=""0821SF62J:00-1F-9F-11-C3-E6'
                                               ':483607:528393"", qop=""auth"",Basic realm=""Thomson Gateway"""'}}
        metadata = Thomson().process(data, Metadata())

        self.assertEqual(metadata.device.manufacturer, 'Alcatel')
        self.assertEqual(metadata.device.type, 'DSL Modem')


if __name__ == '__main__':
    unittest.main()
