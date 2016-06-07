import re


class ZmapLog(object):
    log_regex = '(?P<minutes>\d+):(?P<seconds>\d+).*send:\s(?P<send>\d+).*\((?P<send_avg>[\d\.]+\s\w{2}\/\w).*\).*' \
                'recv:\s(?P<recv>\d+)[^\(]*\((?P<recv_avg>\d+\s\w{1,2}\/\w)[^\)]*\).*hits:\s(?P<hits>[\d\.]+)\%'
    regex = re.compile(log_regex)

    def __init__(self):
        self.time = 0
        self.send = 0
        self.recv = 0
        self.hits = 0

    def process_log(self, input):
        for line in input:
            match_obj = self.regex.search(line)
            if match_obj:
                self.time = (int(match_obj.group('minutes')) * 60) + int(match_obj.group('seconds'))
                self.send = int(match_obj.group('send'))
                self.recv = int(match_obj.group('recv'))
                self.hits = float(match_obj.group('hits'))

    def to_dict(self):
        return dict((k, v) for k, v in self.__dict__.iteritems() if v)
