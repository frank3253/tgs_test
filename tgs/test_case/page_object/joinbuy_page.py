from time import sleep
from selenium.webdriver.common.by import By
from .base import Base


class JoinBuy(Base):
    url = "projects"

    # 定位器
    # 01开放按钮
    kf_loc = (By.CLASS_NAME, "root-kf")
    # 02封闭按钮
    fbi_loc = (By.CLASS_NAME, "root-fbi ")
    # 03类型不限
    type_unlimited_loc = (By.XPATH, "//div[@class='root-fenlei']/div[1]/ul/li[1]/a")
    # 04类型进取
    manage_loc = (By.XPATH, "//div[@class='root-fenlei']/div[1]/ul/li[2]/a")
    # 05类型保本
    stable_loc = (By.XPATH, "//div[@class='root-fenlei']/div[1]/ul/li[3]/a")
    # 06类型稳赢
    stable_profit_loc = (By.XPATH, "//div[@class='root-fenlei']/div[1]/ul/li[4]/a")
    # 07状态不限
    state_unlimited_loc = (By.XPATH, "//div[@class='root-fenlei']/div[2]/ul/li[1]/a")
    # 08状态投资中
    state_invest_loc = (By.XPATH, "//div[@class='root-fenlei']/div[2]/ul/li[2]/a")
    # 09状态操盘中
    state_operate_loc = (By.XPATH, "//div[@class='root-fenlei']/div[2]/ul/li[3]/a")
    # 10状态已结束
    state_end_loc = (By.XPATH, "//div[@class='root-fenlei']/div[2]/ul/li[4]/a")
    # 11产品不限
    product_unlimited_loc = (By.XPATH, "//div[@class='root-fenlei']/div[3]/ul/li[1]/a")
    # 12产品股票
    product_shares_loc = (By.XPATH, "//div[@class='root-fenlei']/div[3]/ul/li[2]/a")
    # 13产品期货
    product_futures_loc = (By.XPATH, "//div[@class='root-fenlei']/div[3]/ul/li[3]/a")
    # 14总收益率按钮
    profit_loc = (By.XPATH, ".//*[@id='this_text']")
    # 15（选项）总收益率
    projectprofit_loc = (By.XPATH, "/html/body/div[5]/ul[1]/li/div[2]/a[1]")
    # 16（选项）近30天收益
    d30profit_loc = (By.XPATH, "/html/body/div[5]/ul[1]/li/div[2]/a[2]")
    # 17（选项）近7天收益
    d7profit_loc = (By.XPATH, "/html/body/div[5]/ul[1]/li/div[2]/a[3]")
    # 18（选项）近1天收益
    d1profit_loc = (By.XPATH, "/html/body/div[5]/ul[1]/li/div[2]/a[4]")
    # 19股神评级
    certify_level_loc = (By.XPATH, "//ul[@class='root-pxu']/li[1]")
    # 20交易周期
    stage_closure_loc = (By.XPATH, "//ul[@class='root-pxu']/li[2]")
    # 21佣金
    commission_loc = (By.XPATH, "//ul[@class='root-pxu']/li[3]")
    # 22总金额
    projetcamount_loc = (By.XPATH, "//ul[@class='root-pxu']/li[4]")
    # 23股神出资
    lead_amount_loc = (By.XPATH, "//ul[@class='root-pxu']/li[5]")
    # 24投资笔数
    amount_num_loc = (By.XPATH, "//ul[@class='root-pxu']/li[6]")
    # 25搜索输入框
    ssk_loc = (By.XPATH, "//*[ @id='root-ssk']")
    sskbutton_loc = (By.XPATH, "//div[@class='root-ssk']/i")
    # 26项目列表是否为空
    isnone_loc = (By.XPATH, "//div[@class='org lag']")

    # (开放)(不限)
    open_name_loc = (By.XPATH, "/html/body/div[6]/div[5]/div[1]/div[2]/h3/a")  # 27项目名称(ID)
    open_nickname_loc = (By.XPATH, "/html/body/div[6]/div[5]/div[1]/div[1]/div[3]/a")  # 28股神名
    open_type1_loc = (By.XPATH, "/html/body/div[6]/div[5]/div[1]/div[2]/div[1]/div[1]")  # 29类型
    open_amount_loc = (By.XPATH, "/html/body/div[6]/div[5]/div[1]/div[2]/div[2]/div[1]")  # 30项目金额
    open_quantity_loc = (By.XPATH, "/html/body/div[6]/div[5]/div[1]/div[2]/div[2]/div[2]/span[1]")  # 31已投笔数
    open_lead_loc = (By.XPATH, "/html/body/div[6]/div[5]/div[1]/div[2]/div[2]/div[2]/span[2]")  # 32领投金额
    open_losure_loc = (By.XPATH, "/html/body/div[6]/div[5]/div[2]/span[2]/em")  # 33退出周期
    open_commisson_loc = (By.XPATH, "/html/body/div[6]/div[5]/div[3]/span[2]/em")  # 34项目佣金
    open_profit_loc = (By.XPATH, "/html/body/div[6]/div[5]/div[4]/span[2]/em")  # 35总收益

    # (封闭)(进取)(投资中)先判断列表不为空
    normalmanage_phase1_loc = (By.XPATH, "/html/body/div[6]/div[1]/div[6]/a")  # 36项目阶段(等待投资/正在投资)
    normalmanage_type2_loc = (By.XPATH, "/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/div[1]")  # 37项目类型
    normalmanage_name1_loc = (By.XPATH, "/html/body/div[6]/div[1]/div[1]/div[2]/h3/a")  # 38项目名称(ID)
    normalmanage_user_loc = (By.XPATH, "/html/body/div[6]/div[1]/div[1]/div[1]/div[3]")  # 39股神名
    normalmanage_amount_loc = (By.XPATH, "/html/body/div[6]/div[1]/div[1]/div[2]/div[2]/div")  # 40项目金额
    normalmanage_losure_loc = (By.XPATH, "/html/body/div[6]/div[1]/div[2]/span[2]/em")  # 41交易周期
    normalmanage_commisson_loc = (By.XPATH, "/html/body/div[6]/div[1]/div[3]/span[2]/em")  # 42项目佣金
    normalmanage_stop_loc = (By.XPATH, "/html/body/div[6]/div[1]/div[4]/span[2]/em")  # 43止损值
    normalmanage_residue_loc = (By.XPATH, "/html/body/div[6]/div[1]/div[5]/span[2]/em")  # 44剩余可投
    # (封闭)(进取)(操盘中)先判断列表不为空
    normalmanage_name2_loc = (By.XPATH, "/html/body/div[6]/div[1]/div[1]/div[2]/h3/a")  # 45项目名称(ID)
    normalmanage_phase2_loc = (By.XPATH, "/html/body/div[6]/div[1]/div[6]/a")  # 46项目阶段
    normalmanage_float_loc = (By.XPATH, "/html/body/div[6]/div[1]/div[5]/span[2]/em")  # 47浮动收益
    # (封闭)(进取)(已结束)先判断列表不为空
    normalmanage_name3_loc = (By.XPATH, "/html/body/div[6]/div[5]/div[1]/div[2]/h3/a")  # 48项目名称(ID)
    normalmanage_phase3_loc = (By.XPATH, "/html/body/div[6]/div[5]/a")  # 49项目阶段(停牌中/已结束)
    normalmanage_profit_loc = (By.XPATH, "/html/body/div[6]/div[5]/div[5]/span[2]/em")  # 50收益率
    # (封闭)(保本)先判断列表不为空
    normalstable_type3_loc = (By.XPATH, "/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/div[1]")  # 51项目类型
    # (封闭)(稳赢)(不限)
    normalprofit_name_loc = (By.XPATH, "/html/body/div[6]/div[1]/div[1]/div[2]/h3/a")  # 52项目名称(ID)
    normalprofit_guarantee_loc = (By.XPATH, "/html/body/div[6]/div[1]/div[4]/span[2]/em[1]")  # 53保底收益
    normalprofit_type4_loc = (By.XPATH, "/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/div[1]")  # 54项目类型

    # (封闭)(股票/期货)先判断列表不为空
    normalshares_name_loc = (By.XPATH, "//div[@class='root-y']/h3/a")  # 55项目名称(ID)

    def joinbuy01_kf(self):  # 01开放按钮
        self.find_element(*self.kf_loc).click( )
        sleep(2)

    def joinbuy02_fbi(self):  # 02封闭按钮
        self.find_element(*self.fbi_loc).click( )
        sleep(2)

    def joinbuy03_type_unlimited(self):  # 03类型不限
        self.find_element(*self.type_unlimited_loc).click( )
        sleep(1)

    def joinbuy04_manage(self):  # 04类型进取
        self.find_element(*self.manage_loc).click( )
        sleep(1)

    def joinbuy05_stable(self):  # 05类型保本
        self.find_element(*self.stable_loc).click( )
        sleep(1)

    def joinbuy06_stable_stable_profit(self):  # 06类型稳赢
        self.find_element(*self.stable_profit_loc).click( )
        sleep(1)

    def joinbuy07_state_unlimited(self):  # 07状态不限
        self.find_element(*self.state_unlimited_loc).click( )
        sleep(1)

    def joinbuy08_state_invest(self):  # 08状态投资中
        self.find_element(*self.state_invest_loc).click( )
        sleep(1)

    def joinbuy09_state_operate(self):  # 09状态操盘中
        self.find_element(*self.state_operate_loc).click( )
        sleep(1)

    def joinbuy10_state_end(self):  # 10状态已结束
        self.find_element(*self.state_end_loc).click( )
        sleep(1)

    def joinbuy11_product_unlimited(self):  # 11产品不限
        self.find_element(*self.product_unlimited_loc).click( )
        sleep(1)

    def joinbuy12_product_shares(self):  # 12产品股票
        self.find_element(*self.product_shares_loc).click( )
        sleep(1)

    def joinbuy13_product_futures(self):  # 13产品期货
        self.find_element(*self.product_futures_loc).click( )
        sleep(1)

    def joinbuy14_profit(self):  # 14总收益率按钮
        self.find_element(*self.profit_loc).click( )
        sleep(1)

    def joinbuy15_projectprofit(self):  # 15（选项）总收益率
        self.find_element(*self.projectprofit_loc).click( )
        sleep(1)

    def joinbuy16_d30profit(self):  # 16（选项）近30天收益
        self.find_element(*self.d30profit_loc).click( )
        sleep(1)

    def joinbuy17_d7profit(self):  # 17（选项）近7天收益
        self.find_element(*self.d7profit_loc).click( )
        sleep(1)

    def joinbuy18_d1profit(self):  # 18（选项）近1天收益
        self.find_element(*self.d1profit_loc).click( )
        sleep(1)

    def joinbuy19_certify_level(self):  # 19股神评级
        self.find_element(*self.certify_level_loc).click( )
        sleep(1)

    def joinbuy20_stage_closure(self):  # 20交易周期
        self.find_element(*self.stage_closure_loc).click( )
        sleep(1)

    def joinbuy21_commission(self):  # 21佣金
        self.find_element(*self.commission_loc).click( )
        sleep(1)

    def joinbuy22_projetcamount(self):  # 22总金额
        self.find_element(*self.projetcamount_loc).click( )
        sleep(2)

    def joinbuy23_lead_amount(self):  # 23股神出资
        self.find_element(*self.lead_amount_loc).click( )
        sleep(2)

    def joinbuy24_amount_num(self):  # 24投资笔数
        self.find_element(*self.amount_num_loc).click( )
        sleep(1)

    def joinbuy25_ssk(self, key):  # 25搜索输入框
        self.find_element(*self.ssk_loc).clear( )
        self.find_element(*self.ssk_loc).send_keys(key)
        self.find_element(*self.sskbutton_loc).click( )
        sleep(1)

    def joinbuy26_isnone(self):  # 26项目列表是否为空
        element = self.find_elements(*self.isnone_loc)
        if len(element) == 0:
            return True
        else:
            return False

    def joinbuy27_open_name(self):
        element = self.find_element(*self.open_name_loc)
        trade_id = element.get_attribute("href").split("/")[-1]
        projectname = element.text
        return projectname, trade_id

    def joinbuy28_open_nickname(self):
        nickname = self.find_element(*self.open_nickname_loc).text
        return nickname

    def joinbuy29_open_type(self):
        type1 = self.find_element(*self.open_type1_loc).text
        return type1

    def joinbuy30_open_amount(self):
        amount = self.find_element(*self.open_amount_loc).text
        return amount

    def joinbuy31_open_quantity(self):
        quantity = self.find_element(*self.open_quantity_loc).text
        return quantity

    def joinbuy32_open_lead(self):
        lead = self.find_element(*self.open_lead_loc).text
        return lead

    def joinbuy33_open_losure(self):
        losure = self.find_element(*self.open_losure_loc).text
        return losure

    def joinbuy34_open_commisson(self):
        commisson = self.find_element(*self.open_commisson_loc).text
        return commisson

    def joinbuy35_open_profit(self):
        profit = self.find_element(*self.open_profit_loc).text
        return profit

    def joinbuy36_normalmanage_phase1(self):
        phase1 = self.find_element(*self.normalmanage_phase1_loc).text
        return phase1

    def joinbuy37_normalmanage_type(self):
        type2 = self.find_element(*self.normalmanage_type2_loc).text
        return type2

    def joinbuy38_normalmanage_name1(self):
        element = self.find_element(*self.normalmanage_name1_loc)
        trade_id = element.get_attribute("href").split("/")[-1]
        projectname = element.text
        return projectname, trade_id

    def joinbuy39_normalmanage_user(self):
        user = self.find_element(*self.normalmanage_user_loc).text
        return user

    def joinbuy40_normalmanage_amount(self):
        amount = self.find_element(*self.normalmanage_amount_loc).text
        return amount

    def joinbuy41_normalmanage_losure(self):
        losure = self.find_element(*self.normalmanage_losure_loc).text
        return losure

    def joinbuy42_normalmanage_commisson(self):
        commisson = self.find_element(*self.normalmanage_commisson_loc).text
        return commisson

    def joinbuy43_normalmanage_stop(self):
        stopvalue = self.find_element(*self.normalmanage_stop_loc).text
        return stopvalue

    def joinbuy44_normalmanage_residue(self):
        residue = self.find_element(*self.normalmanage_residue_loc).text
        return residue

    def joinbuy45_normalmanage_name2(self):
        element = self.find_element(*self.normalmanage_name2_loc)
        trade_id = element.get_attribute("href").split("/")[-1]
        projectname = element.text
        return projectname, trade_id

    def joinbuy46_normalmanage_phase2(self):
        phase2 = self.find_element(*self.normalmanage_phase2_loc).text
        return phase2

    def joinbuy47_normalmanage_float(self):
        floatvalue = self.find_element(*self.normalmanage_float_loc).text
        return floatvalue

    def joinbuy48_normalmanage_name3(self):
        element = self.find_element(*self.normalmanage_name3_loc)
        trade_id = element.get_attribute("href").split("/")[-1]
        projectname = element.text
        return projectname, trade_id

    def joinbuy49normalmanage_phase3(self):
        phase3 = self.find_element(*self.normalmanage_phase3_loc).text
        return phase3

    def joinbuy50_normalmanage_profit(self):
        profit = self.find_element(*self.normalmanage_profit_loc).text
        return profit

    def joinbuy51_normalstable_type(self):
        type3 = self.find_element(*self.normalstable_type3_loc).text
        return type3

    def joinbuy52_normalprofit_name(self):
        element = self.find_element(*self.normalprofit_name_loc)
        trade_id = element.get_attribute("href").split("/")[-1]
        projectname = element.text
        return projectname, trade_id

    def joinbuy53_normalprofit_guarantee(self):
        guarantee = self.find_element(*self.normalprofit_guarantee_loc).text
        return guarantee

    def joinbuy54_normalprofit_type(self):
        type4 = self.find_element(*self.normalprofit_type4_loc).text
        return type4

    def joinbuy55_productlist_name(self):
        elements = self.find_elements(*self.normalshares_name_loc)
        return elements

    def get_id(self, element):
        trade_id = element.get_attribute("href").split("/")[-1]
        return trade_id
