import argparse
import json

from ExternalData.ReverseDNS import reverse_dns
from Whois import whois


def argument_parser():
    parser = argparse.ArgumentParser(description='Recollect IP data')
    parser.add_argument('-i', '--input', help='Input file name', required=True)
    parser.add_argument('-o', '--output', help='Output file name', required=True)
    parser.add_argument('--whois', help='Set whois ip response', required=False)
    parser.add_argument('--reverse_dns', help='Set the machine name', required=False)
    return parser.parse_args()

if __name__ == '__main__':
    args = argument_parser()
    input = open(args.input, 'r')
    output = open(args.output, 'w')

    for line in input:
        json_line = json.loads(line)
        ip = json_line['ip']

        if args.whois:
            json_line['whois'] = whois(ip)
        if args.reverse_dns:
            json_line['dns_reverse'] = reverse_dns(ip)

        output.write(json.dumps(json_line)+'\n')


