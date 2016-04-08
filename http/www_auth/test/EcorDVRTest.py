import unittest
from data.metadata import Metadata
from http.www_auth.EcorDVR import EcorDVR


class EcorDVRTest(unittest.TestCase):
    def test_one(self):
        data = {'header': {
            'www_authenticate': '"Digest qop=""auth"", stale=false, algorithm=MD5, '
                                'realm=""ECOR264-9X1"", nonce=""1457683803"""'}}
        metadata = EcorDVR().process(data, Metadata())

        self.assertEqual(metadata.device.manufacturer, 'EverFocus')
        self.assertEqual(metadata.device.product, 'ECOR264-9X1')
        self.assertEqual(metadata.device.type, 'DVR')


if __name__ == '__main__':
    unittest.main()