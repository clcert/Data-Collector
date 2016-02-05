import json
import textwrap
from pprint import pprint

from dateutil import parser
from OpenSSL.crypto import load_certificate, FILETYPE_PEM
from subprocess import check_output, CalledProcessError


class Https(object):
    def __init__(self, data):
        """
        :param data: dict
        """
        super(Https, self).__init__()
        self.data = data

    def extract_cert_information(self):
        """
        Extract all information in the certificate.
        """
        chain = self.data['chain']

        for cert in chain:
            self.delete_old_values(cert)

            begin, cert_body, end = cert['pem_cert'].split('\n')
            certificate = self.load_pem_cert(begin + '\n' + textwrap.fill(cert_body, 64) + '\n' + end + '\n')

            subject = dict()
            subject['raw_information'] = certificate.get_subject().get_components()
            subject['country_name'] = certificate.get_subject().countryName
            subject['province_name'] = certificate.get_subject().stateOrProvinceName
            subject['locality_name'] = certificate.get_subject().localityName
            subject['organization_name'] = certificate.get_subject().organizationName
            subject['organization_unit_name'] = certificate.get_subject().organizationalUnitName
            subject['common_name'] = certificate.get_subject().commonName
            subject['email_address'] = certificate.get_subject().emailAddress

            issuer = dict()
            issuer['raw_information'] = certificate.get_issuer().get_components()
            issuer['country_name'] = certificate.get_issuer().countryName
            issuer['province_name'] = certificate.get_issuer().stateOrProvinceName
            issuer['locality_name'] = certificate.get_issuer().localityName
            issuer['organization_name'] = certificate.get_issuer().organizationName
            issuer['organization_unit_name'] = certificate.get_issuer().organizationalUnitName
            issuer['common_name'] = certificate.get_issuer().commonName
            issuer['email_address'] = certificate.get_issuer().emailAddress

            cert['subject'] = subject
            cert['issuer'] = issuer

            cert['not_before'] = parser.parse(certificate.get_notBefore()).strftime("%Y-%m-%d %H:%M:%S")
            cert['not_after'] = parser.parse(certificate.get_notAfter()).strftime("%Y-%m-%d %H:%M:%S")
            cert['key_bits'] = certificate.get_pubkey().bits()
            try:
                cert['signature_algorithm'] = certificate.get_signature_algorithm()
            except ValueError:
                cert['signature_algorithm'] = None

    def verify_certificate(self):
        """
        Validate the certificate using openssl-verify and the operative system trust store
        """
        if 'chain' in self.data:
            cert = self.data['chain'][0]['pem_cert'].encode('ascii', 'ignore')
            chain = [i['pem_cert'] for i in self.data['chain'][1:]]

            out_cert = open('cert.crt', 'w')
            begin, cert, end = cert.split('\n')

            out_cert.write(begin + '\n')
            out_cert.write(textwrap.fill(cert, 64))
            out_cert.write('\n' + end)

            out_chain = open('chain.crt', 'w')
            for c in chain:
                begin, cert, end = c.split('\n')
                out_chain.write(begin + '\n')
                out_chain.write(textwrap.fill(cert, 64))
                out_chain.write('\n' + end + '\n')

            out_cert.close()
            out_chain.close()
            try:
                if len(chain) == 0:
                    out = check_output(['openssl', 'verify', '-CApath', '/etc/ssl/certs', 'cert.crt'])
                else:
                    out = check_output(
                        ['openssl', 'verify', '-CApath', '/etc/ssl/certs', '-untrusted', 'chain.crt', 'cert.crt'])

            except CalledProcessError:
                self.data['validate'], self.data['reason'] = False, None
            if self.certificate_expired(out):
                self.data['validate'], self.data['reason'] = False, 'Certificate expired'
            elif self.self_signed(out):
                self.data['validate'], self.data['reason'] = False, 'Self signed'
            self.data['validate'], self.data['reason'] = True, None

    def get_data(self):
        """
        Data getter
        :return: dict
        """
        return self.data

    def print_pretty(self):
        """
        Print in pretty form the data
        """
        pprint(self.data)

    @staticmethod
    def load_pem_cert(certificate):
        """
        Load certificate in PEM format into a python X509 certificate
        :param certificate: str
        :return: OpenSSL.crypto.X509
        """
        return load_certificate(FILETYPE_PEM, certificate)

    @staticmethod
    def delete_old_values(certificate):
        """
        Delete old values in all certificate and rename PemCert key
        :param certificate: dict
        """
        certificate.pop('organizationName', None)
        certificate.pop('organizationURL', None)
        certificate.pop('certificateAuthority', None)
        certificate.pop('expiredTime', None)
        certificate.pop('keyBits', None)
        certificate.pop('signatureAlgorithm', None)

        if 'PemCert' in certificate:
            certificate['pem_cert'] = certificate['PemCert']
            certificate.pop('PemCert', None)

    @staticmethod
    def self_signed(output):
        return 'self signed certificate' in output

    @staticmethod
    def certificate_expired(output):
        return 'certificate has expired' in output


line = r'''{"ip":"200.1.29.48","tlsProtocol":"TLSv1","cipherSuite":"TLS_RSA_WITH_AES_128_CBC_SHA","chain":[{"certificateAuthority":"DigiCert SHA2 Extended Validation Server CA","signatureAlgorithm":"SHA256withRSA","expiredTime":"Jul 31, 2017 9:00:00 AM","organizationName":"Universidad Tecnica Federico Santa Maria","organizationURL":"portalpagos.usm.cl","keyBits":"2048","PemCert":"-----BEGIN CERTIFICATE-----\n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\n-----END CERTIFICATE-----"},{"certificateAuthority":"DigiCert High Assurance EV Root CA","signatureAlgorithm":"SHA256withRSA","expiredTime":"Oct 22, 2028 9:00:00 AM","organizationName":"DigiCert Inc","organizationURL":"DigiCert SHA2 Extended Validation Server CA","keyBits":"2048","PemCert":"-----BEGIN CERTIFICATE-----\nMIIEtjCCA56gAwIBAgIQDHmpRLCMEZUgkmFf4msdgzANBgkqhkiG9w0BAQsFADBsMQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMRkwFwYDVQQLExB3d3cuZGlnaWNlcnQuY29tMSswKQYDVQQDEyJEaWdpQ2VydCBIaWdoIEFzc3VyYW5jZSBFViBSb290IENBMB4XDTEzMTAyMjEyMDAwMFoXDTI4MTAyMjEyMDAwMFowdTELMAkGA1UEBhMCVVMxFTATBgNVBAoTDERpZ2lDZXJ0IEluYzEZMBcGA1UECxMQd3d3LmRpZ2ljZXJ0LmNvbTE0MDIGA1UEAxMrRGlnaUNlcnQgU0hBMiBFeHRlbmRlZCBWYWxpZGF0aW9uIFNlcnZlciBDQTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBANdTpARR+JmmFkhLZyeqk0nQOe0MsLAAh/FnKIaFjI5j2ryxQDji0/XspQUYuD0+xZkXMuwYjPrxDKZkIYXLBxA0sFKIKx9om9KxjxKws9LniB8f7zh3VFNfgHk/LhqqqB5LKw2rt2O5Nbd9FLxZS99RStKh4gzikIKHaq7q12TWmFXo/a8aUGxUvBHy/Urynbt/DvTVvo4WiRJV2MBxNO723C3sxIclho3YIeSwTQyJ3DkmF93215SF2AQhcJ1vb/9cuhnhRctWVyh+HA1BV6q3uCe7seT6Ku8hI3UarS2bhjWMnHe1c63YlC3k8wyd7sFOYn4XwHGeLN7x+RAoGTMCAwEAAaOCAUkwggFFMBIGA1UdEwEB/wQIMAYBAf8CAQAwDgYDVR0PAQH/BAQDAgGGMB0GA1UdJQQWMBQGCCsGAQUFBwMBBggrBgEFBQcDAjA0BggrBgEFBQcBAQQoMCYwJAYIKwYBBQUHMAGGGGh0dHA6Ly9vY3NwLmRpZ2ljZXJ0LmNvbTBLBgNVHR8ERDBCMECgPqA8hjpodHRwOi8vY3JsNC5kaWdpY2VydC5jb20vRGlnaUNlcnRIaWdoQXNzdXJhbmNlRVZSb290Q0EuY3JsMD0GA1UdIAQ2MDQwMgYEVR0gADAqMCgGCCsGAQUFBwIBFhxodHRwczovL3d3dy5kaWdpY2VydC5jb20vQ1BTMB0GA1UdDgQWBBQ901Cl1qCt7vNKYApl0yHU+PjWDzAfBgNVHSMEGDAWgBSxPsNpA/i/RwHUmCYaCALvY2QrwzANBgkqhkiG9w0BAQsFAAOCAQEAnbbQkIbhhgLtxaDwNBx0wY12zIYKqPBKikLWP8ipTa18CK3mtlC4ohpNiAexKSHc59rGPCHg4xFJcKx6HQGkyhE6V6t9VypAdP3THYUYUN9XR3WhfVUgLkc3UHKMf4Ib0mKPLQNa2sPIoc4sUqIAY+tzunHISScjl2SFnjgOrWNoPLpSgVh5oywM395t6zHyuqB8bPEs1OG9d4Q3A84ytciagRpKkk47RpqF/oOi+Z6Mo8wNXrM9zwR4jxQUezKcxwCmXMS1oVWNWlZopCJwqjyBcdmdqEU79OX2olHdx3ti6G8MdOu42vi/hw15UJGQmxg7kVkn8TUoE6smftX3eg==\n-----END CERTIFICATE-----"}],"protocols":{"SSL_30":false,"TLS_10":true,"TLS_11":false,"TLS_12":false},"ciphersSuites":{"low_ciphers":"TLS_DHE_RSA_WITH_DES_CBC_SHA","medium_ciphers":"TLS_DHE_RSA_WITH_SEED_CBC_SHA","des3_ciphers":"TLS_DHE_RSA_WITH_3DES_EDE_CBC_SHA","high_ciphers":"TLS_DHE_RSA_WITH_AES_256_CBC_SHA"}}'''

https = Https(json.loads(line))
https.extract_cert_information()
https.verify_certificate()
https.print_pretty()
