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

class RepliesTest(unittest.TestCase):

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
        self.ElmentCheck = ElementCheck(self,self.d)
        time.sleep(5)

    def tearDown(self):
        print('Test end')
        self.d.quit()

    def EssenceTest(self):
        """精华区回帖"""
        #点击精华区
        self.d.find_element_by_id('com.bugua.fight:id/essence_area').click()
        #随机选取帖子
        self.ElmentCheck.random_click('id','com.bugua.fight:id/bbs_title')
        #对帖子进行回复
        try:
            self.d.find_element_by_name('我要讨论')
            #讨论帖
            c = random.choice(range(2))
            if c == 1:
                self.d.find_element_by_id('com.bugua.fight:id/content_et').send_keys('6666669')
                self.d.find_element_by_id('com.bugua.fight:id/submit_tv').click()
            else:
                self.d.find_element_by_id('com.bugua.fight:id/add_pic_rl').click()
                self.d.find_element_by_id('com.bugua.fight:id/drawee_view_0').click()
                p=self.d.find_elements_by_id('com.bugua.fight:id/check_box_select')
                p[random.choice(range(1,len(p)))].click()
                self.d.find_element_by_id('com.bugua.fight:id/btn_submit').click()
                time.sleep(2)
                self.d.find_element_by_id('com.bugua.fight:id/submit_tv').click()
        except:
            try:
                #求图帖
                #图片回复
                self.d.find_element_by_name('我要求图')
                self.d.find_element_by_id('com.bugua.fight:id/txt_send_emot_container').click()
                self.d.find_element_by_id('com.bugua.fight:id/drawee_view_0').click()
                p=self.d.find_elements_by_id('com.bugua.fight:id/check_box_select')
                p[random.choice(range(1,len(p)))].click()
                self.d.find_element_by_id('com.bugua.fight:id/btn_submit').click()
                time.sleep(2)
                self.d.find_element_by_id('com.bugua.fight:id/btn_send_msg').click()
            except:
                #斗图帖
                b = random.choice(range(2))
                if b == 1:
                    #文字回复
                    self.d.find_element_by_id('com.bugua.fight:id/txt_send_msg_left').click()
                    self.d.find_element_by_id('com.bugua.fight:id/txt_send_msg').send_keys('6666669')
                    self.d.find_element_by_id('com.bugua.fight:id/btn_send_msg').click()
                else:
                    #图片回复
                    self.d.find_element_by_id('com.bugua.fight:id/txt_send_emot').click()
                    self.d.find_element_by_id('com.bugua.fight:id/drawee_view_0').click()
                    p=self.d.find_elements_by_id('com.bugua.fight:id/check_box_select')
                    p[random.choice(range(1,len(p)))].click()
                    self.d.find_element_by_id('com.bugua.fight:id/btn_submit').click()
                    time.sleep(2)
                    self.d.find_element_by_id('com.bugua.fight:id/btn_send_emot').click()

    def PleaseTest(self):
        """求p频道回帖"""
        self.d.find_element_by_id('com.bugua.fight:id/ask_for_ps_tv').click()
        #获取当前页面帖子数量
        self.ElmentCheck.random_click('id','com.bugua.fight:id/bbs_title')
        try:
            self.d.find_element_by_name('我要讨论')
            #讨论帖
            c = random.choice(range(2))
            if c == 1:
                self.d.find_element_by_id('com.bugua.fight:id/content_et').send_keys('6666669')
                self.d.find_element_by_id('com.bugua.fight:id/submit_tv').click()
            else:
                self.d.find_element_by_id('com.bugua.fight:id/add_pic_rl').click()
                self.d.find_element_by_id('com.bugua.fight:id/drawee_view_0').click()
                p=self.d.find_elements_by_id('com.bugua.fight:id/check_box_select')
                p[random.choice(range(1,len(p)))].click()
                self.d.find_element_by_id('com.bugua.fight:id/btn_submit').click()
                self.d.find_element_by_id('com.bugua.fight:id/submit_tv').click()
        except:
            try:
                #求图帖
                #图片回复
                self.d.find_element_by_name('我要求图')
                self.d.find_element_by_id('com.bugua.fight:id/txt_send_emot').click()
                self.d.find_element_by_id('com.bugua.fight:id/drawee_view_0').click()
                p=self.d.find_elements_by_id('com.bugua.fight:id/check_box_select')
                p[random.choice(range(1,len(p)))].click()
                self.d.find_element_by_id('com.bugua.fight:id/btn_submit').click()
                time.sleep(2)
                self.d.find_element_by_id('com.bugua.fight:id/btn_send_msg').click()
            except:
                #斗图帖
                b = random.choice(range(2))
                if b == 1:
                    #文字回复
                    self.d.find_element_by_id('com.bugua.fight:id/txt_send_msg_left').click()
                    self.d.find_element_by_id('com.bugua.fight:id/txt_send_msg').send_keys('6666669')
                    self.d.find_element_by_id('com.bugua.fight:id/btn_send_msg').click()
                else:
                    #图片回复
                    self.d.find_element_by_id('com.bugua.fight:id/txt_send_emot').click()
                    self.d.find_element_by_id('com.bugua.fight:id/drawee_view_0').click()
                    p=self.d.find_elements_by_id('com.bugua.fight:id/check_box_select')
                    p[random.choice(range(1,len(p)))].click()
                    self.d.find_element_by_id('com.bugua.fight:id/btn_submit').click()
                    time.sleep(2)
                    self.d.find_element_by_id('com.bugua.fight:id/btn_send_emot').click()

    def All_areaTest(self):
        """大杂烩回帖"""
        #点击大杂烩
        self.d.find_element_by_id('com.bugua.fight:id/all_area').click()
        #随机选取帖子
        self.ElmentCheck.random_click('id','com.bugua.fight:id/bbs_title')
        #对帖子进行回复
        try:
            self.d.find_element_by_name('我要讨论')
            #讨论帖
            c = random.choice(range(2))
            if c == 1:
                self.d.find_element_by_id('com.bugua.fight:id/content_et').send_keys('6666669')
                self.d.find_element_by_id('com.bugua.fight:id/submit_tv').click()
            else:
                self.d.find_element_by_id('com.bugua.fight:id/add_pic_rl').click()
                self.d.find_element_by_id('com.bugua.fight:id/drawee_view_0').click()
                p=self.d.find_elements_by_id('com.bugua.fight:id/check_box_select')
                p[random.choice(range(1,len(p)))].click()
                self.d.find_element_by_id('com.bugua.fight:id/btn_submit').click()
                self.d.find_element_by_id('com.bugua.fight:id/submit_tv').click()
        except:
            try:
                #求图帖
                #图片回复
                self.d.find_element_by_name('我要求图')
                self.d.find_element_by_id('com.bugua.fight:id/txt_send_emot').click()
                self.d.find_element_by_id('com.bugua.fight:id/drawee_view_0').click()
                p=self.d.find_elements_by_id('com.bugua.fight:id/check_box_select')
                p[random.choice(range(1,len(p)))].click()
                self.d.find_element_by_id('com.bugua.fight:id/btn_submit').click()
                time.sleep(2)
                self.d.find_element_by_id('com.bugua.fight:id/btn_send_msg').click()
            except:
                #斗图帖
                b = random.choice(range(2))
                if b == 1:
                    #文字回复
                    self.d.find_element_by_id('com.bugua.fight:id/txt_send_msg_left').click()
                    self.d.find_element_by_id('com.bugua.fight:id/txt_send_msg').send_keys('6666669')
                    self.d.find_element_by_id('com.bugua.fight:id/btn_send_msg').click()
                else:
                    #图片回复
                    self.d.find_element_by_id('com.bugua.fight:id/txt_send_emot').click()
                    self.d.find_element_by_id('com.bugua.fight:id/drawee_view_0').click()
                    p=self.d.find_elements_by_id('com.bugua.fight:id/check_box_select')
                    p[random.choice(range(1,len(p)))].click()
                    self.d.find_element_by_id('com.bugua.fight:id/btn_submit').click()
                    time.sleep(2)
                    self.d.find_element_by_id('com.bugua.fight:id/btn_send_emot').click()

    def post_send_box_hide(self):
        """帖子预览框隐藏"""
        self.d.find_element_by_id('com.bugua.fight:id/ask_for_ps_tv').click()
        #获取当前页面帖子数量
        self.ElmentCheck.random_click('id','com.bugua.fight:id/bbs_title')
        #点击发送框
        try:
            self.d.find_element_by_name('我要讨论')
            #点击发送框
            self.d.find_element_by_id('com.bugua.fight:id/add_pic').click()
        except:
            try:
                self.d.find_element_by_name('我要求图')
                self.d.find_element_by_id('com.bugua.fight:id/txt_send_emot_container').click()
            except:
                self.d.find_element_by_id('com.bugua.fight:id/txt_send_emot_container').click()

        #滑动页面
        size=self.d.get_window_size()
        width=size['width']
        height=size['height']
        print(width,height)
        self.d.swipe(width*200/1080, height*720/1776, width*200/1080, height*300/1776)
        a = self.d.find_elements_by_id('com.bugua.fight:id/drawee_view_0')
        self.assertEqual(len(a) , 0 , msg='发送框未收起')

    def all_area_send_box_hide(self):
        """大杂烩帖子预览框隐藏"""
        #点击大杂烩
        self.d.find_element_by_id('com.bugua.fight:id/all_area').click()
        #随机选取帖子
        self.ElmentCheck.random_click('id','com.bugua.fight:id/bbs_title')
        try:
            self.d.find_element_by_name('我要讨论')
            #点击发送框
            self.d.find_element_by_id('com.bugua.fight:id/add_pic').click()
        except:
            try:
                self.d.find_element_by_name('我要求图')
                self.d.find_element_by_id('com.bugua.fight:id/txt_send_emot_container').click()
            except:
                self.d.find_element_by_id('com.bugua.fight:id/txt_send_emot_container').click()

        #滑动页面
        size=self.d.get_window_size()
        width=size['width']
        height=size['height']
        print(width,height)
        self.d.swipe(width*680/760, height*500/1776, width*680/760, height*100/1776)
        a = self.d.find_elements_by_id('com.bugua.fight:id/drawee_view_0')
        self.assertEqual(len(a) , 0 , msg='发送框未收起')

    def one_click1(self):
        """表情键盘一键生成不带文字"""
        #点击大杂烩
        self.ElmentCheck.click_change('id','com.bugua.fight:id/all_area')
        #随机选取帖子
        self.ElmentCheck.random_click('id','com.bugua.fight:id/bbs_title')
        try:
            self.d.find_element_by_name('我要讨论')
            #点击发送框
            self.d.find_element_by_id('com.bugua.fight:id/add_pic').click()
        except:
            try:
                self.d.find_element_by_name('我要求图')
                self.d.find_element_by_id('com.bugua.fight:id/txt_send_emot_container').click()
            except:
                self.d.find_element_by_id('com.bugua.fight:id/txt_send_emot_container').click()
        #点击一键生成表情按钮
        self.ElmentCheck.click_jump('id','com.bugua.fight:id/drawee_view_1', 'name', '一键生成')
        #输入内容
        self.d.find_element_by_id('com.bugua.fight:id/input_et').send_keys('不要装逼')
        #点击一键生成
        self.d.find_element_by_name('一键生成').click()
        #time.sleep(2)
        self.ElmentCheck.wait('xpath','//android.widget.ImageView/..')
        #计数是否为0
        result = self.ElmentCheck.existence('name','（0）完成')
        self.ElmentCheck.check_assertTrue(result,msg='计数显示fail')
        time.sleep(5)
        #随机选择图片
        self.ElmentCheck.random_click('xpath','//android.widget.ImageView/..')
        #计数是否为1
        result = self.ElmentCheck.existence('name','（1）完成')
        self.ElmentCheck.check_assertTrue(result,msg='计数显示fail')
        #点击完成按钮
        self.d.find_element_by_id('com.bugua.fight:id/finish_btn').click()
        time.sleep(1)
        try:
            os._exists(r'./Fail_picture') == False
            os.mkdir(r'./Fail_picture')
        except:
                pass
        self.d.get_screenshot_as_file('./result/one_click1.png')

    def one_click2(self):
        """表情键盘一键生成不带文字"""
        #点击大杂烩
        self.ElmentCheck.click_change('id','com.bugua.fight:id/all_area')
        #选取讨论帖子
        while True:
            try:
                #随机选取帖子
                self.ElmentCheck.random_click('id','com.bugua.fight:id/bbs_title')
                self.d.find_element_by_name('我要讨论')
                #文本框输入内容
                self.d.find_element_by_id('com.bugua.fight:id/content_et').send_keys('不要装逼了')
                #点击发送框
                self.d.find_element_by_id('com.bugua.fight:id/add_pic').click()
                break
            except:
                self.d.back()
                continue

        #点击一键生成表情按钮
        self.ElmentCheck.click_jump('id','com.bugua.fight:id/drawee_view_1', 'name', '一键生成')
        #输入内容
        result = self.ElmentCheck.attribute_name('id','com.bugua.fight:id/input_et','不要装逼了')
        self.ElmentCheck.check_assertTrue(result,msg='未将文本带入')
        #点击一键生成
        self.d.find_element_by_name('一键生成').click()
        #time.sleep(2)
        self.ElmentCheck.wait('xpath','//android.widget.ImageView/..')
        #计数是否为0
        result = self.ElmentCheck.existence('name','（0）完成')
        self.ElmentCheck.check_assertTrue(result,msg='计数显示fail')
        time.sleep(5)
        #随机选择图片
        self.ElmentCheck.random_click('xpath','//android.widget.ImageView/..')
        #计数是否为1
        result = self.ElmentCheck.existence('name','（1）完成')
        self.ElmentCheck.check_assertTrue(result,msg='计数显示fail')
        #点击完成按钮
        self.d.find_element_by_id('com.bugua.fight:id/finish_btn').click()
        time.sleep(1)
        try:
            os._exists(r'./Fail_picture') == False
            os.mkdir(r'./Fail_picture')
        except:
                pass
        self.d.get_screenshot_as_file('./result/one_click2.png')







if __name__=="__main__":
    #编辑用例
    suite = unittest.TestSuite()
    # suite.addTest(RepliesTest('EssenceTest'))
    # suite.addTest(RepliesTest('PleaseTest'))
    # suite.addTest(RepliesTest('All_areaTest'))
    # suite.addTest(RepliesTest('post_send_box_hide'))
    # suite.addTest(RepliesTest('all_area_send_box_hide'))
    suite.addTest(RepliesTest('one_click1'))
    # suite.addTest(RepliesTest('one_click2'))
    #执行用例
    runner = unittest.TextTestRunner()
    runner.run(suite)
    #fp = open(filename, 'wb')
    #runner = HTMLTestRunner(stream = fp , title='自动化测试报告' , description='自动化测试报告')
    #runner.run(suite)


