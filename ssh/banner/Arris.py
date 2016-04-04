from ssh.ssh_process import SSHProcess


class Arris(SSHProcess):
    """
    http://www.surfboard.com/
    """

    search = "arris"
    
    def process(self, data, metadata):
        banner = data.get('banner')

        if banner:
            if banner.lower().find(self.search) != -1:
                metadata.device.manufacturer = "Arris"
                metadata.device.type = "Cable Modem"

        return metadata

