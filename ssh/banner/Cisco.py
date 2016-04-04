from ssh.ssh_process import SSHProcess


class Cisco(SSHProcess):

    search = "cisco"

    def process(self, data, metadata):
        banner = data.get('banner')

        if banner:
            if banner.lower().find(self.search) != -1:
                metadata.device.manufacturer = "Cisco"

        return metadata
