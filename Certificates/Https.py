

def normalize_name(data):
    chain = data['chain']

    for cert in chain:
        if 'organizationName' in cert:
            cert['organization_name'] = cert['organizationName']

        if 'organizationURL' in cert:
            cert['organization_url'] = cert['organizationURL']

        if 'certificateAuthority' in cert:
            cert['certificate_authority'] = cert['certificateAuthority']

        if 'PemCert' in cert:
            cert['pem_cert'] = cert['PemCert']

        if 'expiredTime' in cert:
            cert['expired_time'] = cert['expiredTime']

        if 'keyBits' in cert:
            cert['key_bits'] = cert['keyBits']

        if 'signatureAlgorithm' in cert:
            cert['signature_algorithm'] = cert['signatureAlgorithm']


def expose_self_cert_info(data):
    if 'chain' in data:
        self_cert = data['chain'][0]

        if 'certificateAuthority' in self_cert:
            data['certificate_authority'] = self_cert['certificateAuthority']

        if 'signatureAlgorithm' in self_cert:
            data['signature_algorithm'] = self_cert['signatureAlgorithm']

        if 'keyBits' in self_cert:
            data['key_bits'] = self_cert['keyBits']

    return data


a = dict()
a1 = dict()
b = dict()
b1 = dict()


a1['hola'] = 12
b1['hola'] = 13

#a['elem'] = a1
#b['elem'] = b1

lista =  list()
lista.append(a1)
lista.append(b1)

final = dict()
final['lista'] = lista

print final

otra_lista = final['lista']
for l in otra_lista:
    l['chao'] = 15

print final



