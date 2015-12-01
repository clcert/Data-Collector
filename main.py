import argparse
import json

from datetime import date

from ExternalData.ReverseDNS import reverse_dns
from ExternalData.Whois import whois
from HTTP.HttpProcess import HttpProcess
from HTTP.Metadata import Metadata
from HTTP.Header import *


def argument_parser():
    parser = argparse.ArgumentParser(description='Recollect IP data')
    parser.add_argument('-i', '--input', help='Input file name', required=True)
    parser.add_argument('-o', '--output', help='Output file name', required=True)
    parser.add_argument('--date', help='Add the date of scan (input format dd/mm/yyyy)', required=False)
    parser.add_argument('--whois', help='Set whois ip response', action='store_true', required=False)
    parser.add_argument('--dns_reverse', help='Set the machine name', action='store_true', required=False)
    parser.add_argument('--http', help='Parse http info', action='store_true', required=False)
    return parser.parse_args()


if __name__ == '__main__':
    args = argument_parser()
    input = open(args.input, 'r')
    output = open(args.output, 'w')

    for line in input:
        data = json.loads(line)

        if args.date and args.date.count('/') == 2:
            day, month, year = args.date.split('/')
            data['date'] = str(date(int(year), int(month), int(day)))

        if args.dns_reverse:
            reverse = reverse_dns(data['ip'])
            if reverse != 'None':
                data['dns-reverse'] = reverse

        if args.whois:
            whois_response = whois(data['ip'])
            if whois_response is not None:
                data['whois'] = whois_response

        if args.http:
            data = HttpProcess.parse_header(data)
            if 'server' in data:
                subclasses = HttpProcess.all_subclasses()
                meta = Metadata()

                for sub in subclasses:
                    meta = sub().process(data, meta)

                if not meta.is_empty():
                    data['metadata'] = meta.to_dict()

        output.write(json.dumps(data)+'\n')