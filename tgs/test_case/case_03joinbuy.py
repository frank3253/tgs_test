# coding = utf-8
"""
Created on 2017-11-24
@author: yanhao
Project:合买页面的测试用例，覆盖排序功能、搜索功能、列表中的数据校验
"""
from datetime import datetime
from decimal import Decimal
from time import sleep
import unittest, random, sys
from tgs.test_case.model.mdb import getdata, getnum
from tgs.test_case.page_object.joinbuy_page import JoinBuy
from tgs.test_case.model import myunit, function, config
from selenium.webdriver.common.by import By

sys.path.append('./model')
sys.path.append('./page_object')


class JoinBuyTest(myunit.MyTest):
    # 开放式数据校验、封闭式筛选功能、封闭式数据校验（共27条）
    def test01_joinbuy_kf(self):
        """01 开放式按钮校验"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        po.joinbuy01_kf( )
        url = po.driver.current_url
        trade_id = po.joinbuy27_open_name( )[1]
        sql = "select project_mode from base_project WHERE trade_id=" + trade_id
        mode = getdata(sql)
        self.assertEqual(mode, "open_mode", msg="开放式按钮无效")
        self.assertIn("mode=open_mode", url, msg="开放式按钮跳转错误")

    def test02_joinbuy_fbi(self):
        """02 封闭式按钮校验"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        po.joinbuy02_fbi( )
        url = po.driver.current_url
        trade_id = po.joinbuy27_open_name( )[1]
        sql = "select project_mode from base_project WHERE trade_id=" + trade_id
        mode = getdata(sql)
        self.assertEqual(mode, "normal_mode", msg="封闭式按钮无效")
        self.assertIn("mode=normal_mode", url, msg="封闭式按钮跳转错误")

    def test03_joinbuy_nickname(self):
        """03 (开放)产品股神名字校验"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        nickname = po.joinbuy28_open_nickname( )
        trade_id = po.joinbuy27_open_name( )[1]
        sql1 = "select user_name from base_project WHERE trade_id=" + trade_id
        user_name = getdata(sql1)
        sql2 = "select nick_name from user_base_info WHERE user_name=" + "'" + user_name + "'"
        nickname_db = getdata(sql2)
        self.assertEqual(nickname_db, nickname, msg="用户昵称与实际不符")

    def test04_joinbuy_opentype(self):
        """04 (开放)项目类型校验"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        opentype = po.joinbuy29_open_type( )
        if opentype == "进取":
            realtype = "manage"
        trade_id = po.joinbuy27_open_name( )[1]
        sql = "select trade_type from base_project WHERE trade_id=" + trade_id
        type_db = getdata(sql)
        self.assertEqual(realtype, type_db, msg="类型与实际不符")

    def test05_joinbuy_openamount(self):
        """05 (开放)项目金额"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        openamount = float(po.joinbuy30_open_amount( ).split(" ")[1])
        trade_id = po.joinbuy27_open_name( )[1]
        sql1 = "select applied_amount from dynamic_project WHERE trade_id=" + trade_id
        sql2 = "select market_value from opening_project WHERE trade_id=" + trade_id
        applied_amount = getdata(sql1)
        market_value = getdata(sql2)
        openamount_db = int((applied_amount + market_value) / 1000) / 10
        self.assertEqual(openamount_db, openamount, msg="总金额与实际不符")

    def test06_joinbuy_quantity(self):
        """06 (开放)已投笔数"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        quantity = po.joinbuy31_open_quantity( )[-2]
        trade_id = po.joinbuy27_open_name( )[1]
        sql = "select * from open_invest_apply WHERE state!='discard' and trade_id=" + trade_id
        quantity_db = getnum(sql)
        self.assertEqual(str(quantity_db), quantity, msg="投资笔数与实际不符")

    def test07_joinbuy_lead(self):
        """07 (开放)领投金额"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        lead = po.joinbuy32_open_lead( ).split('￥')[-1]
        trade_id = po.joinbuy27_open_name( )[1]
        sql = "select lead_invest_amount from base_project WHERE trade_id=" + trade_id
        lead_db = getdata(sql)
        self.assertEqual(lead, str(lead_db), msg="领投金额与实际不符")

    def test08_joinbuy_losure(self):
        """08 (开放)退出周期"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        losure = po.joinbuy33_open_losure( )
        trade_id = po.joinbuy27_open_name( )[1]
        sql = "select stage_closure from opening_project WHERE trade_id=" + trade_id
        losure_db = getdata(sql)
        self.assertEqual(str(losure_db), losure, msg="退出周期与实际不符")

    def test09_joinbuy_commission(self):
        """09 (开放)项目佣金"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        commission = Decimal("%.3f" % (float(po.joinbuy34_open_commisson( )) / 100))
        trade_id = po.joinbuy27_open_name( )[1]
        sql = "select commission from base_project WHERE trade_id=" + trade_id
        commission_db = getdata(sql)
        self.assertEqual(commission_db, commission, msg="佣金与实际不符")

    def test10_joinbuy_profit(self):
        """10 (开放)总收益"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        profit = round(float(po.joinbuy35_open_profit( )), 2)
        trade_id = po.joinbuy27_open_name( )[1]
        sql = "select float_profit_rate from dynamic_project WHERE trade_id=" + trade_id
        profit_db = round(getdata(sql) * 100, 2)
        self.assertEqual(profit_db, profit, msg="总收益与实际不符")

    def test11_joinbuy_phase1(self):
        """11 (封闭)(进取)(投资中)项目阶段"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        po.joinbuy02_fbi( )
        po.joinbuy04_manage( )
        po.joinbuy08_state_invest( )
        if po.joinbuy26_isnone( ):
            phase1 = po.joinbuy36_normalmanage_phase1( )
            self.assertIn(phase1, "等待投资/正在投资", msg="投资中筛选无效")
            trade_id = po.joinbuy38_normalmanage_name1( )[1]
            sql = "select expire_date from base_project WHERE trade_id=" + trade_id
            expiretime = getdata(sql)
            nowtime = datetime.now( )
            self.assertTrue(nowtime < expiretime, msg="项目实际阶段错误")
        else:
            print("该项目列表为空")

    def test12_joinbuy_type(self):
        """12 (封闭)(进取)(投资中)项目类型"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        po.joinbuy02_fbi( )
        po.joinbuy04_manage( )
        po.joinbuy08_state_invest( )
        if po.joinbuy26_isnone( ):
            objecttype = po.joinbuy37_normalmanage_type( )
            self.assertEqual(objecttype, "进取", msg="类型-进取按钮无效")
            trade_id = po.joinbuy38_normalmanage_name1( )[1]
            sql = "select trade_type from base_project WHERE trade_id=" + trade_id
            tradetype = getdata(sql)
            self.assertEqual(tradetype, "manage", msg="项目实际类型错误")
        else:
            print("该项目列表为空")

    def test13_joinbuy_nickname(self):
        """13 (封闭)(进取)(投资中)股神名"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        po.joinbuy02_fbi( )
        po.joinbuy04_manage( )
        po.joinbuy08_state_invest( )
        if po.joinbuy26_isnone( ):
            nickname = po.joinbuy39_normalmanage_user( )
            trade_id = po.joinbuy38_normalmanage_name1( )[1]
            sql1 = "select user_name from base_project WHERE trade_id=" + trade_id
            user_name = getdata(sql1)
            sql2 = "select nick_name from user_base_info WHERE user_name=" + "'" + user_name + "'"
            nickname_db = getdata(sql2)
            self.assertEqual(nickname, nickname_db, msg="股神名与实际不符")
        else:
            print("该项目列表为空")

    def test14_joinbuy_amount(self):
        """14 (封闭)(进取)(投资中)项目金额"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        po.joinbuy02_fbi( )
        po.joinbuy04_manage( )
        po.joinbuy08_state_invest( )
        if po.joinbuy26_isnone( ):
            amount = float(po.joinbuy40_normalmanage_amount( ).split(" ")[1])
            trade_id = po.joinbuy38_normalmanage_name1( )[1]
            sql = "select trade_amount from base_project WHERE trade_id=" + trade_id
            amount_db = int(getdata(sql) / 1000) / 10
            self.assertEqual(amount_db, amount, msg="总金额与实际不符")
        else:
            print("该项目列表为空")

    def test15_joinbuy_losure(self):
        """15 (封闭)(进取)(投资中)交易周期"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        po.joinbuy02_fbi( )
        po.joinbuy04_manage( )
        po.joinbuy08_state_invest( )
        if po.joinbuy26_isnone( ):
            losure = int(po.joinbuy41_normalmanage_losure( ))
            trade_id = po.joinbuy38_normalmanage_name1( )[1]
            sql = "select period from base_project WHERE trade_id=" + trade_id
            losure_db = getdata(sql)
            self.assertEqual(losure_db, losure, msg="交易周期与实际不符")
        else:
            print("该项目列表为空")

    def test16_joinbuy_commisson(self):
        """16 (封闭)(进取)(投资中)项目佣金"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        po.joinbuy02_fbi( )
        po.joinbuy04_manage( )
        po.joinbuy08_state_invest( )
        if po.joinbuy26_isnone( ):
            commission = Decimal("%.3f" % (float(po.joinbuy42_normalmanage_commisson( )) / 100))
            trade_id = po.joinbuy38_normalmanage_name1( )[1]
            sql = "select commission from base_project WHERE trade_id=" + trade_id
            commission_db = getdata(sql)
            self.assertEqual(commission, commission_db, msg="项目佣金与实际不符")
        else:
            print("该项目列表为空")

    def test17_joinbuy_stop(self):
        """17 (封闭)(进取)(投资中)止损值"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        po.joinbuy02_fbi( )
        po.joinbuy04_manage( )
        po.joinbuy08_state_invest( )
        if po.joinbuy26_isnone( ):
            stopvalue = Decimal("%.2f" % float(po.joinbuy43_normalmanage_stop( ).split("-")[1]))
            trade_id = po.joinbuy38_normalmanage_name1( )[1]
            sql = "select stop_rate from base_project WHERE trade_id=" + trade_id
            stopvalue_db = getdata(sql)
            self.assertEqual(stopvalue_db, stopvalue, msg="项目止损值与实际不符")
        else:
            print("该项目列表为空")

    def test18_joinbuy_residue(self):
        """18 (封闭)(进取)(投资中)剩余可投"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        po.joinbuy02_fbi( )
        po.joinbuy04_manage( )
        po.joinbuy08_state_invest( )
        if po.joinbuy26_isnone( ):
            residue = float(po.joinbuy44_normalmanage_residue( ))
            trade_id = po.joinbuy38_normalmanage_name1( )[1]
            sql1 = "select loaned_amount from dynamic_project WHERE trade_id=" + trade_id  # 已经募集资金
            sql2 = "select trade_amount from base_project WHERE trade_id=" + trade_id  # 募集期限额
            loaned_amount = getdata(sql1)
            trade_amount = getdata(sql2)
            residue_db = float("%.1f" % int((trade_amount - loaned_amount) / 1000)) / 10
            self.assertEqual(residue_db, residue, msg="剩余可投与实际不符")
        else:
            print("该项目列表为空")

    def test19_joinbuy_phase2(self):
        """19 (封闭)(进取)(操盘中)项目阶段"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        po.joinbuy02_fbi( )
        po.joinbuy04_manage( )
        po.joinbuy09_state_operate( )
        if po.joinbuy26_isnone( ):
            phase2 = po.joinbuy46_normalmanage_phase2( )
            self.assertIn(phase2, "操盘中/等待操盘", msg="操盘中筛选无效")
            trade_id = po.joinbuy45_normalmanage_name2( )[1]
            sql1 = "select expire_date from base_project WHERE trade_id=" + trade_id
            sql2 = "select opstock_end_date from base_project WHERE trade_id=" + trade_id
            expiretime = getdata(sql1)
            opstock_end_date = getdata(sql2)
            nowtime = datetime.now( )
            self.assertTrue(nowtime > expiretime & opstock_end_date > nowtime, msg="项目实际阶段错误")
        else:
            print("该项目列表为空")

    def test20_joinbuy_float(self):
        """20 (封闭)(进取)(操盘中)浮动收益"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        po.joinbuy02_fbi( )
        po.joinbuy04_manage( )
        po.joinbuy09_state_operate( )
        if po.joinbuy26_isnone( ):
            floatvalue = float(po.joinbuy47_normalmanage_float( ))
            trade_id = po.joinbuy45_normalmanage_name2( )[1]
            sql = "select float_profit_rate from dynamic_project WHERE trade_id=" + trade_id
            floatvalue_db = float("%.2f" % (getdata(sql) * 100))
            self.assertEqual(floatvalue_db, floatvalue, msg="项目浮动收益与实际不符")
        else:
            print("该项目列表为空")

    def test21_joinbuy_phase3(self):
        """21 (封闭)(进取)(已结束)项目阶段"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        po.joinbuy02_fbi( )
        po.joinbuy04_manage( )
        po.joinbuy10_state_end( )
        if po.joinbuy26_isnone( ):  # 如果列表不为空
            phase3 = po.joinbuy49normalmanage_phase3( )
            self.assertIn(phase3, "停牌中/已结束", msg="已结束筛选无效")
            trade_id = po.joinbuy48_normalmanage_name3( )[1]
            sql1 = "select trade_finish_date from base_project WHERE trade_id=" + trade_id  # '完成日期'
            sql2 = "select opstock_end_date from base_project WHERE trade_id=" + trade_id  # '操盘结束如期'
            sql3 = "select opstock_last_date from base_project WHERE trade_id=" + trade_id  # '最后操盘日期'
            finish_date = getdata(sql1).strftime("%Y-%m-%d %H:%M:%S")
            end_date = getdata(sql2).strftime("%Y-%m-%d %H:%M:%S")
            last_date = getdata(sql3).strftime("%Y-%m-%d %H:%M:%S")
            nowtime = datetime.now( ).strftime("%Y-%m-%d %H:%M:%S")
            if self.assertIsNotNone(finish_date):
                self.assertTrue(nowtime > finish_date, msg="项目实际阶段错误")
            else:
                # print(end_date,last_date,nowtime)
                self.assertTrue(nowtime > end_date and nowtime > last_date, msg="项目实际阶段错误")
        else:
            print("该项目列表为空")

    def test22_joinbuy_profit(self):
        """22 (封闭)(进取)(已结束)收益率"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        po.joinbuy02_fbi( )
        po.joinbuy04_manage( )
        po.joinbuy10_state_end( )
        if po.joinbuy26_isnone( ):  # 如果列表不为空
            profit = Decimal("%.2f" % float(po.joinbuy50_normalmanage_profit( )))
            trade_id = po.joinbuy48_normalmanage_name3( )[1]
            sql = "select float_profit_rate from dynamic_project WHERE trade_id=" + trade_id
            profit_db = Decimal("%.2f" % (getdata(sql) * 100))
            self.assertEqual(profit_db, profit, msg="项目收益率与实际不符")
        else:
            print("该项目列表为空")

    def test23_joinbuy_type(self):
        """23 (封闭)(保本)项目类型"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        po.joinbuy02_fbi( )
        po.joinbuy05_stable( )
        if po.joinbuy26_isnone( ):  # 如果列表不为空
            objecttype = po.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/div[1]").text
            self.assertEqual(objecttype, "保本", msg="保本筛选功能无效")
            trade_id = po.joinbuy38_normalmanage_name1( )[1]
            sql = "select trade_type from base_project WHERE trade_id=" + trade_id
            self.assertEqual(getdata(sql), "stable", msg="项目类型与实际不符")
        else:
            print("该项目列表为空")

    def test24_joinbuy_type(self):
        """24 (封闭)(稳赢)项目类型"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        po.joinbuy02_fbi( )
        po.joinbuy06_stable_stable_profit( )
        if po.joinbuy26_isnone( ):
            objecttype = po.joinbuy54_normalprofit_type( )
            self.assertEqual(objecttype, "稳盈", msg="稳盈筛选按钮无效")
            trade_id = po.joinbuy52_normalprofit_name( )[1]
            sql = "select trade_type from base_project WHERE trade_id=" + trade_id
            self.assertEqual(getdata(sql), "stable_profit", msg="项目类型与实际不符")
        else:
            print("该项目列表为空")

    def test25_joinbuy_guarantee(self):
        """25 (封闭)(稳赢)保底收益"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        po.joinbuy02_fbi( )
        po.joinbuy06_stable_stable_profit( )
        if po.joinbuy26_isnone( ):
            guarantee = Decimal("%.4f" % (float(po.joinbuy53_normalprofit_guarantee( )) / 100))
            trade_id = po.joinbuy52_normalprofit_name( )[1]
            sql = "select promise_profit_ratio from base_project WHERE trade_id=" + trade_id
            guarantee_db = getdata(sql)
            self.assertEqual(guarantee_db, guarantee, msg="项目保底收益与实际不符")
        else:
            print("该项目列表为空")

    def test26_joinbuy_shares(self):
        """26 (封闭)股票"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        po.joinbuy02_fbi( )
        po.joinbuy12_product_shares( )
        if po.joinbuy26_isnone( ):
            elements = po.joinbuy55_productlist_name( )
            for i in elements:
                trade_id = po.get_id(i)
                sql = "select product_type from base_project WHERE trade_id=" + trade_id
                product_type = getdata(sql)
                self.assertEqual(product_type, "stock", msg="股票筛选按钮无效")
        else:
            print("该项目列表为空")

    def test27_joinbuy_futures(self):
        """27 (封闭)期货"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        po.joinbuy02_fbi( )
        po.joinbuy13_product_futures( )
        if po.joinbuy26_isnone( ):
            elements = po.joinbuy55_productlist_name( )  # 取出元素列表循环列表比较各个投资类型
            for i in elements:
                trade_id = po.get_id(i)
                sql = "select product_type from base_project WHERE trade_id=" + trade_id
                product_type = getdata(sql)
                self.assertEqual(product_type, "futures", msg="股票筛选按钮无效")
        else:
            print("该项目列表为空")

    # 开放式排序、封闭式排序测试用例（20条）
    def test28_joinbuy_profit_sort(self):
        """28 (开放式排序)总收益"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        po.joinbuy14_profit( )
        po.joinbuy15_projectprofit( )
        elements = po.joinbuy55_productlist_name( )
        num = len(elements)
        i = 0
        while (i + 1) < num:
            trade_id = po.get_id(elements[i])
            sql = "select float_profit_rate from dynamic_project where trade_id=" + trade_id
            profit1 = getdata(sql)
            i += 1
            trade_id = po.get_id(elements[i])
            sql = "select float_profit_rate from dynamic_project where trade_id=" + trade_id
            profit2 = getdata(sql)
            self.assertTrue(profit1 >= profit2, msg="总收益排序无效")

    @unittest.skip("测试数据不支持该用例")
    def test29_joinbuy_d30profit_sort(self):
        """29 (开放式排序)近30天收益"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        po.joinbuy14_profit( )
        po.joinbuy16_d30profit( )
        elements = po.joinbuy55_productlist_name( )
        num = len(elements)
        i = 0
        while (i + 1) < num:
            trade_id = po.get_id(elements[i])

    @unittest.skip("测试数据不支持该用例")
    def test30_joinbuy_d7profi_sort(self):
        """30 (开放式排序)近7天收益"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        po.joinbuy14_profit( )
        po.joinbuy17_d7profit( )
        elements = po.joinbuy55_productlist_name( )
        num = len(elements)

    @unittest.skip("测试数据不支持该用例")
    def test31_joinbuy_d1profit_sort(self):
        """31 (开放式排序)近1天收益"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        po.joinbuy14_profit( )
        po.joinbuy18_d1profit( )
        elements = po.joinbuy55_productlist_name( )
        num = len(elements)

    def test32_joinbuy_godlevel_sort(self):
        """32 (开放式排序)股神评级"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        po.joinbuy19_certify_level( )  # 点一次从高到低排序
        elements = po.joinbuy55_productlist_name( )
        num = len(elements)
        i = 0
        while (i + 1) < num:
            trade_id = po.get_id(elements[i])
            sql = "select user_name from base_project where trade_id=" + trade_id
            user_name = getdata(sql)
            sql = "select user_id from user_base_info where user_name=" + '"' + user_name + '"'
            user_id = str(getdata(sql))
            sql = "select certify_level from god where user_id=" + user_id
            god_level1 = getdata(sql)
            i += 1
            trade_id = po.get_id(elements[i])
            sql = "select user_name from base_project where trade_id=" + trade_id
            user_name = getdata(sql)
            sql = "select user_id from user_base_info where user_name=" + '"' + user_name + '"'
            user_id = str(getdata(sql))
            sql = "select certify_level from god where user_id=" + user_id
            god_level2 = getdata(sql)
            self.assertTrue(god_level1 >= god_level2, msg="按股神评级排序无效")

        po.joinbuy19_certify_level( )  # 点两次从低到高排列
        elements = po.joinbuy55_productlist_name( )
        num = len(elements)
        i = 0
        while (i + 1) < num:
            trade_id = po.get_id(elements[i])
            sql = "select user_name from base_project where trade_id=" + trade_id
            user_name = getdata(sql)
            sql = "select user_id from user_base_info where user_name=" + '"' + user_name + '"'
            user_id = str(getdata(sql))
            sql = "select certify_level from god where user_id=" + user_id
            god_level1 = getdata(sql)
            i += 1
            trade_id = po.get_id(elements[i])
            sql = "select user_name from base_project where trade_id=" + trade_id
            user_name = getdata(sql)
            sql = "select user_id from user_base_info where user_name=" + '"' + user_name + '"'
            user_id = str(getdata(sql))
            sql = "select certify_level from god where user_id=" + user_id
            god_level2 = getdata(sql)
            self.assertTrue(god_level1 <= god_level2, msg="按股神评级排序无效")

    def test33_joinbuy_closure_sort(self):
        """33 (开放式排序)交易周期"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        po.joinbuy20_stage_closure( )
        elements = po.joinbuy55_productlist_name( )
        num = len(elements)
        i = 0
        while (i + 1) < num:
            trade_id = po.get_id(elements[i])
            sql = "select stage_closure from opening_project WHERE trade_id=" + trade_id
            closure1 = getdata(sql)
            i += 1
            trade_id = po.get_id(elements[i])
            sql = "select stage_closure from opening_project WHERE trade_id=" + trade_id
            closure2 = getdata(sql)
            self.assertTrue(closure1 >= closure2, msg="按交易周期排序无效")

        po.joinbuy20_stage_closure( )
        elements = po.joinbuy55_productlist_name( )
        num = len(elements)
        i = 0
        while (i + 1) < num:
            trade_id = po.get_id(elements[i])
            sql = "select stage_closure from opening_project WHERE trade_id=" + trade_id
            closure1 = getdata(sql)
            i += 1
            trade_id = po.get_id(elements[i])
            sql = "select stage_closure from opening_project WHERE trade_id=" + trade_id
            closure2 = getdata(sql)
            self.assertTrue(closure1 <= closure2, msg="按交易周期排序无效")

    def test34_joinbuy_commission_sort(self):
        """34 (开放式排序)佣金"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        po.joinbuy21_commission( )
        elements = po.joinbuy55_productlist_name( )
        num = len(elements)
        i = 0
        while (i + 1) < num:
            trade_id = po.get_id(elements[i])
            sql = "select commission from base_project WHERE trade_id=" + trade_id
            commission1 = getdata(sql)
            i += 1
            trade_id = po.get_id(elements[i])
            sql = "select commission from base_project WHERE trade_id=" + trade_id
            commission2 = getdata(sql)
            self.assertTrue(commission1 >= commission2, msg="佣金排序无效")

        po.joinbuy21_commission( )
        elements = po.joinbuy55_productlist_name( )
        num = len(elements)
        i = 0
        while (i + 1) < num:
            trade_id = po.get_id(elements[i])
            sql = "select commission from base_project WHERE trade_id=" + trade_id
            commission1 = getdata(sql)
            i += 1
            trade_id = po.get_id(elements[i])
            sql = "select commission from base_project WHERE trade_id=" + trade_id
            commission2 = getdata(sql)
            self.assertTrue(commission1 <= commission2, msg="佣金排序无效")

    def test35_joinbuy_projetcamount_sort(self):
        """35 (开放式排序)总金额"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        po.joinbuy22_projetcamount( )
        elements = po.joinbuy55_productlist_name( )
        num = len(elements)
        i = 0
        while (i + 1) < num:
            trade_id = po.get_id(elements[i])
            sql1 = "select applied_amount from dynamic_project WHERE trade_id=" + trade_id
            sql2 = "select market_value from opening_project WHERE trade_id=" + trade_id
            applied = getdata(sql1)
            market = getdata(sql2)
            if getdata(sql1) is None:
                applied = 0
            if getdata(sql2) is None:
                market = 0
            projetcamount1 = applied + market
            trade_id = po.get_id(elements[i])
            i += 1
            sql1 = "select applied_amount from dynamic_project WHERE trade_id=" + trade_id
            sql2 = "select market_value from opening_project WHERE trade_id=" + trade_id
            applied = getdata(sql1)
            market = getdata(sql2)
            if getdata(sql1) is None:
                applied = 0
            if getdata(sql2) is None:
                market = 0
            projetcamount2 = applied + market
            self.assertTrue(projetcamount1 >= projetcamount2, msg="总金额排序无效")

        po.joinbuy22_projetcamount( )
        elements = po.joinbuy55_productlist_name( )
        num = len(elements)
        i = 0
        while (i + 1) < num:
            trade_id = po.get_id(elements[i])
            sql1 = "select applied_amount from dynamic_project WHERE trade_id=" + trade_id
            sql2 = "select market_value from opening_project WHERE trade_id=" + trade_id
            applied = getdata(sql1)
            market = getdata(sql2)
            if getdata(sql1) is None:
                applied = 0
            if getdata(sql2) is None:
                market = 0
            projetcamount1 = applied + market
            trade_id = po.get_id(elements[i])
            i += 1
            sql1 = "select applied_amount from dynamic_project WHERE trade_id=" + trade_id
            sql2 = "select market_value from opening_project WHERE trade_id=" + trade_id
            applied = getdata(sql1)
            market = getdata(sql2)
            if getdata(sql1) is None:
                applied = 0
            if getdata(sql2) is None:
                market = 0
            projetcamount2 = applied + market
            self.assertTrue(projetcamount1 <= projetcamount2, msg="总金额排序无效")

    def test36_joinbuy_lead_sort(self):
        """36 (开放式排序)股神出资"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        po.joinbuy23_lead_amount( )
        elements = po.joinbuy55_productlist_name( )
        num = len(elements)
        i = 0
        while (i + 1) < num:
            trade_id = po.get_id(elements[i])
            sql = "select lead_invest_amount from base_project WHERE trade_id=" + trade_id
            lead1 = getdata(sql)
            i += 1
            trade_id = po.get_id(elements[i])
            sql = "select lead_invest_amount from base_project WHERE trade_id=" + trade_id
            lead2 = getdata(sql)
            self.assertTrue(lead1 >= lead2, msg="股神出资排序错误")

        po.joinbuy23_lead_amount( )
        elements = po.joinbuy55_productlist_name( )
        num = len(elements)
        i = 0
        while (i + 1) < num:
            trade_id = po.get_id(elements[i])
            sql = "select lead_invest_amount from base_project WHERE trade_id=" + trade_id
            lead1 = getdata(sql)
            i += 1
            trade_id = po.get_id(elements[i])
            sql = "select lead_invest_amount from base_project WHERE trade_id=" + trade_id
            lead2 = getdata(sql)
            self.assertTrue(lead1 <= lead2, msg="股神出资排序错误")

    def test37_joinbuy_amountnum_sort(self):
        """37 (开放式排序)投资笔数"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        po.joinbuy24_amount_num( )
        elements = po.joinbuy55_productlist_name( )
        num = len(elements)
        i = 0
        while (i + 1) < num:
            trade_id = po.get_id(elements[i])
            sql = "select * from open_invest_apply WHERE state!='discard' and trade_id=" + trade_id
            amountnum1 = getnum(sql)
            i += 1
            trade_id = po.get_id(elements[i])
            sql = "select * from open_invest_apply WHERE state!='discard' and trade_id=" + trade_id
            amountnum2 = getnum(sql)
            self.assertTrue(amountnum1 >= amountnum2, msg="投资笔数排序错误")

        po.joinbuy24_amount_num( )
        elements = po.joinbuy55_productlist_name( )
        num = len(elements)
        i = 0
        while (i + 1) < num:
            trade_id = po.get_id(elements[i])
            sql = "select * from open_invest_apply WHERE state!='discard' and trade_id=" + trade_id
            amountnum1 = getnum(sql)
            i += 1
            trade_id = po.get_id(elements[i])
            sql = "select * from open_invest_apply WHERE state!='discard' and trade_id=" + trade_id
            amountnum2 = getnum(sql)
            self.assertTrue(amountnum1 <= amountnum2, msg="投资笔数排序错误")

    def test38_joinbuy_projectprofit_sort(self):
        """38 (封闭式排序)总收益"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        po.joinbuy02_fbi( )
        po.joinbuy14_profit( )
        po.joinbuy15_projectprofit( )
        elements = po.joinbuy55_productlist_name( )
        num = len(elements)
        i = 0
        while (i + 1) < num:
            trade_id = po.get_id(elements[i])
            sql = "select float_profit_rate from dynamic_project WHERE trade_id=" + trade_id
            projectprofit1 = getdata(sql)
            i += 1
            trade_id = po.get_id(elements[i])
            sql = "select float_profit_rate from dynamic_project WHERE trade_id=" + trade_id
            projectprofit2 = getdata(sql)
            self.assertTrue(projectprofit1 >= projectprofit2, msg="总收益排序错误")

    @unittest.skip("测试数据不支持该用例")
    def test39_joinbuy_d30profit(self):
        """39 (封闭式排序)近30天收益"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        po.joinbuy02_fbi( )
        po.joinbuy14_profit( )
        po.joinbuy16_d30profit( )

    @unittest.skip("测试数据不支持该用例")
    def test40_joinbuy_(self):
        """40 (封闭式排序)近7天收益"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        po.joinbuy02_fbi( )
        po.joinbuy14_profit( )
        po.joinbuy17_d7profit( )

    @unittest.skip("测试数据不支持该用例")
    def test41_joinbuy_(self):
        """41 (封闭式排序)近1天收益"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        po.joinbuy02_fbi( )
        po.joinbuy14_profit( )
        po.joinbuy18_d1profit( )

    def test42_joinbuy_godlevel_sort(self):
        """42 (封闭式排序)股神评级"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        po.joinbuy02_fbi( )
        po.joinbuy19_certify_level( )
        elements = po.joinbuy55_productlist_name( )
        num = len(elements)
        i = 0
        while (i + 1) < num:
            trade_id = po.get_id(elements[i])
            sql = "select user_name from base_project where trade_id=" + trade_id
            user_name = getdata(sql)
            sql = "select user_id from user_base_info where user_name=" + '"' + user_name + '"'
            user_id = str(getdata(sql))
            sql = "select certify_level from god where user_id=" + user_id
            god_level1 = getdata(sql)
            i += 1
            trade_id = po.get_id(elements[i])
            sql = "select user_name from base_project where trade_id=" + trade_id
            user_name = getdata(sql)
            sql = "select user_id from user_base_info where user_name=" + '"' + user_name + '"'
            user_id = str(getdata(sql))
            sql = "select certify_level from god where user_id=" + user_id
            god_level2 = getdata(sql)
            self.assertTrue(god_level1 >= god_level2, msg="按股神评级排序无效")

        po.joinbuy19_certify_level( )
        elements = po.joinbuy55_productlist_name( )
        num = len(elements)
        i = 0
        while (i + 1) < num:
            trade_id = po.get_id(elements[i])
            sql = "select user_name from base_project where trade_id=" + trade_id
            user_name = getdata(sql)
            sql = "select user_id from user_base_info where user_name=" + '"' + user_name + '"'
            user_id = str(getdata(sql))
            sql = "select certify_level from god where user_id=" + user_id
            god_level1 = getdata(sql)
            i += 1
            trade_id = po.get_id(elements[i])
            sql = "select user_name from base_project where trade_id=" + trade_id
            user_name = getdata(sql)
            sql = "select user_id from user_base_info where user_name=" + '"' + user_name + '"'
            user_id = str(getdata(sql))
            sql = "select certify_level from god where user_id=" + user_id
            god_level2 = getdata(sql)
            self.assertTrue(god_level1 <= god_level2, msg="按股神评级排序无效")

    def test43_joinbuy_closure_sort(self):
        """43 (封闭式排序)交易周期"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        po.joinbuy02_fbi( )
        po.joinbuy20_stage_closure( )
        elements = po.joinbuy55_productlist_name( )
        num = len(elements)
        i = 0
        while (i + 1) < num:
            trade_id = po.get_id(elements[i])
            sql = "select period from base_project WHERE trade_id=" + trade_id
            period1 = getdata(sql)
            i += 1
            trade_id = po.get_id(elements[i])
            sql = "select period from base_project WHERE trade_id=" + trade_id
            period2 = getdata(sql)
            self.assertTrue(period1 >= period2, msg="按交易周期排序错误")

        po.joinbuy20_stage_closure( )
        elements = po.joinbuy55_productlist_name( )
        num = len(elements)
        i = 0
        while (i + 1) < num:
            trade_id = po.get_id(elements[i])
            sql = "select period from base_project WHERE trade_id=" + trade_id
            period1 = getdata(sql)
            i += 1
            trade_id = po.get_id(elements[i])
            sql = "select period from base_project WHERE trade_id=" + trade_id
            period2 = getdata(sql)
            self.assertTrue(period1 <= period2, msg="按交易周期排序错误")

    def test44_joinbuy_commission_sort(self):
        """44 (封闭式排序)佣金"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        po.joinbuy02_fbi( )
        po.joinbuy21_commission( )
        elements = po.joinbuy55_productlist_name( )
        num = len(elements)
        i = 0
        while (i + 1) < num:
            trade_id = po.get_id(elements[i])
            sql = "select commission from base_project WHERE trade_id=" + trade_id
            commission1 = getdata(sql)
            i += 1
            trade_id = po.get_id(elements[i])
            sql = "select commission from base_project WHERE trade_id=" + trade_id
            commission2 = getdata(sql)
            self.assertTrue(commission1 >= commission2, msg="按佣金排序错误")

        po.joinbuy21_commission( )
        elements = po.joinbuy55_productlist_name( )
        num = len(elements)
        i = 0
        while (i + 1) < num:
            trade_id = po.get_id(elements[i])
            sql = "select commission from base_project WHERE trade_id=" + trade_id
            commission1 = getdata(sql)
            i += 1
            trade_id = po.get_id(elements[i])
            sql = "select commission from base_project WHERE trade_id=" + trade_id
            commission2 = getdata(sql)
            self.assertTrue(commission1 <= commission2, msg="按佣金排序错误")

    def test45_joinbuy_projetcamount_sort(self):
        """45 (封闭式排序)总金额"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        po.joinbuy02_fbi( )
        po.joinbuy22_projetcamount( )
        elements1 = po.joinbuy55_productlist_name( )
        elements2 = po.find_elements(By.XPATH, "//div[@class='root-listxq']/a")
        num = len(elements1)
        i = 0
        while (i + 1) < num:
            trade_id = po.get_id(elements1[i])
            stage = elements2[i].text
            if stage in "投资中/审核中":
                sql = "select trade_amount from base_project WHERE trade_id=" + trade_id
            else:
                sql = "select loaned_amount from dynamic_project WHERE trade_id=" + trade_id
            projetcamount1 = getdata(sql)
            i += 1
            trade_id = po.get_id(elements1[i])
            stage = elements2[i].text
            if stage in "投资中/审核中":
                sql = "select trade_amount from base_project WHERE trade_id=" + trade_id
            else:
                sql = "select loaned_amount from dynamic_project WHERE trade_id=" + trade_id
            projetcamount2 = getdata(sql)
            self.assertTrue(projetcamount1 >= projetcamount2, msg="总金额排序错误")

        po.joinbuy22_projetcamount( )
        elements1 = po.joinbuy55_productlist_name( )
        elements2 = po.find_elements(By.XPATH, "//div[@class='root-listxq']/a")
        num = len(elements1)
        i = 0
        while (i + 1) < num:
            trade_id = po.get_id(elements1[i])
            stage = elements2[i].text
            if stage in "投资中/审核中":
                sql = "select trade_amount from base_project WHERE trade_id=" + trade_id
            else:
                sql = "select loaned_amount from dynamic_project WHERE trade_id=" + trade_id
            projetcamount1 = getdata(sql)
            i += 1
            trade_id = po.get_id(elements1[i])
            stage = elements2[i].text
            if stage in "投资中/审核中":
                sql = "select trade_amount from base_project WHERE trade_id=" + trade_id
            else:
                sql = "select loaned_amount from dynamic_project WHERE trade_id=" + trade_id
            projetcamount2 = getdata(sql)
            self.assertTrue(projetcamount1 <= projetcamount2, msg="总金额排序错误")

    def test46_joinbuy_lead_sort(self):
        """46 (封闭式排序)股神出资"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        po.joinbuy02_fbi( )
        po.joinbuy23_lead_amount( )
        elements = po.joinbuy55_productlist_name( )
        num = len(elements)
        i = 0
        while (i + 1) < num:
            trade_id = po.get_id(elements[i])
            sql = "select lead_invest_amount from base_project where trade_id=" + trade_id
            lead1 = getdata(sql)
            i += 1
            trade_id = po.get_id(elements[i])
            sql = "select lead_invest_amount from base_project where trade_id=" + trade_id
            lead2 = getdata(sql)
            self.assertTrue(lead1 >= lead2, msg="按股神出资排序错误")

        po.joinbuy23_lead_amount( )
        elements = po.joinbuy55_productlist_name( )
        num = len(elements)
        i = 0
        while (i + 1) < num:
            trade_id = po.get_id(elements[i])
            sql = "select lead_invest_amount from base_project where trade_id=" + trade_id
            lead1 = getdata(sql)
            i += 1
            trade_id = po.get_id(elements[i])
            sql = "select lead_invest_amount from base_project where trade_id=" + trade_id
            lead2 = getdata(sql)
            self.assertTrue(lead1 <= lead2, msg="按股神出资排序错误")

    def test47_joinbuy_amountnum_sort(self):
        """47 (封闭式排序)投资笔数"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        po.joinbuy02_fbi( )
        po.joinbuy24_amount_num( )
        elements = po.joinbuy55_productlist_name( )
        num = len(elements)
        i = 0
        while (i + 1) < num:
            trade_id = po.get_id(elements[i])
            sql = "select * from open_invest_apply WHERE state!='discard' and trade_id=" + trade_id
            amountnum1 = getnum(sql)
            i += 1
            trade_id = po.get_id(elements[i])
            sql = "select * from open_invest_apply WHERE state!='discard' and trade_id=" + trade_id
            amountnum2 = getnum(sql)
            self.assertTrue(amountnum1 >= amountnum2, msg="投资笔数排序错误")

        po.joinbuy24_amount_num( )
        elements = po.joinbuy55_productlist_name( )
        num = len(elements)
        i = 0
        while (i + 1) < num:
            trade_id = po.get_id(elements[i])
            sql = "select * from open_invest_apply WHERE state!='discard' and trade_id=" + trade_id
            amountnum1 = getnum(sql)
            i += 1
            trade_id = po.get_id(elements[i])
            sql = "select * from open_invest_apply WHERE state!='discard' and trade_id=" + trade_id
            amountnum2 = getnum(sql)
            self.assertTrue(amountnum1 <= amountnum2, msg="投资笔数排序错误")

    # 搜索功能(5条)
    def test48_joinbuy_chinese_search(self):
        """48 搜索-中文匹配"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        key_text = "项目"
        po.joinbuy25_ssk(key_text)
        if po.joinbuy26_isnone( ):
            productnames = po.find_elements(By.XPATH, "//div[@class='root-y']/h3/a")
            nicknames = po.find_elements(By.XPATH, "//div[@class='root-xm']/a")
            for (i, j) in zip(productnames, nicknames):
                self.assertTrue(key_text in i.text or key_text in j.text, msg="搜索结果错误")
        else:
            self.assertTrue(1 == 2, msg="无搜索结果")

        key_text = "专属"
        po.joinbuy25_ssk(key_text)
        if po.joinbuy26_isnone( ):
            productnames = po.find_elements(By.XPATH, "//div[@class='root-y']/h3/a")
            nicknames = po.find_elements(By.XPATH, "//div[@class='root-xm']/a")
            for (i, j) in zip(productnames, nicknames):
                self.assertTrue(key_text in i.text or key_text in j.text, msg="搜索结果错误")
        else:
            self.assertTrue(1 == 2, msg="无搜索结果")

    def test49_joinbuy_english_search(self):
        """48 搜索-英文匹配 """
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        key_text = "d"
        po.joinbuy25_ssk(key_text)
        if po.joinbuy26_isnone( ):
            productnames = po.find_elements(By.XPATH, "//div[@class='root-y']/h3/a")
            nicknames = po.find_elements(By.XPATH, "//div[@class='root-xm']/a")
            # 用两个元素组成元组去循环元组列表，zip把两个列表合并成元组列表。
            for (i, j) in zip(productnames, nicknames):
                self.assertTrue(key_text in i.text.lower( ) or key_text in j.text.lower( ), msg="搜索结果错误")
        else:
            self.assertTrue(1 == 2, msg="无搜索结果")

        key_text = "hh"
        po.joinbuy25_ssk(key_text)
        if po.joinbuy26_isnone( ):
            productnames = po.find_elements(By.XPATH, "//div[@class='root-y']/h3/a")
            nicknames = po.find_elements(By.XPATH, "//div[@class='root-xm']/a")
            for (i, j) in zip(productnames, nicknames):
                self.assertTrue(key_text in i.text.lower( ) or key_text in j.text.lower( ), msg="搜索结果错误")
        else:
            self.assertTrue(1 == 2, msg="无搜索结果")

    def test50_joinbuy_number_search(self):
        """48 搜索-数字匹配"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        key_text = "2017"
        po.joinbuy25_ssk(key_text)
        if po.joinbuy26_isnone( ):
            productnames = po.find_elements(By.XPATH, "//div[@class='root-y']/h3/a")
            nicknames = po.find_elements(By.XPATH, "//div[@class='root-xm']/a")
            for (i, j) in zip(productnames, nicknames):
                self.assertTrue(key_text in i.text or key_text in j.text, msg="搜索结果错误")
        else:
            self.assertTrue(1 == 2, msg="无搜索结果")

    def test51_joinbuy_symbol_search(self):
        """48 搜索-符号匹配"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        key_text = "-"
        po.joinbuy25_ssk(key_text)
        if po.joinbuy26_isnone( ):
            productnames = po.find_elements(By.XPATH, "//div[@class='root-y']/h3/a")
            nicknames = po.find_elements(By.XPATH, "//div[@class='root-xm']/a")
            for (i, j) in zip(productnames, nicknames):
                self.assertTrue(key_text in i.text or key_text in j.text, msg="搜索结果错误")
        else:
            self.assertTrue(1 == 2, msg="无搜索结果")

    def test52_joinbuy_mixture_search(self):
        """48 搜索-混合匹配"""
        po = JoinBuy(self.driver)
        po.open( )
        sleep(2)
        key_text = "测试2017"
        po.joinbuy25_ssk(key_text)
        if po.joinbuy26_isnone( ):
            productnames = po.find_elements(By.XPATH, "//div[@class='root-y']/h3/a")
            nicknames = po.find_elements(By.XPATH, "//div[@class='root-xm']/a")
            for (i, j) in zip(productnames, nicknames):
                self.assertTrue(key_text in i.text.lower( ) or key_text in j.text.lower( ), msg="搜索结果错误")
        else:
            self.assertTrue(1 == 2, msg="无搜索结果")


# if __name__ == "__main__":
#     runner = unittest.TextTestRunner( )
#     suite = unittest.TestSuite( )
    # suite.addTest(JoinBuyTest("test01_joinbuy_kf"))
    # suite.addTest(JoinBuyTest("test02_joinbuy_fbi"))
    # suite.addTest(JoinBuyTest("test03_joinbuy_nickname"))
    # suite.addTest(JoinBuyTest("test04_joinbuy_opentype"))
    # suite.addTest(JoinBuyTest("test05_joinbuy_openamount"))
    # suite.addTest(JoinBuyTest("test06_joinbuy_quantity"))
    # suite.addTest(JoinBuyTest("test07_joinbuy_lead"))
    # suite.addTest(JoinBuyTest("test08_joinbuy_losure"))
    # suite.addTest(JoinBuyTest("test09_joinbuy_commission"))
    # suite.addTest(JoinBuyTest("test10_joinbuy_profit"))
    # suite.addTest(JoinBuyTest("test11_joinbuy_phase1"))
    # suite.addTest(JoinBuyTest("test12_joinbuy_type"))
    # suite.addTest(JoinBuyTest("test13_joinbuy_nickname"))
    # suite.addTest(JoinBuyTest("test14_joinbuy_amount"))
    # suite.addTest(JoinBuyTest("test15_joinbuy_losure"))
    # suite.addTest(JoinBuyTest("test16_joinbuy_commisson"))
    # suite.addTest(JoinBuyTest("test17_joinbuy_stop"))
    # suite.addTest(JoinBuyTest("test18_joinbuy_residue"))
    # suite.addTest(JoinBuyTest("test19_joinbuy_phase2"))
    # suite.addTest(JoinBuyTest("test20_joinbuy_float"))
    # suite.addTest(JoinBuyTest("test21_joinbuy_phase3"))
    # suite.addTest(JoinBuyTest("test22_joinbuy_profit"))
    # suite.addTest(JoinBuyTest("test23_joinbuy_type"))
    # suite.addTest(JoinBuyTest("test24_joinbuy_type"))
    # suite.addTest(JoinBuyTest("test25_joinbuy_guarantee"))
    # suite.addTest(JoinBuyTest("test26_joinbuy_shares"))
    # suite.addTest(JoinBuyTest("test27_joinbuy_futures"))
    # suite.addTest(JoinBuyTest("test28_joinbuy_profit_sort"))
    # suite.addTest(JoinBuyTest("test32_joinbuy_godlevel_sort"))
    # suite.addTest(JoinBuyTest("test33_joinbuy_closure_sort"))
    # suite.addTest(JoinBuyTest("test34_joinbuy_commission_sort"))
    # suite.addTest(JoinBuyTest("test35_joinbuy_projetcamount_sort"))
    # suite.addTest(JoinBuyTest("test36_joinbuy_lead_sort"))
    # suite.addTest(JoinBuyTest("test37_joinbuy_amountnum_sort"))
    # suite.addTest(JoinBuyTest("test38_joinbuy_projectprofit_sort"))
    # suite.addTest(JoinBuyTest("test42_joinbuy_godlevel_sort"))
    # suite.addTest(JoinBuyTest("test43_joinbuy_closure_sort"))
    # suite.addTest(JoinBuyTest("test44_joinbuy_commission_sort"))
    # suite.addTest(JoinBuyTest("test45_joinbuy_projetcamount_sort"))
    # suite.addTest(JoinBuyTest("test46_joinbuy_lead_sort"))
    # suite.addTest(JoinBuyTest("test47_joinbuy_amountnum_sort"))
    # suite.addTest(JoinBuyTest("test48_joinbuy_chinese_search"))
    # suite.addTest(JoinBuyTest("test49_joinbuy_english_search"))
    # suite.addTest(JoinBuyTest("test50_joinbuy_number_search"))
    # suite.addTest(JoinBuyTest("test51_joinbuy_symbol_search"))
    # suite.addTest(JoinBuyTest("test52_joinbuy_mixture_search"))

    # runner.run(suite)
