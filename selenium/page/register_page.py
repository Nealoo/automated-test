#coding=utf-8

from util.find_element import FindElement

class RegisterPage(object):
    def __init__(self, driver):
        self.search = FindElement(driver)

    def get_email_element(self):
        return self.search.get_element('user_email')

    def get_name_element(self):
        return self.search.get_element('user_name')

    def get_password_element(self):
        return self.search.get_element('password')

    def get_code_element(self):
        return self.search.get_element('captcha_code')

    def get_register_button(self):
        return self.search.get_element('register_btn')

    def get_email_error_element(self):
        return self.search.get_element('user_email_error')

    def get_name_error_element(self):
        return self.search.get_element('user_name_error')

    def get_password_error_element(self):
        return self.search.get_element('password-error')

    def get_code_error_element(self):
        return self.search.get_element('captcha_code-error')
