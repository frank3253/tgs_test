from time import sleep
from selenium.webdriver.common.by import By
from .base import Base


# 登录后的首页面
class HomePage(Base):
    url = '/'

    # 定位器
    # 01客服电话
    servicetel_loc = (By.XPATH, "html/body/div[1]/div[1]/div/ul[1]/li[1]")
    # 02新手必读
    newrequired_loc = (By.XPATH, "html/body/div[1]/div[1]/div/ul[2]/li[4]/a")
    # 03邀请好友
    invite_loc = (By.XPATH, "html/body/div[1]/div[1]/div/ul[2]/li[6]/a")
    # 04发起合买
    startbuy_loc = (By.XPATH, "html/body/div[1]/div[1]/div/ul[2]/li[8]/a")
    # 05了解淘股神
    img1_loc = (By.XPATH, ".//*[@id='main-out']/div[1]/div[1]/a[1]/img")
    # 06挑战股神
    img2_loc = (By.XPATH, ".//*[@id='main-out']/div[1]/div[1]/a[2]/img")
    # 07发起合买
    img3_loc = (By.XPATH, ".//*[@id='main-out']/div[1]/div[1]/a[3]/img")
    # 08立即交易
    img4_loc = (By.XPATH, ".//*[@id='main-out']/div[1]/div[1]/a[4]/img")
    # 09合买列表(复数)
    hmlist_locs = (By.XPATH, "//div[@class='root-indexlist']/div[@class='root-hmlist']")
    # 其中一条合买项目数据校验
    projectname_loc = (By.XPATH, ".//*[@id='main']/div[1]/div[2]/div[3]/ul/li[1]/h4/a")  # 10项目名
    projectrealname_loc = (By.XPATH, ".//*[@id='main']/div[1]/div[2]/div[3]/div/a[2]/p")  # 11股神名
    projectmode_loc = (By.XPATH, ".//*[@id='main']/div[1]/div[2]/div[3]/ul/li[1]/span[2]")  # 12项目模式
    projecttype_loc = (By.XPATH, ".//*[@id='main']/div[1]/div[2]/div[3]/ul/li[1]/span[1]")  # 13项目类型
    projectlead_loc = (By.XPATH, ".//*[@id='main']/div[1]/div[2]/div[3]/ul/li[2]/p[1]")  # 14领投
    projectquantity_loc = (By.XPATH, ".//*[@id='main']/div[1]/div[2]/div[3]/ul/li[2]/p[2]")  # 15投资笔数
    projectcommisson_loc = (By.XPATH, ".//*[@id='main']/div[1]/div[2]/div[3]/ul/li[4]/p[2]")  # 16佣金比例
    projectclosure_loc = (By.XPATH, ".//*[@id='main']/div[1]/div[2]/div[3]/ul/li[3]/p[2]/span")  # 17退出周期
    projectprofit_loc = (By.XPATH, ".//*[@id='main']/div[1]/div[2]/div[3]/ul/li[5]/p[2]")  # 18总收益率
    projectamount_loc = (By.XPATH,"//*[@id='main']/div[1]/div[2]/div[3]/ul/li[1]/p") #22 项目总额=申请中的金额+市值
    # 19股神观点数量
    godview_locs = (By.XPATH, "//div[@class='gs-view']/div[@class='view-item']")
    # 20帮助中心
    helpercenter_locs = (By.CLASS_NAME, 'help-item')
    # 21媒体报道
    media_locs = (By.CLASS_NAME,'media-item')

    # 把每一个元素封装成一个方法
    def home01_servicetel(self):
        tel = self.find_element(*self.servicetel_loc).text
        return tel

    def home02_newrequired(self):
        self.find_element(*self.newrequired_loc).click()
        sleep(3)
        return self.driver.current_url

    def home03_invite(self):
        self.find_element(*self.invite_loc).click( )
        sleep(3)
        return self.driver.current_url

    def home04_startbuy(self):
        self.find_element(*self.startbuy_loc).click( )
        sleep(3)
        return self.driver.current_url

    def home05_img1(self):
        self.find_element(*self.img1_loc).click( )
        sleep(3)
        return self.driver.current_url

    def home06_img2(self):
        self.find_element(*self.img2_loc).click( )
        sleep(3)
        return self.driver.current_url

    def home07_img3(self):
        self.find_element(*self.img3_loc).click( )
        sleep(3)
        return self.driver.current_url

    def home08_img4(self):
        self.find_element(*self.img4_loc).click( )
        sleep(3)
        return self.driver.current_url

    def home09_hmlist(self):
        hmlist = self.find_elements(*self.hmlist_locs)
        # 返回list的长度
        return len(hmlist)

    def home10_projectname(self):
        element = self.find_element(*self.projectname_loc)
        trade_id = element.get_attribute("href").split("/")[-1]
        projectname = element.text
        return projectname, trade_id

    def home11_projectnickname(self):
        projectnickname = self.find_element(*self.projectrealname_loc).text
        return projectnickname

    def home12_projectmode(self):
        projectmode = self.find_element(*self.projectmode_loc).text
        return projectmode

    def home13_projecttype(self):
        projecttype = self.find_element(*self.projecttype_loc).text
        return projecttype

    def honme14_projectlead(self):
        projectlead = self.find_element(*self.projectlead_loc).text
        return projectlead

    def home15_projectquantity(self):
        projectlead = self.find_element(*self.projectquantity_loc).text
        return projectlead

    def home16_projectcommisson(self):
        projectcommisson = self.find_element(*self.projectcommisson_loc).text
        return projectcommisson

    def home17_projectclosure(self):
        projectclosure = self.find_element(*self.projectclosure_loc).text
        return projectclosure

    def home18_projectprofit(self):
        projectprofit = self.find_element(*self.projectprofit_loc).text
        return projectprofit

    def home19_godview(self):
        godview = self.find_elements(*self.godview_locs)
        return len(godview)

    def home20_helpercenter(self):
        helpercenter = self.find_elements(*self.helpercenter_locs)
        return helpercenter

    def home21_media(self):
        media = self.find_elements(*self.media_locs)
        return  len(media)

    def home22_projectamount(self):
        projectamount = self.find_element(*self.projectamount_loc).text
        return projectamount
