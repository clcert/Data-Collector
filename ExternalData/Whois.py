from ipwhois import IPWhois

__author__ = 'eduardo'


def whois(ip):
    """
    return the whois of ip
    :param ip: str
    :return:
    """
    obj = IPWhois(ip)
    return obj.lookup()

