import urllib
import json

__author__ = 'eduardo'

urlCL = "https://stat.ripe.net/data/country-resource-list/data.json?resource=CL"


def get_chilean_ip():
    """
    Retrieves chilean ip from ripe website
    """

    web = urllib.urlopen(urlCL)
    data = json.load(web)

    ipv4 = data["data"]["resources"]["ipv4"]

    # output = "chilean_ipv4.csv"
    # fo = open(output, 'w')
    ipv4_list = list()

    for ip in ipv4:
        ipv4_list.append(ip)

    return ipv4_list


def save_chilean_ip(output):
    """
    Write into a file all chilean ips
    :param output: str
    """
    fo = open(output, 'w')

    for ip in get_chilean_ip():
        fo.write(ip + "\n")

    fo.close()