import textwrap
from subprocess import check_output, CalledProcessError


def verify_cert(data):

    if 'chain' in data:
        cert = data['chain'][0]['PemCert'].encode('ascii', 'ignore')
        chain = [i['PemCert'] for i in data['chain'][1:]]

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
                out = check_output(['openssl', 'verify', '-CApath', '/etc/ssl/certs', '-untrusted', 'chain.crt', 'cert.crt'])

        except CalledProcessError:
            return False
        if certificate_expired(out) or self_signed(out):
            return False
        return True


def certificate_expired(output):
    return 'certificate has expired' in output


def self_signed(output):
    return 'self signed certificate' in output
