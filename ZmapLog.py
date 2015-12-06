import re


class ZmapLog(object):
    log_regex = '(?P<time>\d+:\d+).*send:\s(?P<send>\d+).*\((?P<send_avg>[\d\.]+\s\w{2}\/\w).*\).*recv:\s(?P<recv>\d+)[^\(]*\((?P<recv_avg>\d+\s\w{1,2}\/\w)[^\)]*\).*hits:\s(?P<hits>[\d\.\%]+)'
    regex = re.compile(log_regex)

    def __init__(self):
        self.time = None
        self.send = 0
        self.send_avg = 0
        self.recv = 0
        self.recv_avg = 0
        self.hits = 0

    def process_log(self, input):
        for line in input:
            match_obj = self.regex.search(line)
            if match_obj:
                self.time = match_obj.group('time')
                self.send = match_obj.group('send')
                self.send_avg = match_obj.group('send_avg')
                self.recv = match_obj.group('recv')
                self.recv_avg = match_obj.group('recv_avg')
                self.hits = match_obj.group('hits')

    def to_dict(self):
        return dict((k, v) for k, v in self.__dict__.iteritems() if v)
