#__author__ = 'gz'
#-*- coding: utf-8 -*-
from appium import webdriver
import time
import unittest
import random
from appium.webdriver.common.touch_action import TouchAction
from HTMLTestRunner import HTMLTestRunner
from extend import Appium_Extend
from Element_Click_Check import ElementCheck

class New_pictureTest(unittest.TestCase):

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

    def Picture1(self):
        """新图浏览框隐藏"""
        #点击发现
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/home_pic')
        self.ElementCheck.check_assertTrue(result,msg='发现按钮Fail')
        #点击新图
        self.d.find_element_by_id('com.bugua.fight:id/new_pic_tv').click()
        #随机滑屏
        self.ElementCheck.random_click('id','com.bugua.fight:id/jgznewpic_content')
        #单击后内容检查
        result = self.ElementCheck.existence('id','com.bugua.fight:id/btn_send')
        self.ElementCheck.check_assertTrue(result,msg='直接发送按钮Fail')
        result = self.ElementCheck.existence('id','com.bugua.fight:id/btn_save')
        self.ElementCheck.check_assertTrue(result,msg='添加收藏按钮Fail')
        result = self.ElementCheck.existence('id','com.bugua.fight:id/btn_hide_preview')
        self.ElementCheck.check_assertTrue(result,msg='隐藏按钮Fail')
        #点击隐藏按钮
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/btn_hide_preview','hide')
        self.ElementCheck.check_assertTrue(result,msg='隐藏按钮失败')
        #滑动后隐藏
        self.ElementCheck.random_click('id','com.bugua.fight:id/jgznewpic_content')
        result = self.ElementCheck.swipe_existence('id','com.bugua.fight:id/btn_hide_preview')
        self.ElementCheck.check_assertTrue(result, msg='隐藏失败')
        #点击收藏
        self.ElementCheck.random_click('id','com.bugua.fight:id/jgznewpic_content')
        result = self.ElementCheck.click_change('id', 'com.bugua.fight:id/btn_save')
        self.ElementCheck.check_assertTrue(result, msg='收藏按钮未变化')

    def Picture2(self):
        """新图浏览框收藏"""
        #点击发现
        self.d.find_element_by_id('com.bugua.fight:id/home_pic').click()
        #点击新图
        self.d.find_element_by_id('com.bugua.fight:id/new_pic_tv').click()
        #随机滑屏
        self.ElementCheck.random_click('id', 'com.bugua.fight:id/jgznewpic_content', 'long_press')
        #单击后内容检查
        result = self.ElementCheck.existence('id','com.bugua.fight:id/btn_send')
        self.ElementCheck.check_assertTrue(result,msg='直接发送按钮Fail')
        result = self.ElementCheck.existence('id','com.bugua.fight:id/btn_star')
        self.ElementCheck.check_assertTrue(result,msg='添加收藏按钮Fail')
        result = self.ElementCheck.existence('id','com.bugua.fight:id/btn_download')
        self.ElementCheck.check_assertTrue(result,msg='保存到本地按钮Fail')
        result = self.ElementCheck.existence('id','com.bugua.fight:id/btn_edit')
        self.ElementCheck.check_assertTrue(result,msg='改图按钮Fail')
        #点击收藏
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/icon_star')
        self.ElementCheck.check_assertTrue(result,msg='收藏按钮未变化')

    def Top(self):
        """新图置顶按钮"""
        #点击发现
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/home_pic')
        self.ElementCheck.check_assertTrue(result,msg='发现按钮Fail')
        #点击新图
        self.d.find_element_by_id('com.bugua.fight:id/new_pic_tv').click()
        #随机滑屏
        a = random.choice(range(1, 4))
        print(a)
        size = self.d.get_window_size()
        width = size['width']
        height = size['height']
        print(width, height)
        i = 0
        for i in range(a):
            self.d.swipe(width*280/1080, height*1600/1776, width*280/1080, height*432/1776)
            i = i+1
        time.sleep(2)
        self.d.swipe(width*280/1080, height*500/1776, width*280/1080, height*900/1776)
        time.sleep(1)
        self.ElementCheck.click('id','com.bugua.fight:id/to_top')
        time.sleep(2)
        result=self.ElementCheck.existence('name','大家正在发')
        self.assertTrue(result, msg='没有回到顶部')

if __name__=="__main__":
    #编辑用例
    suite = unittest.TestSuite()
    # suite.addTest(New_pictureTest('Picture1'))
    # suite.addTest(New_pictureTest('Picture2'))
    suite.addTest(New_pictureTest('Top'))
    #执行用例
    runner = unittest.TextTestRunner()
    runner.run(suite)




