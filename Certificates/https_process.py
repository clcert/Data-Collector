import textwrap
import time
from subprocess import check_output, CalledProcessError

from OpenSSL.crypto import load_certificate, FILETYPE_PEM
from dateutil import parser


class HTTPSProcess(object):
    def __init__(self, data, date):
        self.data = data
        self.timestamp = str(int(time.mktime(date.timetuple())))

    def process(self):
        self.__extract_cert_information()
        self.__verify_certificate()

        return self.data

    def __extract_cert_information(self):
        if 'chain' not in self.data:
            return

        chain = self.data['chain']

        for cert in chain:
            self.__delete_old_values(cert)

            begin, cert_body, end = cert['pem_cert'].split('\n')
            certificate = self.load_pem_cert(begin + '\n' + textwrap.fill(cert_body, 64) + '\n' + end + '\n')

            cert['subject'] = self.__certificate_entity_data(certificate.get_subject())
            cert['issuer'] = self.__certificate_entity_data(certificate.get_issuer())

            cert['not_before'] = parser.parse(certificate.get_notBefore()).strftime("%Y-%m-%d %H:%M:%S")
            cert['not_after'] = parser.parse(certificate.get_notAfter()).strftime("%Y-%m-%d %H:%M:%S")
            cert['key_bits'] = certificate.get_pubkey().bits()
            try:
                cert['signature_algorithm'] = certificate.get_signature_algorithm()
            except ValueError:
                cert['signature_algorithm'] = None

    def __verify_certificate(self):
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
                    out = check_output(('openssl verify -attime ' + self.timestamp + ' -CApath /etc/ssl/certs cert.crt').split())
                else:
                    out = check_output(('openssl verify -attime ' + self.timestamp + ' -CApath /etc/ssl/certs -untrusted chain.crt cert.crt').split())

            except CalledProcessError as e:
                out = e.output

            if self.certificate_expired(out):
                self.data['validate'], self.data['reason'] = False, 'Certificate expired'
            elif self.self_signed(out):
                self.data['validate'], self.data['reason'] = False, 'Self signed'
            elif self.certificate_not_valid_yet(out):
                self.data['validate'], self.data['reason'] = False, 'Not yet valid'
            elif self.certificate_valid_ok(out):
                self.data['validate'] = True
            else:
                self.data['validate'], self.data['reason'] = False, 'Other error'

    @staticmethod
    def __certificate_entity_data(certificate):
        entity = dict()

        entity['raw_information'] = certificate.get_components()
        entity['country_name'] = certificate.countryName
        entity['province_name'] = certificate.stateOrProvinceName
        entity['locality_name'] = certificate.localityName
        entity['organization_name'] = certificate.organizationName
        entity['organization_unit_name'] = certificate.organizationalUnitName
        entity['common_name'] = certificate.commonName
        entity['email_address'] = certificate.emailAddress

        return entity

    @staticmethod
    def load_pem_cert(certificate):
        return load_certificate(FILETYPE_PEM, certificate)

    @staticmethod
    def __delete_old_values(certificate):
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

    @staticmethod
    def certificate_not_valid_yet(output):
        return 'certificate is not yet valid' in output

    @staticmethod
    def certificate_valid_ok(output):
        return 'cert.crt: OK' in output
