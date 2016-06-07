import argparse
import json
import sys

import datetime

import certificates
import http
import ssh
from clean.clean_errors import clean_json
from data.metadata import Metadata
from external_data.reverse_dns import reverse_dns
from external_data.whois import whois
from http.http_preprocessor import HTTPPreprocessor
from http.http_process import HTTPProcess
from http.normalizer import Normalizer
from logs.zmap_log import ZmapLog
from progressBar import ProgressBar
from ssh.ssh_process import SSHProcess
from ssh.Juniper import Juniper
from http.header import *
from ssh.banner import *


def argument_parser():
    parser = argparse.ArgumentParser(description='Recollect IP data')
    parser.add_argument('-i', '--input', help='Input file name', required=True)
    parser.add_argument('-o', '--output', help='Output file name', required=True)
    parser.add_argument('--port', help='Set the scanned port', required=True)
    parser.add_argument('--date', help='Add the date of scan (input format dd/mm/yyyy)', required=True)
    parser.add_argument('--whois', help='Set whois ip response', action='store_true', required=False)
    parser.add_argument('--dns_reverse', help='Set the machine name', action='store_true', required=False)
    parser.add_argument('--old_data', help='Parse old data', action='store_true', required=False)
    parser.add_argument('--http', help='Parse http info', action='store_true', required=False)
    parser.add_argument('--https', help='Parse https certificate info and validate this', action='store_true',
                        required=False)
    parser.add_argument('--ssh', help='Parse ssh info', action='store_true', required=False)
    parser.add_argument('--normalize_cert', help='Normalize old certificate scans fields', action='store_true',
                        required=False)
    parser.add_argument('--clean_errors', help='Clean the lines with only error an ip fields', action='store_true',
                        required=False)
    parser.add_argument('--zmap_log', help='Parse Zmap log', action='store_true', required=False)

    return parser.parse_args()


def parse_date(date_string):
    if date_string.count('/') == 2:
        day, month, year = date_string.split('/')
        return datetime.date(int(year), int(month), int(day))

    print "Error: Wrong date format"
    sys.exit(1)


def http_protocol(data, old_data):
    if old_data:
        data = http.normalizer.Normalizer(data).normalize()

    parsed_data = HTTPPreprocessor.preprocess(data)
    subclasses = HTTPProcess.all_subclasses()
    meta = Metadata()

    for sub in subclasses:
        meta.merge(sub().process(parsed_data, Metadata()))

    if not meta.is_empty():
        parsed_data['metadata'] = meta.to_dict()

    return parsed_data


def https_protocol(data, date):
    normalized_data = certificates.normalizer.Normalizer(data).normalize()
    return HTTPProcess(normalized_data, date).process()


def ssh_protocol(data):
    normalized_data = ssh.normalizer.Normalizer(data).normalize()
    subclasses = SSHProcess.all_subclasses()
    meta = Metadata()

    for sub in subclasses:
        meta = sub().process(normalized_data, meta)

    if not meta.is_empty():
        normalized_data['metadata'] = normalized_data.to_dict()

    normalized_data = Juniper.has_backdoor(normalized_data)

    return normalized_data


def zmap_log(port, date, input):
    log = ZmapLog()

    log.process_log(input)
    log_dict = log.to_dict()
    log_dict['port'] = int(port)
    log_dict['date'] = str(date)

    return log_dict


def dns_reverse(data):
    reverse = reverse_dns(data['ip'])

    if reverse != 'None':
        data['dns-reverse'] = reverse

    return data


def ip_whois(data):
    whois_response = whois(data['ip'])

    if whois_response is not None:
        data['whois'] = whois_response

    return data


def main():
    args = argument_parser()
    progress_bar = ProgressBar(args.input)
    date = parse_date(args.date)

    input = open(args.input, 'r')
    output = open(args.output, 'w')

    if args.zmap_log:
        log_dict = zmap_log(args.port, date, input)

        output.write(json.dumps(log_dict))
        sys.exit(0)

    progress_bar.start()

    for line in input:
        progress_bar.update(1)
        data = json.loads(line)

        if args.clean_errors and clean_json(data):
            continue

        if args.dns_reverse:
            data = dns_reverse(data)

        if args.whois:
            data = ip_whois(data)

        if args.http:
            data = http_protocol(data, args.old_data)

        if args.https:
            data = https_protocol(data, date)

        if args.ssh:
            data = ssh_protocol()

        data['date'] = date.strftime("%Y-%m-%d")
        data['schema_version'] = '1.0'

        output.write(json.dumps(data) + '\n')

    progress_bar.finish()

if __name__ == '__main__':
    main()
