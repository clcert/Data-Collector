import unittest
from data.metadata import Metadata
from http.www_auth.EparaDVR import EparaDVR


class EparaDVRTest(unittest.TestCase):
    def test_one(self):
        data = {'header': {
            'www_authenticate': '"Digest qop=""auth"", stale=false, algorithm=MD5, realm=""EPARA16D3"", nonce=""1458108515"""'}}
        metadata = EparaDVR().process(data, Metadata())

        self.assertEqual(metadata.device.manufacturer, 'EverFocus')
        self.assertEqual(metadata.device.product, 'EPARA16D3')
        self.assertEqual(metadata.device.type, 'DVR')


if __name__ == '__main__':
    unittest.main()