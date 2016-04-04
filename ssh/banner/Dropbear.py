from ssh.ssh_process import SSHProcess


class Dropbear(SSHProcess):
    """
    https://matt.ucc.asn.au/dropbear/dropbear.html
    """

    search = "dropbear"

    def process(self, data, metadata):
        banner = data.get('banner')

        if banner:
            if banner.lower().find(self.search) != -1:
                metadata.service.product = "Dropbear"

        return metadata
