"""
Created on 2017-11-14
@author: yanhao
Project:登录页面的测试用例
"""
from time import sleep
import unittest, random, sys
from tgs.test_case.model import myunit, function, config
from tgs.test_case.page_object.login_page import LoginPage
from tgs.test_case.page_object.logon_page import Logon_page

sys.path.append('./model')
sys.path.append('./page_object')


class LoginTest(myunit.MyTest):
    def test01_login_user_pwd_null(self):
        '''用户名、密码为空登录'''
        po = LoginPage(self.driver)
        po.open( )
        po.login_action('', '')
        sleep(1)
        # print(po.login_error_hint())
        self.assertEqual(po.login_error_hint( ), '用户名不能为空')
        function.insert_img(self.driver, 'user_null.jpg')

    def test02_login_pwd_null(self):
        '''密码为空登录'''
        po = LoginPage(self.driver)
        po.open( )
        po.login_action('abc', '')
        sleep(1)
        # print(po.login_error_hint( ))
        self.assertEqual(po.login_error_hint( ), '密码不能为空')
        function.insert_img(self.driver, 'pwd_null.jpg')

    def test03_login_user_error(self):
        '''用户名不存在'''
        po = LoginPage(self.driver)
        po.open( )
        character = random.choice('zyxwvutsrqponmlkjihgfedcba')
        username = "test" + character
        po.login_action(username, "$#%#")
        sleep(1)
        # print(po.login_error_hint())
        self.assertEqual(po.login_error_hint( ), '不存在该用户!')
        function.insert_img(self.driver, "user_error.jpg")

    def test04_login_pwd_error(self):
        '''密码错误'''
        po = LoginPage(self.driver)
        po.open( )
        username = "13296722824"
        po.login_action(username, "$#%#")
        sleep(1)
        # print(po.login_error_hint())
        self.assertIn('密码错误', po.login_error_hint( ))
        function.insert_img(self.driver, "pwd_error.jpg")

    def test05_login_success(self):
        '''用户名、密码正确,登录成功'''
        po = LoginPage(self.driver)
        po.open( )
        name = config.getuser( )[0]
        password = config.getuser()[1]
        po.login_action(name, password)
        sleep(2)
        po2 = Logon_page(self.driver)
        # print(po2.login_success_user())
        self.assertEqual(po2.login_success_user(), "[退出]")
        function.insert_img(self.driver, "success.jpg")
