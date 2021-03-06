import re

from ssh.ssh_process import SSHProcess


class Dropbear(SSHProcess):
    """
    https://matt.ucc.asn.au/dropbear/dropbear.html
    """

    re_expr = re.compile("^ssh-\d\.\d.dropbear_(?P<version>[\d\.]+)", re.IGNORECASE)

    def process(self, data, metadata):
        banner = data.get('banner')

        if banner:
            match_obj = self.re_expr.search(banner)

            if match_obj:
                metadata.service.product = "Dropbear"
                metadata.service.version = match_obj.group('version')

        return metadata
