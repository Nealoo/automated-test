#coding=utf-8
import sys
import os
sys.path.append( os.path.abspath('./') )
from business.register_business import RegisterBusiness
from selenium import webdriver

class FirstCase(object):
    def __init__(self):

        driver = webdriver.Chrome()
        driver.get('http://www.5itest.cn/register')
        self.business = RegisterBusiness(driver)

    def test_register_email_error(self):
        found_email_error = self.business.register('33','name','123123','captcha')

        if found_email_error:
            print('found email error')
    
    def test_register_name_error(self):
        found_name_error = self.business.register('33','name','123123','captcha')

        if found_name_error:
            print('found email error')

def main():
    first = FirstCase()
