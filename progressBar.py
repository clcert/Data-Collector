import progressbar


class ProgressBar(object):
    def __init__(self, filename):
        self.number_lines = sum(1 for line in open(filename))
        self.bar = progressbar.ProgressBar(maxval=self.number_lines,
                                           widgets=['Data Collector:', progressbar.Bar('=', '[', ']'), ' ',
                                                    progressbar.Percentage()])
        self.current_lines = 0

    def start(self):
        self.bar.start()

    def update(self, increment):
        self.current_lines += increment
        self.bar.update(self.current_lines)

    def finish(self):
        self.bar.finish()