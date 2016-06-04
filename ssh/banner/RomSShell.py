import re

from ssh.ssh_process import SSHProcess


class RomSShell(SSHProcess):
    """
    https://www.allegrosoft.com/embedded-ssh-client-server-ae
    """

    re_expr = re.compile('ssh-\d\.\d-romsshell_(?P<version>[\d\.]+)', re.IGNORECASE)

    def process(self, data, metadata):
        banner = data.get('banner')

        if banner:
            match_obj = self.re_expr.search(banner)

            if match_obj:
                metadata.service.product = "RomSShell"
                metadata.service.manufacturer = "Allegro"
                metadata.service.version = match_obj.group('version')

        return metadata
