#coding=utf-8
from util.read_init import ReadIni

class FindElement(object):
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, key):
        read_int = ReadIni()
        value_array = read_int.get_value(key).split('>')
        by = value_array[0]
        name = value_array[1]

        try:
            if by == 'id':
                return self.driver.find_element_by_id(name)
            elif by == 'name':
                return self.driver.find_element_by_name(name)
            elif by == 'className':
                return self.driver.find_element_by_class_name(name)
            elif by == 'xpath':
                return self.driver.find_element_by_xpath(name)
            else:
                return None
        except:
            return None
