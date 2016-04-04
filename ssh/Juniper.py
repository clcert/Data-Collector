class Juniper(object):
    """
    https://community.rapid7.com/community/infosec/blog/2015/12/20/cve-2015-7755-juniper-screenos-authentication-backdoor
    """

    search = "ssh-2.0-netscreen"

    def has_backdoor(self, data):
        banner = data.get('banner')

        if banner:
            if banner.lower.find(self.search) != -1:
                data['juniper_backdoor'] = True
                return
        data['juniper_backdoor'] = False

