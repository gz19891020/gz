#__author__ = 'gz'
#-*- coding: utf-8 -*-
from appium import webdriver
import time
import unittest
import random
from appium.webdriver.common.touch_action import TouchAction
from HTMLTestRunner import HTMLTestRunner
import  os
from Element_Click_Check import ElementCheck

class SerchTest(unittest.TestCase):

    def setUp(self):
        print('Test start')
        #读取设备名字
        try:
            txt = open('./devices', 'r')
            device = txt.read()
            txt.close()
        except:
            device = 'Android Emulator'
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.2'
        desired_caps['deviceName'] = '%s' % device
        desired_caps['appPackage'] = 'com.bugua.fight'
        desired_caps['appActivity'] = 'com.yuelian.qqemotion.splash.SplashActivity'
        desired_caps['resetKeyboard']='True'
        desired_caps['unicodeKeyboard']='True'

        self.d = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.ElementCheck = ElementCheck(self,self.d)
        time.sleep(5)


    def tearDown(self):
        print('Test end')
        self.d.quit()

    def serch_post(self):
        #点击搜索框
        self.ElementCheck.click_jump('id','com.bugua.fight:id/search_tv','id','com.bugua.fight:id/et_search')
        #搜索金馆长
        self.d.find_element_by_id('com.bugua.fight:id/et_search').send_keys('金馆长')
        #点击搜索
        self.d.find_element_by_id('com.bugua.fight:id/search_key').click()

