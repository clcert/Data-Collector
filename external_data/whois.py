import ipwhois
from ipwhois import IPWhois
from netaddr import IPNetwork
from external_data.IPRipe import get_chilean_ip


def search(networks, ip):
    for network in networks:
        if ip in network:
            return True
    return False


def whois(ip):
    try:
        obj = IPWhois(ip)
        response = obj.lookup()
    except ipwhois.exceptions.WhoisLookupError:
        return None

    return response






