# coding = utf-8
"""
Created on 2017-11-20
@author: yanhao
Project:首页的测试用例
"""
from decimal import Decimal
from time import sleep
import unittest, random, sys
from tgs.test_case.model.mdb import getdata, getnum
from tgs.test_case.page_object.login_page import LoginPage
from tgs.test_case.model import myunit, function, config
from tgs.test_case.page_object.home_page import HomePage
from selenium.webdriver.common.by import By
sys.path.append('./model')
sys.path.append('./page_object')


class HomeTest(myunit.MyTest):
    def test01_home_servicetel(self):
        """01客服电话校验"""
        po = HomePage(self.driver)
        po.open( )
        sleep(2)
        tel = po.home01_servicetel( )
        self.assertEqual(tel, "客服热线：4008-579-779|", msg="客服热线错误")

    def test02_home_newrequired(self):
        """02新手必读跳转页面校验"""
        po = HomePage(self.driver)
        po.open( )
        sleep(2)
        newrequired = po.home02_newrequired( )
        self.assertEqual(newrequired, "http://121.41.86.192:7080/help/guide", msg="新手必读地址错误")
        self.assertIsNotNone(po.find_element(By.XPATH, "html/body/div[5]/img"))

    def test03_home_invite(self):
        """03邀请好友按钮校验"""
        po = HomePage(self.driver)
        po.open( )
        sleep(2)
        inviteurl = po.home03_invite( )
        self.assertEqual(inviteurl, "http://121.41.86.192:7080/anon/intro/broker", msg="邀请好友地址错误")
        self.assertIsNotNone(po.find_element(By.XPATH, "html/body/div[4]/img"))

    def test04_home_startbuy(self):
        """ 04点击title发起合买（未登录、已登录）"""
        po = HomePage(self.driver)
        po.open( )
        sleep(2)
        startbyurl = po.home04_startbuy( )
        self.assertIn("http://121.41.86.192:7080/login/login", startbyurl,
                      msg="首页跳转登录地址错误")
        name = config.getuser( )[0]
        password = config.getuser( )[1]
        po2 = LoginPage(self.driver)
        po2.login_action(name, password)
        sleep(2)
        po.find_element(By.XPATH, "//a[@title='成就自我，你就是下一个股神']").click( )
        sleep(2)
        startbyur2 = self.driver.current_url
        self.assertEqual(startbyur2, "http://121.41.86.192:7080/product/create", msg="首页跳转合买地址错误")
        self.assertEqual(po.find_element(By.XPATH, ".//*[@id='form1']/div[1]/h2", ).text, "发布合买")

    def test05_home_img1(self):
        """ 05了解淘股神"""
        po = HomePage(self.driver)
        po.open( )
        sleep(2)
        img1url = po.home05_img1( )
        self.assertIn("help#1", img1url, msg="什么是淘股神地址错误")
        self.assertEqual(po.find_element(By.XPATH, "//div[@class='biaoti1']").text, "什么是淘股神？")

    def test06_home_newrequired(self):
        """ 06挑战股神(测试环境不可测)"""
        # po = HomePage(self.driver)
        # po.open( )
        # sleep(2)
        pass

    def test07_home_img3(self):
        """ 07点击玩转淘股神的发起合买"""
        po = HomePage(self.driver)
        po.open( )
        sleep(2)
        startbyurl = po.home07_img3( )
        self.assertIn("http://121.41.86.192:7080/login/login", startbyurl,
                      msg="首页跳转登录地址错误")
        name = config.getuser( )[0]
        password = config.getuser( )[1]
        po2 = LoginPage(self.driver)
        po2.login_action(name, password)
        sleep(2)
        po.find_element(By.XPATH, "//img[@title='玩转淘股神第3步-发起合买']").click( )
        sleep(2)
        startbyur2 = self.driver.current_url
        self.assertEqual(startbyur2, "http://121.41.86.192:7080/product/create", msg="首页跳转合买地址错误")
        self.assertEqual(po.find_element(By.XPATH, ".//*[@id='form1']/div[1]/h2", ).text, "发布合买")

    def test08_home_newrequired(self):
        """ 08立即交易（测试环境不可测）"""
        # po = HomePage(self.driver)
        # po.open( )
        # sleep(2)
        pass

    def test09_home_hmlist(self):
        """合买列表数量校验"""
        po = HomePage(self.driver)
        po.open( )
        sleep(2)
        hmlist = po.home09_hmlist( )
        self.assertEqual(hmlist, 8, msg="产品列表数据错误")

    def test10_home_projectname(self):
        """ 10项目名"""
        po = HomePage(self.driver)
        po.open( )
        sleep(2)
        projectname = po.home10_projectname( )
        self.assertIsNotNone(projectname)
        print(projectname)

    def test11_home_projectnickname(self):
        """ 11股神名校验"""
        po = HomePage(self.driver)
        po.open( )
        sleep(2)
        projectname = po.home10_projectname( )[0]
        projectnickname = po.home11_projectnickname( )
        sql1 = "select user_name from base_project WHERE trade_name=" + "'" + projectname + "'"
        user_name = getdata(sql1)
        sql2 = "select nick_name from user_base_info WHERE user_name=" + "'" + user_name + "'"
        projectnickname_db = getdata(sql2)
        self.assertEqual(projectnickname, projectnickname_db, msg="股神名与数据库不一致")

    def test12_home_projectmode(self):
        """  12项目模式（开放）"""
        po = HomePage(self.driver)
        po.open( )
        sleep(2)
        trade_id = po.home10_projectname( )[1]  # 获取项目ID
        projectmodehz = po.home12_projectmode( )  # 获取项目模式的中文
        if projectmodehz == "开放":
            projectmode = "open_mode"
            sql = "select project_mode from base_project WHERE trade_id=" + trade_id
            projectmode_db = getdata(sql)
            self.assertEqual(projectmode, projectmode_db, msg="项目模式错误")
        else:
            print("封闭式项目，不适用本条用例")

    def test13_home_projecttype(self):
        """  13项目类型（开放）（进取、保本、稳赢）"""
        po = HomePage(self.driver)
        po.open( )
        sleep(2)
        projectmodehz = po.home12_projectmode( )  # 获取项目模式的中文
        if projectmodehz == "开放":
            trade_id = po.home10_projectname( )[1]
            projecttypehz = po.home13_projecttype( )
            if projecttypehz == "进取":
                projecttype = "manage"
            # elif projecttypehz == "稳盈":
            #     projecttype = "stable_profit"
            # elif projecttypehz == "保本":
            #     projecttype = "stable"
            else:
                projecttype = None
                print("项目类型错误")
            sql = "select trade_type from base_project WHERE trade_id=" + trade_id
            projecttype_db = getdata(sql)
            self.assertEqual(projecttype, projecttype_db, msg="项目类型与实际不符")
        else:
            print("封闭式项目，不适用本条用例")

    def test14_home_projectlead(self):
        """ 14领投金额（开放）"""
        po = HomePage(self.driver)
        po.open( )
        sleep(2)
        projectmodehz = po.home12_projectmode( )  # 获取项目模式的中文
        if projectmodehz == "开放":
            trade_id = po.home10_projectname( )[1]
            projectleadhz = po.honme14_projectlead( )  # 获取领投金额字段
            projectlead = Decimal("%.2f" % float(projectleadhz.split("￥")[-1]))  # 获取字段中的数字并保留两位小数
            sql = "select lead_invest_amount from base_project WHERE trade_id=" + trade_id
            projectlead_db = getdata(sql)
            self.assertEqual(projectlead, projectlead_db, msg="领投金额与实际不符")
        else:
            print("封闭式项目，不适用本条用例")

    def test15_home_projectquantity(self):
        """15投资笔数（开放）"""
        po = HomePage(self.driver)
        po.open( )
        sleep(2)
        projectmodehz = po.home12_projectmode( )  # 获取项目模式的中文
        if projectmodehz == "开放":
            trade_id = po.home10_projectname( )[1]
            projectquantity = int(po.home15_projectquantity( )[2:-1])
            sql = "select * from open_invest_apply WHERE state!='discard' and trade_id=" + trade_id
            projectquantity_db = getnum(sql)
            self.assertEqual(projectquantity, projectquantity_db, msg="投资笔试与实际不符")
        else:
            print("封闭式项目，不适用本条用例")

    def test16_home_projectcommisson(self):
        """ 16佣金比例（开放）"""
        po = HomePage(self.driver)
        po.open( )
        sleep(2)
        projectmodehz = po.home12_projectmode( )  # 获取项目模式的中文
        if projectmodehz == "开放":
            projectcommisson = Decimal("%.3f" % (float(po.home16_projectcommisson( )[:-1]) / 100))
            trade_id = po.home10_projectname( )[1]
            sql = "select commission from base_project WHERE trade_id=" + trade_id
            projectcommisson_db = getdata(sql)
            self.assertEqual(projectcommisson, projectcommisson_db, msg="佣金比例与实际不符")
        else:
            print("封闭式项目，不适用本条用例")

    def test17_home_projectclosure(self):
        """ 17退出周期（开放）"""
        po = HomePage(self.driver)
        po.open( )
        sleep(2)
        projectmodehz = po.home12_projectmode( )  # 获取项目模式的中文
        if projectmodehz == "开放":
            projectclosure = int(po.home17_projectclosure( ))
            trade_id = po.home10_projectname( )[1]
            sql = "select stage_closure from opening_project WHERE trade_id=" + trade_id
            projectclosure_db = getdata(sql)
            self.assertEqual(projectclosure, projectclosure_db, msg="退出周期与实际不符")
        else:
            print("封闭式项目，不适用本条用例")

    def test18_home_projectprofit(self):
        """ 18总收益率（开放）"""
        po = HomePage(self.driver)
        po.open( )
        sleep(2)
        projectmodehz = po.home12_projectmode( )  # 获取项目模式的中文
        if projectmodehz == "开放":
            projectprofit = round(float(po.home18_projectprofit( )[:-1]), 2)
            trade_id = po.home10_projectname( )[1]
            sql = "select float_profit_rate from dynamic_project WHERE trade_id=" + trade_id
            projectprofit_db = round(getdata(sql)*100, 2)
            self.assertEqual(projectprofit, projectprofit_db, msg="总收益与实际不符")

    def test19_home_godview(self):
        """ 19股神观点数量"""
        po = HomePage(self.driver)
        po.open( )
        sleep(2)
        godview = po.home19_godview( )
        self.assertEqual(godview, 5, msg="股神观点条数错误")

    def test20_home_helpercenter(self):
        """ 20帮助中心"""
        po = HomePage(self.driver)
        po.open( )
        sleep(2)
        helpercenter = po.home20_helpercenter( )
        self.assertEqual(helpercenter[0].text, "淘股神平台有什么优势？", msg="帮助中心标题错误")
        self.assertEqual(helpercenter[1].text, "淘股神平台有哪些产品？", msg="帮助中心标题错误")
        self.assertEqual(helpercenter[2].text, "如何参加淘股神炒股大赛？", msg="帮助中心标题错误")
        self.assertEqual(helpercenter[3].text, "如何申请淘股神平台的股神？", msg="帮助中心标题错误")
        self.assertEqual(helpercenter[4].text, "淘股神平台充值、提现限额介绍", msg="帮助中心标题错误")
        self.assertEqual(helpercenter[5].text, "淘股神账户余额生息介绍", msg="帮助中心标题错误")
        self.assertEqual(helpercenter[6].text, "淘股神平台相关名词解释", msg="帮助中心标题错误")

    def test21_home_media(self):
        """ 21媒体报道"""
        po = HomePage(self.driver)
        po.open( )
        sleep(2)
        media = po.home21_media( )
        self.assertEqual(media, 7, msg="媒体条数错误")

    def test22_home_projectamount(self):
        """ 22项目金额"""
        po = HomePage(self.driver)
        po.open( )
        sleep(2)
        projectamount = float(po.home22_projectamount( ).split(' ')[1])
        trade_id = po.home10_projectname( )[1]
        sql1 = "select applied_amount from dynamic_project WHERE trade_id=" + trade_id
        sql2 = "select market_value from opening_project WHERE trade_id=" + trade_id
        applied_amount = getdata(sql1)
        market_value = getdata(sql2)
        projectamount_db = int((applied_amount+market_value)/1000)/10
        self.assertEqual(projectamount_db, projectamount, msg="项目金额与实际不符")

"""
if __name__ == "__main__":
    runner = unittest.TextTestRunner( )
    suite = unittest.TestSuite( )
    # suite.addTest(HomeTest("test01_home_servicetel"))
    # suite.addTest(HomeTest("test02_home_newrequired"))
    # suite.addTest(HomeTest("test03_home_invite"))
    # suite.addTest(HomeTest("test04_home_startbuy"))
    # suite.addTest(HomeTest("test05_home_img1"))
    # suite.addTest(HomeTest("test07_home_img3"))
    # suite.addTest(HomeTest("test09_home_hmlist"))
    # suite.addTest(HomeTest("test10_home_projectname"))
    suite.addTest(HomeTest("test11_home_projectnickname"))
    # suite.addTest(HomeTest("test12_home_projectmode"))
    # suite.addTest(HomeTest("test13_home_projecttype"))
    # suite.addTest(HomeTest("test14_home_projectlead"))
    # suite.addTest(HomeTest("test15_home_projectquantity"))
    # suite.addTest(HomeTest("test16_home_projectcommisson"))
    # suite.addTest(HomeTest("test17_home_projectclosure"))
    # suite.addTest(HomeTest("test18_home_projectprofit"))
    # suite.addTest(HomeTest("test19_home_godview"))
    # suite.addTest(HomeTest("test20_home_helpercenter"))
    # suite.addTest(HomeTest("test21_home_media"))
    # suite.addTest(HomeTest("test22_home_projectamount"))
    runner.run(suite)
"""