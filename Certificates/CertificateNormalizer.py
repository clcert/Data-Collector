class CertificateNormalizer(object):

    def __init__(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def normalize(self):
        self.__create_chain()
        self.__remove_old_fields()

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
