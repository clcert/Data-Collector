import argparse
import json
import sys

from datetime import date

from Certificates.validate import verify_cert
from Clean.CleanErrors import clean_json
from Clean.NormalizeCert import normalize_cert
from Clean.NormalizeHttp import normalize_http
from Logs.ZmapLog import ZmapLog
from ExternalData.ReverseDNS import reverse_dns
from ExternalData.Whois import whois
from HTTP.HttpProcess import HttpProcess
from HTTP.Metadata import Metadata
from HTTP.Header import *


def argument_parser():
    parser = argparse.ArgumentParser(description='Recollect IP data')
    parser.add_argument('-i', '--input', help='Input file name', required=True)
    parser.add_argument('-o', '--output', help='Output file name', required=False)
    parser.add_argument('--port', help='Set the scanned port', required=False)
    parser.add_argument('--date', help='Add the date of scan (input format dd/mm/yyyy)', required=False)
    parser.add_argument('--whois', help='Set whois ip response', action='store_true', required=False)
    parser.add_argument('--dns_reverse', help='Set the machine name', action='store_true', required=False)
    parser.add_argument('--http', help='Parse http info', action='store_true', required=False)
    parser.add_argument('--normalize_http', help='Normalize old http scans fields', action='store_true', required=False)
    parser.add_argument('--normalize_cert', help='Normalize old certificate scans fields', action='store_true', required=False)
    parser.add_argument('--validate_cert', help='Validate server certificate', action='store_true', required=False)
    parser.add_argument('--clean_errors', help='Clean the lines with only error an ip fields', action='store_true', required=False)
    parser.add_argument('--zmap_log', help='Parse Zmap log', action='store_true', required=False)
    return parser.parse_args()


if __name__ == '__main__':
    args = argument_parser()
    input = open(args.input, 'r')
    output = open(args.output, 'w')

    if args.date and args.date.count('/') == 2:
        day, month, year = args.date.split('/')
        date = str(date(int(year), int(month), int(day)))
    elif args.date:
        sys.exit(1)

    if args.zmap_log and args.port and args.date:
        log = ZmapLog()
        log.process_log(input)
        log_dict = log.to_dict()
        log_dict['port'] = args.port
        log_dict['date'] = date

        output.write(json.dumps(log_dict))
        sys.exit(1)

    for line in input:
        data = json.loads(line)

        if args.normalize_http:
            data = normalize_http(data)

        if args.normalize_cert:
            data = normalize_cert(data)

        if args.clean_errors and clean_json(data):
            continue

        if args.date:
            data['date'] = date

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

        if args.validate_cert and 'chain' in data:
            data['valid'] = verify_cert(data)

        output.write(json.dumps(data)+'\n')