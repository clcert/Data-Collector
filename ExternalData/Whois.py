import ipwhois
from ipwhois import IPWhois
from netaddr import IPNetwork
from ExternalData.IPRipe import get_chilean_ip

__author__ = 'eduardo'

pool_size = 10


def search(networks, ip):
    for network in networks:
        if ip in network:
            return True
    return False


def whois(ip):
    """
    return the whois of ip
    :param ip: str
    :return:
    """
    try:
        obj = IPWhois(ip)
        response = obj.lookup()
    except ipwhois.exceptions.WhoisLookupError:
        return None
    return response


if __name__ == '__main__':
    check_sub_network = list()

    for sub_network in get_chilean_ip():
        ip_network = IPNetwork(sub_network)
        for ip in ip_network:
            if not search(check_sub_network, ip):
                response = whois(ip)
                print response
                if response['nets'][0]['cidr'] is not None:
                    check_sub_network.append(IPNetwork(response['nets'][0]['cidr']))






