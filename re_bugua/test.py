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
desired_caps['appPackage'] = 'com.tuan800.tao800'
desired_caps['appActivity'] = 'com.tuan800.tao800.share.activities.SplashActivity'
desired_caps['resetKeyboard']='True'
desired_caps['unicodeKeyboard']='True'

d = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

time.sleep(10)

d.swipe(500,1000,500,250)
a = d.find_elements_by_class_name("android.widget.ImageView")
a[14].click()
time.sleep(5)

print(d.contexts)
d.switch_to.context('webview')
d.swipe(500,1000,500,300)
d.find_element_by_xpath("//android.widget.Image[@content-desc='【抽奖团】香雪海 BC-50B 家用单门迷你小冰箱'").click()