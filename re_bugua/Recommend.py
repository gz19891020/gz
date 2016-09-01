#__author__ = 'gz'
#-*- coding: utf-8 -*-
from appium import webdriver
import time
import unittest
import random
from appium.webdriver.common.touch_action import TouchAction
from HTMLTestRunner import HTMLTestRunner
from extend import Appium_Extend
from re_Element_Click_Check import ElementCheck

class RecommendTest(unittest.TestCase):

    def setUp(self):
        print('Test start')
        #读取设备名字
        try:
            txt = open('./devices', 'r')
            phone=[]
            for i in txt:
                phone.append(i)
            system1 = phone[0]
            device = phone[1]
            txt.close()
        except:
            system1 = '4.4.4'
            device = 'Android Emulator'
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '%s' % system1
        desired_caps['deviceName'] = '%s' % device
        desired_caps['appPackage'] = 'com.bugua.fight'
        desired_caps['appActivity'] = 'com.yuelian.qqemotion.splash.SplashActivity'
        desired_caps['resetKeyboard']='True'
        desired_caps['unicodeKeyboard']='True'

        self.d = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.extend = Appium_Extend(self.d)
        self.ElementCheck = ElementCheck(self, self.d)

        time.sleep(5)

    def tearDown(self):
        print('Test end')
        self.d.quit()

    def User_test1(self):
        """关注推荐用户"""
        #点击发现
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/home_pic')
        self.ElementCheck.check_assertTrue(result,msg='发现按钮Fail')
        #点击关注
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/focus_tv')
        self.ElementCheck.check_assertTrue(result,msg='关注集合页面Fail')
        #点击用户推荐
        result = self.ElementCheck.click_change('name','用户推荐')
        self.ElementCheck.check_assertTrue(result,msg='用户推荐页面Fail')
        #获取第一个腿甲用户的名字
        user_name = self.ElementCheck.attribute_name('xpath', '//android.support.v7.widget.RecyclerView/\
                                                 android.widget.LinearLayout[2]/\
                                                 android.widget.LinearLayout[1]/\
                                                 android.widget.LinearLayout[1]/\
                                                 android.widget.TextView[1]')
        self.ElementCheck.click_change('ides','com.bugua.fight:id/followBtn[0]')
        #检查关注
        self.d.back()
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/my_pic')
        self.ElementCheck.check_assertTrue(result,msg='进入我的页面失败')
        result = self.ElementCheck.click_jump('name','关注')
        self.ElementCheck.check_assertTrue(result,msg='进入关注页面失败')
        result = self.ElementCheck.existence('name', user_name)
        self.ElementCheck.check_assertTrue(result,msg='未发现关注的推荐用户')
        result = self.ElementCheck.click_jump('name','已关注','name','关注')
        self.ElementCheck.check_assertTrue(result,msg='已关注按钮失败')
        self.d.back()
        time.sleep(2)
        self.d.find_element_by_name('关注').click()
        result = self.ElementCheck.existence('name', user_name)
        self.assertFalse(result, msg='发现关注的推荐用户')
if __name__=="__main__":
    #编辑用例
    suite = unittest.TestSuite()
    suite.addTest(RecommendTest('User_test1'))
    #执行用例
    runner = unittest.TextTestRunner()
    runner.run(suite)
    #执行用例并生成报告
    #filename = 'C:/\Users/\yuelian/\Desktop/\Automated Testing/\Report/\Recommend.html'
    #fp = open(filename, 'wb')
    #runner = HTMLTestRunner(stream = fp , title='自动化测试报告' , description='自动化测试报告')
    #runner.run(suite)

