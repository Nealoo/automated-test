#coding=utf-8
from page.register_page import RegisterPage

class RegisterHandle(object):
    def __init__(self, drive):
        self.page = RegisterPage(drive)

    def send_user_email(self, email):
        self.page.get_email_element().send_keys(email)

    def send_user_name(self, name):
        self.page.get_name_element().send_keys(name)

    def send_user_password(self, password):
        self.page.get_password_element().send_keys(password)

    def send_captcha_code(self, code):
        self.page.get_code_element().send_keys(code)
    
    def get_error_text(self, error_type):
        if error_type == 'email_error':
            return self.page.get_name_error_element().get_attribute('value')
        elif error_type == 'name_error':
            return self.page.get_name_error_element().get_attribute('value')
        elif error_type == 'password_error':
            return self.page.get_password_error_element().get_attribute('value')
        elif error_type == 'captcha_error':
            return self.page.get_code_error_element().get_attribute('value')

    def click_register_button(self):
        self.page.get_register_button().click