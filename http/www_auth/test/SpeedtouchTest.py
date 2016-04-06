import unittest

from data.metadata import Metadata
from http.www_auth.Speedtouch import Speedtouch


class SpeedtouchTest(unittest.TestCase):
    def test(self):
        data = {'header': {'www_authenticate': '"Digest realm=""SpeedTouch"", nonce=""0742JTNWA:00-14-7F-E5-92-37'
                                               ':33189:634512"", qop=""auth"",Basic realm=""SpeedTouch"""'}}
        metadata = Speedtouch().process(data, Metadata())

        self.assertEqual(metadata.device.manufacturer, 'Alcatel')
        self.assertEqual(metadata.device.type, 'DSL Modem')


if __name__ == '__main__':
    unittest.main()
