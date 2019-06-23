#coding=utf-8

from business.register_business import RegisterBusiness

class FirstCase(object):
    def __init__(self):
        self.business = RegisterBusiness()

    def test_register_email_error(self):
        self.business.register('33','name','123123','captcha')
