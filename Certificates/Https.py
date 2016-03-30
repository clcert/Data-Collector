import textwrap
import time
from subprocess import check_output, CalledProcessError

from OpenSSL.crypto import load_certificate, FILETYPE_PEM
from dateutil import parser


class Https(object):
    def __init__(self, data, date):
        super(Https, self).__init__()
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
    def load_pem_cert(certificate):
        return load_certificate(FILETYPE_PEM, certificate)

    @staticmethod
    def delete_old_values(certificate):
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
