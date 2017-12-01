from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from .base import Base

class Logon_page(Base):
    url = '/'
    login_success_user_loc = (By.XPATH, 'html/body/div[1]/div[1]/div/ul[2]/li[2]/a')

    def login_success_user(self):
        return self.find_element(*self.login_success_user_loc).text