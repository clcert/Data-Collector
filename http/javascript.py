import re


class Javascript:

    script_regex_1 = '<script\s*src\s*=\s*\"\s*(?P<script>.+?)\s*\"\s*.*?\s*type\s*=\s*\"\s*.*?javascript.*?\s*\"'
    script_regex_2 = '<script\s*type\s*=\s*\"\s*.*?javascript.*?\s*\"\s*.*?\s*src\s*=\s*\"(?P<script>.+?)\s*\"'

    regex_1 = re.compile(script_regex_1, re.IGNORECASE)
    regex_2 = re.compile(script_regex_2, re.IGNORECASE)

    def __init__(self):
        pass

    def parse(self, index):
        match_1 = self.regex_1.findall(index)
        match_2 = self.regex_2.findall(index)

        if match_1 or match_2:
            javascript_list = list()

            javascript_list.extend(match_1)
            javascript_list.extend(match_2)

            return javascript_list

        return None
