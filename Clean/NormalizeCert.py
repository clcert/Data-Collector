import json

from OpenSSL.crypto import load_certificate, FILETYPE_PEM


def load_pem_cert(certificate):
    """
    :param certificate: str
    :return: OpenSSL.crypto.X509
    """
    return load_certificate(FILETYPE_PEM, certificate)


def get_cert_info(data):
    """
    :param data: dict
    :return: dict
    """
    #TODO expose more info
    cert = dict()

    if 'signatureAlgorithm' in data:
        cert['signatureAlgorithm'] = data['signatureAlgorithm']
        data.pop('signatureAlgorithm', None)

    if 'expiredTime' in data:
        cert['expiredTime'] = data['expiredTime']
        data.pop('expiredTime', None)

    if 'organizationName' in data:
        cert['organizationName'] = data['organizationName']
        data.pop('organizationName', None)

    if 'organizationURL' in data:
        cert['organizationURL'] = data['organizationURL']
        data.pop('organizationURL', None)

    if 'keyBits' in data:
        cert['keyBits'] = data['keyBits']
        data.pop('keyBits', None)

    if 'PemCert' in data:
        cert['PemCert'] = data['PemCert']
        data.pop('PemCert', None)

    if len(cert) == 0:
        return None
    return cert


def normalize_cert(data):
    """
    :param data: dict
    :return: dict
    """
    if 'validation' in data:
        data.pop('validation', None)

    if 'certificateAuthority' in data:
        data.pop('certificateAuthority', None)

    cert = get_cert_info(data)

    if cert is not None and 'chainAuthority' in data:
        chain = data['chainAuthority']
        data.pop('chainAuthority', None)
        chain.insert(0, cert)
        data['chain'] = chain

        for certificate in chain:
            pem_cert = load_pem_cert(certificate['PemCert'])
            certificate['certificateAuthority'] = pem_cert.get_issuer().organizationName

    return data
