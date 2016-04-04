from dns import reversename, resolver


def reverse_dns(ip):
    addr = reversename.from_address(ip)

    try:
        dns_name = resolver.query(addr, 'PTR')[0]
    except:
        dns_name = None

    return str(dns_name)