#__author__ = 'gz'
#-*- coding: utf-8 -*-

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
import unittest
import random
from extend import Appium_Extend
from HTMLTestRunner import HTMLTestRunner
from Element_Click_Check import ElementCheck

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = 'bb15c680'
desired_caps['appPackage'] = 'com.bugua.fight'
desired_caps['appActivity'] = 'com.yuelian.qqemotion.splash.SplashActivity'
desired_caps['resetKeyboard']='True'
desired_caps['unicodeKeyboard']='True'

d = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

time.sleep(5)

# d.find_element_by_id('com.bugua.fight:id/search_tv').click()
# time.sleep(1)
# d.find_element_by_id('com.bugua.fight:id/et_search').send_keys('psvr')
# time.sleep(5)
# d.find_element_by_id('com.bugua.fight:id/search_key').click()
# time.sleep(2)
# d.find_element_by_id('com.bugua.fight:id/bbs_title').click()
# time.sleep(5)
# for i in range(90):
#     d.find_element_by_id('com.bugua.fight:id/content_et').send_keys('斗图斗图')
#     time.sleep(1)
#     d.find_element_by_id('com.bugua.fight:id/submit_tv').click()
#     time.sleep(10)
# d.switch_to().frame()

d.find_element_by_id('com.bugua.fight:id/ask_for_ps_tv').click()
time.sleep(1)
d.find_element_by_xpath('//android.support.v7.widget.RecyclerView/android.widget.LinearLayout/android.widget.ImageView').click()
time.sleep(5)
print(d.contexts)
a=d.find_elements_by_class_name('android.view.View')
a[1].click()
# d.switch_to.frame()
d.refresh()