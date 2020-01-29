# Embedded file name: ServerInfo.py


class Info:

    def __init__(self, get):
        self.get = get

    def get_info(self):
        if self.get.lower() == 'uid':
            return '0x00000000'
        if self.get.lower() == 'heap':
            return '0x8000-0x1000000'
        if self.get.lower() == 'name':
            return 'scriptslock'
        if self.get.lower() == 'about':
            return 'linux version'
        if self.get.lower() == 'ver':
            return '1.0'
        if self.get.lower() == 'date':
            return '07-09-2014'