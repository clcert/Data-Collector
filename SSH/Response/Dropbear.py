from SSH.SshProcess import SshProcess
import Data.Metadata


class Dropbear(SshProcess):
    """
    https://matt.ucc.asn.au/dropbear/dropbear.html
    """

    protocol = "SSH"
    subprotocol = "Banner"

    search = "dropbear"

    def process(self, data, metadata):
        """
        :type metadata: Metadata.Metadata
        :type data: dict
        """
        if SshProcess.get_response(data).lower().find(self.search) != -1:
            metadata.service.product = "Dropbear"
        return metadata
