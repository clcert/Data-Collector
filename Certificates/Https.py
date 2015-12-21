
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
