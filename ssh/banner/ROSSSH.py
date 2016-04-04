from ssh.ssh_process import SSHProcess


class ROSSSH(SSHProcess):
    """
    http://www.mikrotik.com/software
    """

    search = "rosssh"

    def process(self, data, metadata):
        banner = data.get('banner')

        if banner:
            if banner.lower().find(self.search) != -1:
                metadata.device.manufacturer = "Mikrotik"
                metadata.device.os = "RouterOS"
                metadata.device.type = "Router"

        return metadata
