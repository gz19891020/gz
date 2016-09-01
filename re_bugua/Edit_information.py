#__author__ = 'gz'
#-*- coding: utf-8 -*-

from appium import webdriver
import time
import unittest
import random
from re_Element_Click_Check import  ElementCheck
from HTMLTestRunner import HTMLTestRunner

class Edit_informationTest(unittest.TestCase):

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
        self.ElementCheck = ElementCheck(self, self.d)
        time.sleep(5)


    def tearDown(self):
        print('Test end')
        self.d.quit()

    def HeadPortraitTest(self):
        """修改头像"""
        #点击【我的】按钮
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/my_tab')
        self.ElementCheck.check_assertTrue(result, msg='进入我的页面失败')
        #点击资料编辑入口
        result = self.ElementCheck.click_jump('xpath','//android.support.v7.widget.RecyclerView/'
                                              'android.widget.LinearLayout/android.widget.LinearLayout','name','编辑信息')
        self.ElementCheck.check_assertTrue(result,msg='进入资料编辑失败')
        #点击头像
        result = self.ElementCheck.click_jump('xpath','//android.widget.RelativeLayout/android.widget.ImageView','name','最近')
        self.ElementCheck.check_assertTrue(result,msg='进入头像选择失败')
        #收集图片
        result = self.ElementCheck.random_click('id','com.android.documentsui:id/icon_thumb')
        self.ElementCheck.check_assertTrue(result,msg='选择头像失败')
        self.d.get_screenshot_as_file('./result/HeadportraitTes.jpg')#其实这里可以用图片不同进行判断
    def RenameTest(self):
        """修改昵称"""
        #点击【我的】按钮
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/my_tab')
        self.ElementCheck.check_assertTrue(result,msg='进入我的页面失败')
        #点击资料编辑入口
        result = self.ElementCheck.click_jump('xpath','//android.support.v7.widget.RecyclerView/'
                                              'android.widget.LinearLayout/android.widget.LinearLayout','name','编辑信息')
        self.ElementCheck.check_assertTrue(result,msg='进入资料编辑失败')
        exname = self.ElementCheck.attribute_name('id','com.bugua.fight:id/user_name')
        #点击昵称
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/nick_name_container','name','修改昵称')
        self.ElementCheck.check_assertTrue(result,msg='修改昵称提示框未弹出')
        #情况昵称输入框
        self.d.find_element_by_id('com.bugua.fight:id/edit_folder_name').clear()
        #获取字数统计
        self.assertEqual(self.ElementCheck.attribute_name('id','com.bugua.fight:id/count'),'14',msg='字是统计有问题')
        #随机产生输入的位数
        number=random.choice(range(1,14))
        name=number*u"g"
        number2=str(14-number)
        #输入number个g
        self.d.find_element_by_id('com.bugua.fight:id/edit_folder_name').send_keys(name)
        #获取字数统计
        self.assertEqual(self.ElementCheck.attribute_name('id','com.bugua.fight:id/count'), number2, msg='字数统计有问题')
        #点击确定
        self.d.find_element_by_id('com.bugua.fight:id/ok').click()
        #点击返回
        self.d.back()
        validate= self.d.find_elements_by_name(name)
        self.assertEqual(len(validate) ,1,msg='名字修改未成功')
        #回复原来的名字
        self.d.find_element_by_xpath('//android.support.v7.widget.RecyclerView/'
                                     'android.widget.LinearLayout/android.widget.LinearLayout').click()
        self.d.find_element_by_id('com.bugua.fight:id/nick_name_container').click()
        self.d.find_element_by_id('com.bugua.fight:id/edit_folder_name').clear()
        self.d.find_element_by_id('com.bugua.fight:id/edit_folder_name').send_keys(exname)
        self.d.find_element_by_id('com.bugua.fight:id/ok').click()

    def SexTest(self):
        """修改性别"""
        #点击【我的】按钮
        self.d.find_element_by_id('com.bugua.fight:id/my_tab').click()
        #点击资料编辑入口
        self.d.find_element_by_xpath('//android.support.v7.widget.RecyclerView/'
                                     'android.widget.LinearLayout/android.widget.LinearLayout').click()
        #点击性别
        self.d.find_element_by_id('com.bugua.fight:id/gender_container').click()
        validate= self.d.find_elements_by_id('com.bugua.fight:id/male')
        self.assertEqual(len(validate) ,1,msg='未发现性别选择按钮_男')
        validate= self.d.find_elements_by_id('com.bugua.fight:id/female')
        self.assertEqual(len(validate) ,1,msg='未发现性别选择按钮_女')
        #点击女
        self.d.find_element_by_id('com.bugua.fight:id/female').click()
        validate= self.d.find_elements_by_name('女')
        self.assertEqual(len(validate) ,1,msg='性别为女修改失败')
        self.d.find_element_by_id('com.bugua.fight:id/gender_container').click()
        #点击男
        self.d.find_element_by_id('com.bugua.fight:id/male').click()
        validate= self.d.find_elements_by_name('男')
        self.assertEqual(len(validate) ,1,msg='性别为男修改失败')

    def SelfIntroductionTest(self):
        """修改自我介绍"""
        #点击【我的】按钮
        self.d.find_element_by_id('com.bugua.fight:id/my_tab').click()
        #点击资料编辑入口
        self.d.find_element_by_xpath('//android.support.v7.widget.RecyclerView/'
                                     'android.widget.LinearLayout/android.widget.LinearLayout').click()
        #点击自我介绍
        self.d.find_element_by_id('com.bugua.fight:id/self_intro').click()
        self.assertEqual(self.d.find_element_by_id('com.bugua.fight:id/title').get_attribute('name'),'自我介绍',msg='进入自我介绍修改页面失败')
        #情况输入框
        self.d.find_element_by_id('com.bugua.fight:id/edit_folder_name').clear()
        self.assertEqual(self.d.find_element_by_id('com.bugua.fight:id/count').get_attribute('name'),'19',msg='字数统计')
        #随机产生输入的位数
        number=random.choice(range(1,19))
        Introduction=number*u"图"
        number2=str(19-number)
        #输入number个图
        self.d.find_element_by_id('com.bugua.fight:id/edit_folder_name').send_keys(Introduction)
        #获取字数统计
        self.assertEqual(self.d.find_element_by_id('com.bugua.fight:id/count').get_attribute('name'), number2, msg='字数统计有问题')
        self.d.find_element_by_id('com.bugua.fight:id/ok').click()
        #修改内容检查
        self.assertEqual(self.d.find_element_by_id('com.bugua.fight:id/intro_tv').get_attribute('name'),Introduction,msg='编辑页面自我介绍显示有问题')
        self.d.back()
        validate= self.d.find_elements_by_name(Introduction)
        self.assertEqual(len(validate) ,1,msg='编辑页面自我介绍显示有问题')

if __name__=="__main__":
    #编辑用例
    suite=unittest.TestSuite()
    suite.addTest(Edit_informationTest('HeadPortraitTest'))
    suite.addTest(Edit_informationTest('RenameTest'))
    suite.addTest(Edit_informationTest('SexTest'))
    suite.addTest(Edit_informationTest('SelfIntroductionTest'))
    #执行用例
    runner =unittest.TextTestRunner()
    runner.run(suite)
