class CertificateNormalizer(object):

    def __init__(self, data):
        self.data = data

    def normalize(self):
        self.__rename_fields()
        self.__create_chain()
        self.__remove_old_fields()

        return self.data

    def __remove_old_fields(self):
        self.data.pop('validation', None)
        self.data.pop('certificateAuthority', None)
        self.data.pop('signatureAlgorithm', None)
        self.data.pop('expiredTime', None)
        self.data.pop('organizationName', None)
        self.data.pop('organizationURL', None)
        self.data.pop('keyBits', None)
        self.data.pop('PemCert', None)
        self.data.pop('chainAuthority', None)

    def __rename_fields(self):

        if 'tlsProtocol' in self.data:
            self.data['tls_protocol'] = self.data['tlsProtocol']
            self.data.pop('tlsProtocol', None)

        if 'cipherSuite' in self.data:
            self.data['cipher_suite'] = self.data['cipherSuite']
            self.data.pop('cipherSuite', None)

        if 'ciphersSuites' in self.data:
            self.data['test_cipher_suites'] = self.data['ciphersSuites']
            self.data.pop('ciphersSuites', None)

        if 'tlsProtocol' in self.data:
            self.data['tls_protocol'] = self.data['tlsProtocol']
            self.data.pop('tlsProtocol', None)

        if 'tlsProtocol' in self.data:
            self.data['tls_protocol'] = self.data['tlsProtocol']
            self.data.pop('tlsProtocol', None)

        if 'protocols' in self.data:
            self.data['supported_protocols'] = self.data['protocols']
            self.data.pop('protocols', None)

        if 'heartbleedData' in self.data:
            self.data['heartbleed_data'] = self.data['heartbleedData']
            self.data.pop('heartbleedData', None)

        if 'beastCipher' in self.data:
            self.data['beast_cipher'] = self.data['beastCipher']
            self.data.pop('beastCipher', None)

    def __create_chain(self):
        cert = self.format_pem_cert(self.data.get('PemCert'))
        chain = self.__get_chain_pem_cert()

        if cert is not None:
            chain.insert(0, cert)
            new_chain = list()

            for elem in chain:
                new_cert = {'pem_cert': elem}
                new_chain.append(new_cert)

            self.data['chain'] = new_chain

    def __get_chain_pem_cert(self):
        chain = self.data.get('chainAuthority')
        pem_chain = list()

        if chain is not None:
            for elem in chain:
                pem = elem.get('PemCert')
                if pem is not None:
                    pem_chain.append(self.format_pem_cert(pem))

        return pem_chain

    @staticmethod
    def format_pem_cert(cert):
        if cert is not None:
            split_cert = cert.split('\n')
            begin = split_cert[0]
            body = ''.join(split_cert[1:-1])
            end = split_cert[-1]

            return begin + '\n' + body + '\n' + end

        return None
