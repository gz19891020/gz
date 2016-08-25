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

class ThemeTest(unittest.TestCase):

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

    def Follow_Theme_Test1(self):
        #点击主题
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/theme_tv')
        self.ElementCheck.check_assertTrue(result,msg='进入主题失败')
        #点击发现更多主题
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/more_normal_theme','name','关注列表')
        self.ElementCheck.check_assertTrue(result, msg='未进入关注列表')
        #选择关注一个主题
        time.sleep(2)
        theme =self.ElementCheck.random_click_get_name('id','com.bugua.fight:id/theme_title')
        result = self.ElementCheck.click_jump('name','关注','name','已关注')
        self.ElementCheck.check_assertTrue(result, msg='关注按钮未改变')
        #返回首页主题
        self.d.back()
        self.d.back()
        time.sleep(4)
        result = self.ElementCheck.existence('name',theme)
        self.ElementCheck.check_assertTrue(result, msg='关注主题未成功')
        #取消关注了的主题
        self.d.find_element_by_name(theme).click()
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/is_follow')
        self.ElementCheck.check_assertTrue(result, msg='已关注按钮未改变')
        #检查是否已取消关注
        self.d.back()
        result = self.ElementCheck.existence('name',theme)
        self.ElementCheck.check_assertFalse(result, msg='关注主题未成功')

    def Follow_Theme_Test2(self):
        #点击主题
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/theme_tv')
        self.ElementCheck.check_assertTrue(result,msg='进入主题失败')
        #点击发现更多主题
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/more_normal_theme','name','关注列表')
        self.ElementCheck.check_assertTrue(result, msg='未进入关注列表')
        #选择关注一个主题
        theme = self.ElementCheck.random_click_get_other_name('id','com.bugua.fight:id/theme_support','id','com.bugua.fight:id/theme_title')
        result = self.ElementCheck.existence('name','已关注')
        self.ElementCheck.check_assertTrue(result, msg='关注按钮未改变')
        #返回首页主题
        self.d.back()
        time.sleep(4)
        result = self.ElementCheck.existence('name',theme)
        self.ElementCheck.check_assertTrue(result, msg='关注主题未成功')
        #取消关注了的主题
        self.d.find_element_by_name(theme).click()
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/is_follow')
        self.ElementCheck.check_assertTrue(result, msg='已关注按钮未改变')
        #检查是否已取消关注
        self.d.back()
        time.sleep(1)
        result = self.ElementCheck.existence('name',theme)
        self.ElementCheck.check_assertFalse(result, msg='关注主题未成功')
    def Theme_picture1(self):
        #点击主题
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/theme_tv')
        self.ElementCheck.check_assertTrue(result,msg='进入主题失败')
        #点击发现更多主题
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/more_normal_theme','name','关注列表')
        self.ElementCheck.check_assertTrue(result, msg='未进入关注列表')
        #选择一个主题
        self.ElementCheck.random_click('id','com.bugua.fight:id/click_area')
        #点击图片墙
        self.d.find_element_by_name('图片墙').click()
        #点击图片
        self.ElementCheck.random_click('id','com.bugua.fight:id/jgznewpic_content')
        #单击后内容检查
        result = self.ElementCheck.existence('id','com.bugua.fight:id/btn_send')
        self.ElementCheck.check_assertTrue(result, msg='直接发送按钮Fail')
        result = self.ElementCheck.existence('id','com.bugua.fight:id/btn_save')
        self.ElementCheck.check_assertTrue(result, msg='添加收藏按钮Fail')
        result = self.ElementCheck.existence('id','com.bugua.fight:id/btn_hide_preview')
        self.ElementCheck.check_assertTrue(result,  msg='隐藏按钮Fail')
        #点击收藏
        self.d.find_element_by_id('com.bugua.fight:id/btn_save').click()
        test = self.d.find_elements_by_name('添加收藏')
        self.assertEqual(len(test), 0, msg='收藏按钮未变化')

    def Theme_picture2(self):
        #点击主题
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/theme_tv')
        self.ElementCheck.check_assertTrue(result,msg='进入主题失败')
        #点击发现更多主题
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/more_normal_theme','name','关注列表')
        self.ElementCheck.check_assertTrue(result, msg='未进入关注列表')
        #选择一个主题
        self.ElementCheck.random_click('id','com.bugua.fight:id/click_area')
        #点击图片墙
        self.d.find_element_by_name('图片墙').click()
        time.sleep(5)
        #长按图片
        self.ElementCheck.random_click('id','com.bugua.fight:id/jgznewpic_content','long_press')
        #点击收藏
        self.d.find_element_by_id('com.bugua.fight:id/icon_star').click()
        test = self.d.find_elements_by_name('添加收藏')
        self.assertEqual(len(test), 0, msg='收藏按钮未变化')

    def Theme_picture3(self):
        #点击主题
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/theme_tv')
        self.ElementCheck.check_assertTrue(result,msg='进入主题失败')
        #点击发现更多主题
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/more_normal_theme','name','关注列表')
        self.ElementCheck.check_assertTrue(result, msg='未进入关注列表')
        #选择一个主题
        self.ElementCheck.random_click('id','com.bugua.fight:id/click_area')
        #点击图片墙
        self.d.find_element_by_name('图片墙').click()
        #点击图片
        self.ElementCheck.random_click('id','com.bugua.fight:id/jgznewpic_content')
        #点击隐藏按钮
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/btn_hide_preview')
        self.ElementCheck.check_assertTrue(result,msg='点击隐藏按钮失败')
        #滑动后隐藏
        self.ElementCheck.random_click('id','com.bugua.fight:id/jgznewpic_content')
        result = self.ElementCheck.swipe_existence('id','com.bugua.fight:id/btn_hide_preview')
        self.ElementCheck.check_assertTrue(result, msg='隐藏失败')
        #点击收藏
        self.ElementCheck.random_click('id','com.bugua.fight:id/jgznewpic_content')
        result = self.ElementCheck.click_change('id', 'com.bugua.fight:id/btn_save')
        self.ElementCheck.check_assertTrue(result, msg='收藏按钮未变化')


if __name__=="__main__":
    #编辑用例
    suite = unittest.TestSuite()
    # suite.addTest(ThemeTest('Follow_Theme_Test1'))
    # suite.addTest(ThemeTest('Follow_Theme_Test2')
    suite.addTest(ThemeTest('Theme_picture1'))
    #suite.addTest(ThemeTest('Theme_picture2'))
    #suite.addTest(ThemeTest('Theme_picture3'))
    #执行用例
    runner = unittest.TextTestRunner()
    runner.run(suite)
