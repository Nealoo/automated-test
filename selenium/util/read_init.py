import configparser
import os.path

class ReadIni(object):

    def __init__(self, 
    file_name = os.path.abspath('../config/LocalElement.ini'), 
    node='RegisterElement'):
        self.cp = self.load_int(file_name)
        self.node = node

    def load_int(self, file_name):
        cp = configparser.ConfigParser()
        cp.read(file_name)
        return cp

    def get_value(self, key='user_email'):
        config = self.cp.get(self.node, key)
        return config