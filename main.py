import argparse
import json

# from ExternalData.ReverseDNS import reverse_dns
# from Whois import whois
from HTTP.Header import *
from HTTP.HttpProcess import HttpProcess
from HTTP.Metadata import Metadata


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
        data = json.loads(line)
        # ip = json_line['ip']
        #
        # if args.whois:
        # json_line['whois'] = whois(ip)
        # if args.reverse_dns:
        #     json_line['dns_reverse'] = reverse_dns(ip)

        data = HttpProcess.parse_header(data)
        if 'server' in data:
            subclasses = HttpProcess.all_subclasses()
            meta = Metadata()

            for sub in subclasses:
                    meta = sub().process(data, meta)

            if meta.is_empty() and 'header' in data and 'Server' in data['header']:
                print data['header']['Server']

        # output.write(json.dumps(json_line)+'\n')


