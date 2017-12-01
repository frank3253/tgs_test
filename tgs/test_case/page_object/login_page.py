from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from .base import Base

#页面对象（PO）登录页面
class LoginPage(Base):
    url = '/login/login'

    #定位器
    username_loc = (By.NAME, 'username')
    password_loc = (By.NAME, 'password')
    assertID_loc = (By.NAME, 'captcha')
    button_loc = (By.ID, 'confirm')
    error_loc = (By.CLASS_NAME, 'layui-layer-content')

    #把每一个元素封装成一个方法
    def login_username(self, text):
        self.find_element(*self.username_loc).send_keys(text)

    def login_password(self, text):
        self.find_element(*self.password_loc).send_keys(text)

    def login_assertID(self):
        self.find_element(*self.assertID_loc).send_keys("8888")

    def login_button(self):
        self.find_element(*self.button_loc).click()

    def login_error_hint(self):
        return self.find_element(*self.error_loc).text

    #登录方法
    def login_action(self, username, password):
        self.login_username(username)
        self.login_password(password)
        self.login_assertID()
        self.login_button()
