import re

from ssh.ssh_process import SSHProcess


class OpenSSH(SSHProcess):

    re_expr = re.compile("^ssh-\d\.\d-openssh_(?P<version>[\d\.p]+)", re.IGNORECASE)

    def process(self, data, metadata):
        banner = data.get('banner')

        if banner:
            match_obj = self.re_expr.search(banner)

            if match_obj:
                metadata.service.product = 'OpenSSH'
                metadata.service.version = match_obj.group('version')

        return metadata
