#__author__ = 'gz'
#-*- coding: utf-8 -*-
from appium import webdriver
import time
import unittest
import random
from appium.webdriver.common.touch_action import TouchAction
from HTMLTestRunner import HTMLTestRunner
import  os
from re_Element_Click_Check import ElementCheck
from extend import Appium_Extend

class Suspension_Test(unittest.TestCase):


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
        self.ElementCheck = ElementCheck(self,self.d)
        self.Exent = Appium_Extend(self.d)
        time.sleep(5)

    def tearDown(self):
        print('Test end')
        self.d.quit()

    def weixin_suspension_test(self):
        """微信悬浮窗"""
        #点击我的页面
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/my_pic')
        self.ElementCheck.check_assertTrue(result,'进入我的页面失败')
        #点击设置
        self.d.find_element_by_id('com.bugua.fight:id/btn_info').click()
        #确认表情悬浮窗状态
        float = self.d.find_element_by_id('com.bugua.fight:id/show_float_window').get_attribute('name')
        if float == '未开启':
            result = self.ElementCheck.click_jump('id','com.bugua.fight:id/float_window','name','斗图悬浮球')
            self.ElementCheck.check_assertTrue(result,'进入表情悬浮窗失败')
            #点击悬浮窗开关
            result = self.ElementCheck.click_change('id','com.bugua.fight:id/float_window_switch')
            self.ElementCheck.check_assertTrue(result,'点击悬浮窗开关失败')
            self.d.back()
            result = self.d.find_element_by_id('com.bugua.fight:id/show_float_window').get_attribute('name')
            self.assertEqual(result,'已开启','悬浮窗开启失败')
        else:
            result = self.ElementCheck.click_jump('id','com.bugua.fight:id/float_window','name','斗图悬浮球')
            self.ElementCheck.check_assertTrue(result,'进入表情悬浮窗失败')
            #点击悬浮窗开关
            result = self.ElementCheck.click_change('id','com.bugua.fight:id/float_window_switch')
            self.ElementCheck.check_assertTrue(result,'点击悬浮窗开关失败')
            #再次点击悬浮窗开关
            time.sleep(1)
            result = self.ElementCheck.click_change('id','com.bugua.fight:id/float_window_switch')
            self.ElementCheck.check_assertTrue(result,'点击悬浮窗开关失败')
            self.d.back()
            result = self.d.find_element_by_id('com.bugua.fight:id/show_float_window').get_attribute('name')
            self.assertEqual(result,'已开启','悬浮窗开启失败')
        #打开微信
        self.d.start_activity('com.tencent.mm','com.tencent.mm.ui.LauncherUI')
        size = self.d.get_window_size()
        wid = size['width']
        hig = size['height']
        time.sleep(5)
        #截屏
        #self.Exent.get_screenshot_by_element(self.d.find_element_by_id('com.tencent.mm:id/bd5')).write_to_file('./Temp','SuspensionPicture')
        # TouchAction(self.d).tap(x=940, y=1360).perform()
        #点击悬浮窗
        self.d.tap([(940, 1360)],)#这里的坐标应该算出来这个是临时的
        #设置输入法为搜狗输入法
        os.system('adb shell ime set com.sohu.inputmethod.sogouoem/.SogouIME')
        #点击一键生成输入框
        self.d.find_element_by_id('com.bugua.fight:id/input_et').click()
        self.d.find_element_by_id('com.bugua.fight:id/input_et_small').send_keys('let us ZB')
        time.sleep(2)
        self.d.find_element_by_id('com.bugua.fight:id/input_sure_small').click()
        try:
            os._exists(r'./Temp') == False
            os.mkdir(r'./Temp')
        except:
            pass
        #第一页随机选择图片
        time.sleep(5)
        self.d.find_element_by_id('com.bugua.fight:id/item_container_%d' % random.choice(range(0,7))).click()
        time.sleep(5)
        #发送给管昭
        self.d.find_element_by_name('管昭').click()
        time.sleep(2)
        self.d.find_element_by_name('分享').click()
        time.sleep(1)
        self.ElementCheck.click_change('id','com.tencent.mm:id/a7m','hide')
        #检查是否返回到发送页面（这里不能够模糊对比，两张图片会因为发图以后的时间变化不一致）
        # self.Exent.get_screenshot_by_element(self.d.find_element_by_id('com.tencent.mm:id/bd5')).write_to_file('./Temp','SuspensionPicture1')
        # result = self.ElementCheck.cintrast_element_picture('id','com.tencent.mm:id/bd5','./Temp/SuspensionPicture.png')
        # self.ElementCheck.check_assertTrue(result,'没有返回发送图片时页面')
        time.sleep(2)
        #点击悬浮窗
        self.d.tap([(940, 1360)],)#这里的坐标应该算出来这个是临时的
        #点击清除按钮
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/make_pic_reset','hide')
        self.ElementCheck.check_assertTrue(result,'点击清除按钮失败')
        try:
            self.d.find_element_by_name('输入一句话随机生成多张配图')
        except:
            assert 1+1== 3,'点击清除按钮失败'

    def qq_suspension_test(self):
        """QQ悬浮窗"""
        #点击我的页面
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/my_pic')
        self.ElementCheck.check_assertTrue(result,'进入我的页面失败')
        #点击设置
        self.d.find_element_by_id('com.bugua.fight:id/btn_info').click()
        #确认表情悬浮窗状态
        float = self.d.find_element_by_id('com.bugua.fight:id/show_float_window').get_attribute('name')
        if float == '未开启':
            result = self.ElementCheck.click_jump('id','com.bugua.fight:id/float_window','name','斗图悬浮球')
            self.ElementCheck.check_assertTrue(result,'进入表情悬浮窗失败')
            #点击悬浮窗开关
            result = self.ElementCheck.click_change('id','com.bugua.fight:id/float_window_switch')
            self.ElementCheck.check_assertTrue(result,'点击悬浮窗开关失败')
            self.d.back()
            result = self.d.find_element_by_id('com.bugua.fight:id/show_float_window').get_attribute('name')
            self.assertEqual(result,'已开启','悬浮窗开启失败')
        else:
            result = self.ElementCheck.click_jump('id','com.bugua.fight:id/float_window','name','斗图悬浮球')
            self.ElementCheck.check_assertTrue(result,'进入表情悬浮窗失败')
            #点击悬浮窗开关
            result = self.ElementCheck.click_change('id','com.bugua.fight:id/float_window_switch')
            self.ElementCheck.check_assertTrue(result,'点击悬浮窗开关失败')
            #再次点击悬浮窗开关
            time.sleep(1)
            result = self.ElementCheck.click_change('id','com.bugua.fight:id/float_window_switch')
            self.ElementCheck.check_assertTrue(result,'点击悬浮窗开关失败')
            self.d.back()
            result = self.d.find_element_by_id('com.bugua.fight:id/show_float_window').get_attribute('name')
            self.assertEqual(result,'已开启','悬浮窗开启失败')
        #打开QQ
        self.d.start_activity('com.tencent.mobileqq','com.tencent.mobileqq.activity.SplashActivity')
        size = self.d.get_window_size()
        wid = size['width']
        hig = size['height']
        time.sleep(5)
        #截屏
        #self.Exent.get_screenshot_by_element(self.d.find_element_by_id('com.tencent.mm:id/bd5')).write_to_file('./Temp','SuspensionPicture')
        # TouchAction(self.d).tap(x=940, y=1360).perform()
        self.d.tap([(940, 1360)],)#这里的坐标应该算出来这个是临时的
        #设置输入法为搜狗输入法
        os.system('adb shell ime set com.sohu.inputmethod.sogouoem/.SogouIME')
        #点击一键生成输入框
        self.d.find_element_by_id('com.bugua.fight:id/input_et').click()
        self.d.find_element_by_id('com.bugua.fight:id/input_et_small').send_keys('let us ZB')
        time.sleep(2)
        self.d.find_element_by_id('com.bugua.fight:id/input_sure_small').click()
        try:
            os._exists(r'./Temp') == False
            os.mkdir(r'./Temp')
        except:
            pass
        #第2页随机选择图片
        time.sleep(5)
        self.d.swipe(wid*800/1080,hig*1400/1920,wid*200/1080,hig*1400/1920)
        self.d.find_element_by_id('com.bugua.fight:id/item_container_%d' % random.choice(range(0,7))).click()
        #QQ分享
        #self.d.find_element_by_id('com.bugua.fight:id/share_to_qq').click()
        time.sleep(5)
        self.d.find_element_by_name('狗中极品').click()
        #点击发送
        time.sleep(2)
        self.d.find_element_by_id('com.tencent.mobileqq:id/dialogRightBtn').click()
        #检查是否返回到发送页面（这里不能够模糊对比，两张图片会因为发图以后的时间变化不一致）
        # self.Exent.get_screenshot_by_element(self.d.find_element_by_id('com.tencent.mm:id/bd5')).write_to_file('./Temp','SuspensionPicture1')
        # result = self.ElementCheck.cintrast_element_picture('id','com.tencent.mm:id/bd5','./Temp/SuspensionPicture.png')
        # self.ElementCheck.check_assertTrue(result,'没有返回发送图片时页面')
        time.sleep(2)
        #点击悬浮窗
        self.d.tap([(940, 1360)],)#这里的坐标应该算出来这个是临时的
        #点击清除按钮
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/make_pic_reset','hide')
        self.ElementCheck.check_assertTrue(result,'点击清除按钮失败')
        try:
            self.d.find_element_by_name('输入一句话随机生成多张配图')
        except:
            assert 1+1== 3,'点击清除按钮失败'

if __name__=="__main__":
    #编辑用例
    suite = unittest.TestSuite()
    # suite.addTest(Suspension_Test('weixin_suspension_test'))
    # suite.addTest(Suspension_Test('qq_suspension_test'))
    #执行用例
    runner = unittest.TextTestRunner()
    runner.run(suite)