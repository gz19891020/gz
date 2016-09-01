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

class Follow_Test(unittest.TestCase):

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

    def Follow_user1(self):
        """从帖子中关注一个用户"""
        #点击大杂烩
        self.d.find_element_by_id('com.bugua.fight:id/all_area').click()
        # #向下拉屏幕隐藏帖子以外内容
        # size=self.d.get_window_size()
        # width=size['width']
        # height=size['height']
        # print(width,height)
        # self.d.swipe(width*200/1080, height*1500/1776, width*200/1080, height*720/1776)
        #翻页
        user_name = '丑到爆的同桌'
        while user_name == '丑到爆的同桌':
            self.ElementCheck.random_click('id','com.bugua.fight:id/bbs_title')
            #在帖子中寻找用户头像
            self.ElementCheck.random_click('id','com.bugua.fight:id/avatar')
            #获取名字
            user_name = self.d.find_elements_by_class_name('android.widget.TextView')
            user_name =user_name[1].get_attribute('name')
            print(user_name)
            if user_name == '丑到爆的同桌':
                continue
            #点击添加关注
            time.sleep(2)
            self.d.find_element_by_id('com.bugua.fight:id/btn_follow').click()
            time.sleep(5)
            user_data = self.d.find_element_by_xpath('//android.support.v7.widget.RecyclerView/'
                                                     'android.widget.LinearLayout/android.widget.LinearLayout[1]')
            self.extend.get_screenshot_by_element(user_data).write_to_file('.\Temp','user_data')
            #进入我的关注页面
            self.d.back()
            self.d.back()
            self.d.find_element_by_id('com.bugua.fight:id/my_pic').click()
            self.d.find_element_by_name('关注').click()
            a1 = self.d.find_elements_by_name(user_name)
            self.d.find_element_by_name(user_name).click()
            self.assertEqual(len(a1) ,1,msg='没有发现所关注的用户')
            #对比用户的个人资料,只对比了资料的部分（头像，用户名，签名）
            load = self.extend.load_image('.\Temp/user_data.png')
            user_data = self.d.find_element_by_xpath('//android.support.v7.widget.RecyclerView/'
                                                     'android.widget.LinearLayout/android.widget.LinearLayout[1]')
            self.extend.get_screenshot_by_element(user_data).write_to_file('.\Temp','user_data2')
            result = self.extend.get_screenshot_by_element(self.d.find_element_by_xpath('//android.support.v7.widget.RecyclerView/android.widget.LinearLayout/android.widget.LinearLayout[1]')).same_as(load, 0)
            self.ElementCheck.check_assertTrue(result, msg='用户资料显示有误')
            #取消关注
            self.d.back()
            self.d.find_element_by_id('com.bugua.fight:id/button').click()
            button1 = self.d.find_elements_by_name('关注')
            self.assertEqual(len(button1), 1, msg='取消关注Fail')
            #关注列表检查
            self.d.back()
            self.d.find_element_by_name('关注').click()
            button2 = self.d.find_elements_by_name(user_name)
            self.assertEqual(len(button2), 0, msg='关注列表自动刷新Fail')

    def Follow_package1(self):
        """从帖子中关注一个用户的表情包"""
        #点击大杂烩
        self.d.find_element_by_id('com.bugua.fight:id/all_area').click()
        while True:
            self.ElementCheck.random_click('id','com.bugua.fight:id/bbs_title')
            #在帖子中寻找用户头像
            self.ElementCheck.random_click('id','com.bugua.fight:id/avatar')
            #获取名字
            user_name = self.d.find_elements_by_class_name('android.widget.TextView')
            user_name =user_name[1].get_attribute('name')
            print(user_name)
            if user_name == '丑到爆的同桌':
                continue
            #单击表情包
            a = len(self.d.find_elements_by_xpath('//android.support.v7.widget.RecyclerView/\
                                      android.widget.FrameLayout/\
                                      android.widget.LinearLayout'))
            print(a)
            if a > 0:
                self.d.find_element_by_xpath('//android.support.v7.widget.RecyclerView/\
                                            android.widget.FrameLayout/\
                                            android.widget.LinearLayout[1]').click()
            else:
                self.d.back()
                self.d.back()
                user_name = '丑到爆的同桌'
                continue
            self.d.find_element_by_name(user_name).click()
            a2 = self.d.find_elements_by_name('个人资料')
            self.assertEqual(len(a2), 1, msg='进入用户资料失败')
            self.d.back()
            #点击收藏表情包
            self.ElementCheck.click_change('name','关注表情包','hide')
            packagename = self.ElementCheck.attribute_name('id','com.bugua.fight:id/folder_name')
            # time.sleep(5)
            # self.extend.get_screenshot_by_element(self.d.find_element_by_id('com.bugua.fight:id/recycler_view')).write_to_file('./Temp','packpage')
            #关注的表情包检查
            self.d.back()
            self.d.back()
            self.d.back()
            #点击我的
            self.d.find_element_by_id('com.bugua.fight:id/my_pic').click()
            #进入关注表情包
            self.d.find_element_by_name('关注表情包').click()
            result = self.ElementCheck.existence('name',user_name)
            self.ElementCheck.check_assertTrue(result, msg='未找到对应用户的表情包')
            #点击进入用户资料
            result = self.ElementCheck.click_jump('name',user_name,'name','个人资料')
            self.ElementCheck.check_assertTrue(result, msg='未进入对应用的个人资料页面')
            self.d.back()
            #进入表情包
            self.d.find_element_by_xpath('//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]').click()
            # time.sleep(2)
            # load = self.extend.load_image('./Temp/packpage.png')
            # self.extend.get_screenshot_by_element(self.d.find_element_by_id('com.bugua.fight:id/recycler_view')).write_to_file('./Temp','packpage2')
            # result = self.extend.get_screenshot_by_element(self.d.find_element_by_id('com.bugua.fight:id/recycler_view')).same_as(load, 0)
            # self.ElementCheck.check_assertTrue(result, msg='收藏的表情包显示不一致')
            if self.ElementCheck.attribute_name('id','com.bugua.fight:id/folder_name') == packagename:
                result = True
            else:
                result = False
            self.assertTrue(result,msg='所收藏的表情包名称正确')
            time.sleep(1)
            #取消关注表情包
            test = self.d.find_elements_by_name('取消关注')
            print(len(test))
            self.d.find_element_by_name('取消关注').click()
            a4 = self.d.find_elements_by_name('关注表情包')
            self.assertEqual(len(a4),1,msg='取消关注Fail')
            #返回关注列表页面检查
            self.d.back()
            a5 = self.d.find_elements_by_name(user_name)
            self.assertEqual(len(a5), 0,msg='取消关注查看页面Fail')
            break


if __name__=="__main__":
    #编辑用例
    suite = unittest.TestSuite()
    # suite.addTest(Follow_Test('Follow_user1'))
    suite.addTest(Follow_Test('Follow_package1'))
    #执行用例
    runner = unittest.TextTestRunner()
    runner.run(suite)


