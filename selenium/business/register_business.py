#coding=utf-8
from handle.register_handle import RegisterHandle

class RegisterBusiness(object):
    def __init__(self, driver):
        self.handle = RegisterHandle(driver)

    def register(self, email, name, password, code):
        self.handle.send_user_email(email)

        if self.handle.get_error_text('email_error') == 'email error':
            print('detect email error')
            return True

        self.handle.send_user_name(name)
        self.handle.send_user_password(password)
        self.handle.send_captcha_code(code)

    