from dns import reversename, resolver

__author__ = 'eduardo'

def reverse_dns(ip):
    """
    get the machine name of ip if exist
    :param ip: str
    :return: str
    """
    addr = reversename.from_address(ip)
    try:
        dns_name = resolver.query(addr, 'PTR')[0]
    except:
        dns_name = None
    # if dns_name:
    #     json_line['dns_reverse'] = str(dns_name)
    return str(dns_name)