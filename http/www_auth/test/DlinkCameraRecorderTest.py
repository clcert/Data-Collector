import unittest
from data.metadata import Metadata
from http.www_auth.DlinkCameraRecorder import DlinkCameraRecorder


class DlinkCameraRecorderTest(unittest.TestCase):
    def test_one(self):
        data = {'header': {
            'www_authenticate': '"Digest realm=""DNR-202L"", qop=""auth"", nonce=""4af6f7c76106e7243b261e73babf6da4"",'
                                ' opaque=""14-373c-132"", algorithm=""MD5"", stale=""FALSE"""'}}
        metadata = DlinkCameraRecorder().process(data, Metadata())

        self.assertEqual(metadata.device.manufacturer, 'DLink')
        self.assertEqual(metadata.device.product, 'DNR-202L')
        self.assertEqual(metadata.device.type, 'DVR')

    def test_two(self):
        data = {'header': {
            'www_authenticate': '"Digest realm=""DNR-312L"", qop=""auth"", nonce=""7daecfa45bb43934fe6a6941a56e8dd5"",'
                                ' opaque=""0-64d-133"", algorithm=""MD5"", stale=""FALSE"""'}}
        metadata = DlinkCameraRecorder().process(data, Metadata())

        self.assertEqual(metadata.device.manufacturer, 'DLink')
        self.assertEqual(metadata.device.product, 'DNR-312L')
        self.assertEqual(metadata.device.type, 'DVR')


if __name__ == '__main__':
    unittest.main()
