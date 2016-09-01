#__author__ = 'gz'
#-*- coding: utf-8 -*-

from appium import webdriver
import time
import unittest
import random
from extend import Appium_Extend
from HTMLTestRunner import HTMLTestRunner
from re_Element_Click_Check import ElementCheck

class PostTest(unittest.TestCase):

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
        self.d.quit()

    def Tv_theme_name_Test(self):
        """发帖主题内容检查"""
        #只能检查收藏主题对应的前两个
        #点击主题
        self.d.find_element_by_id('com.bugua.fight:id/theme_tv').click()
        #获取主题
        a2=[]
        a2.append(self.ElementCheck.attribute_name('ides','com.bugua.fight:id/tv_theme_name[0]'))
        a2.append(self.ElementCheck.attribute_name('ides','com.bugua.fight:id/tv_theme_name[1]'))
        #print(a2)
        #点击【发帖】按钮
        self.d.find_element_by_id('com.bugua.fight:id/btn_new_topic').click()
        #点击斗图
        self.d.find_element_by_id('com.bugua.fight:id/click_type_find').click()
        #点击发帖位置选择
        self.d.find_element_by_id('com.bugua.fight:id/post_topic_area').click()
        result = self.ElementCheck.click_jump('xpath','//android.support.v7.widget.RecyclerView/'
                                     'android.widget.LinearLayout/'
                                     'android.widget.LinearLayout[1]/'
                                     'android.widget.TextView','name','大杂烩')
        self.ElementCheck.check_assertTrue(result,msg='关注的主题顺序错误',)
        b2=[]
        b2.append(self.ElementCheck.attribute_name('ides','com.bugua.fight:id/theme_name[0]'))
        b2.append(self.ElementCheck.attribute_name('ides','com.bugua.fight:id/theme_name[1]'))
        self.assertEqual(b2[0],a2[0],msg='关注的主题顺序错误')
        self.assertEqual(b2[1],a2[1],msg='关注的主题顺序错误')

    def FindPostTest(self):
        """发求图帖"""
        #求图
        #点击【发帖】按钮
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/btn_new_topic','name','选择发帖类型')
        self.ElementCheck.check_assertTrue(result,msg='发帖按钮FAil')
        self.d.find_element_by_id('com.bugua.fight:id/click_type_find').click()
        #标题输入框输入标题
        self.d.find_element_by_id('com.bugua.fight:id/et_bbs_title').send_keys('都谁有这种图拿出来')
        #输入内容
        text='有这种图的就不要客气的拿出来吧!'
        self.d.find_element_by_id('com.bugua.fight:id/et_bbs_content').send_keys(text)
        #选图
        self.d.find_element_by_id('com.bugua.fight:id/emotion_thumb').click()
        checkbox = self.d.find_elements_by_id('com.bugua.fight:id/check_box_select')
        checkbox[0].click()
        time.sleep(1)
        result = self.ElementCheck.existence('name','预览')
        self.ElementCheck.check_assertTrue(result,msg='选择图片后预览按钮fail')
        time.sleep(1)
        result = self.ElementCheck.existence('name','完成(1/8)')
        self.ElementCheck.check_assertTrue(result,msg='选择图片后计数fail')
        time.sleep(1)
        # pic_select=self.d.find_elements_by_id('com.bugua.fight:id/pic_select')
        # pic_select[random.choice(range(1,len(checkbox)))].click()
        self.ElementCheck.random_click('id','com.bugua.fight:id/pic_select')
        time.sleep(1)
        self.d.find_element_by_id('com.bugua.fight:id/tv_selector').click()
        time.sleep(1)
        result = self.ElementCheck.existence('name','完成(2/8)')
        self.ElementCheck.check_assertTrue(result,msg='选择图片后计数fail')
        time.sleep(1)
        #其他相册中进行选图
        self.d.back()
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/tv_other','name','所有照片')
        self.ElementCheck.check_assertTrue(result,msg='其他相册按钮失败')
        #随机选择相册
        self.ElementCheck.random_click('id','com.bugua.fight:id/folder_name')
        time.sleep(1)
        self.ElementCheck.random_click('id','com.bugua.fight:id/check_box_select')
        result = self.ElementCheck.existence('name','完成(3/8)')
        self.ElementCheck.check_assertTrue(result,msg='选择图片后计数fail')
        self.d.find_element_by_id('com.bugua.fight:id/btn_submit').click()
        time.sleep(1)
        #删除一张图片
        delete = self.d.find_elements_by_id('com.bugua.fight:id/delete_emotion')
        delete[random.choice(range(0,len(delete)))].click()
        #提交图片
        self.d.find_element_by_id('com.bugua.fight:id/btn_submit').click()
        time.sleep(10)
        self.d.find_element_by_name('H都谁有这种图拿出来').click()
        time.sleep(2)
        print('发现所发帖子')
        self.d.get_screenshot_as_file('C:\\Users\\yuelian\\Desktop\\DTtestresult\\tiezi.jpg')
        validate= self.d.find_elements_by_name(text)
        self.assertEqual(len(validate) , 1, msg='内容输入错误')

    def FightPostTest(self):
        """发斗图帖"""
        #点击【发帖】按钮
        self.d.find_element_by_id('com.bugua.fight:id/btn_new_topic').click()
        self.d.find_element_by_id('com.bugua.fight:id/click_type_fight').click()
        #标题输入框输入标题
        self.d.find_element_by_id('com.bugua.fight:id/et_bbs_title').send_keys('斗啊')
        #输入内容
        text='有这种图的就不要客气的拿出来吧!'
        self.d.find_element_by_id('com.bugua.fight:id/et_bbs_content').send_keys(text)
        #选图
        self.d.find_element_by_id('com.bugua.fight:id/emotion_thumb').click()
        checkbox = self.d.find_elements_by_id('com.bugua.fight:id/check_box_select')
        checkbox[0].click()
        time.sleep(1)
        result = self.ElementCheck.existence('name','预览')
        self.ElementCheck.check_assertTrue(result,msg='选择图片后预览按钮fail')
        time.sleep(1)
        result = self.ElementCheck.existence('name','完成(1/8)')
        self.ElementCheck.check_assertTrue(result,msg='选择图片后计数fail')
        time.sleep(1)
        # pic_select=self.d.find_elements_by_id('com.bugua.fight:id/pic_select')
        # pic_select[random.choice(range(1,len(checkbox)))].click()
        self.ElementCheck.random_click('id','com.bugua.fight:id/pic_select')
        time.sleep(1)
        self.d.find_element_by_id('com.bugua.fight:id/tv_selector').click()
        time.sleep(1)
        result = self.ElementCheck.existence('name','完成(2/8)')
        self.ElementCheck.check_assertTrue(result,msg='选择图片后计数fail')
        time.sleep(1)
        #其他相册中进行选图
        self.d.back()
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/tv_other','name','所有照片')
        self.ElementCheck.check_assertTrue(result,msg='其他相册按钮失败')
        #随机选择相册
        self.ElementCheck.random_click('id','com.bugua.fight:id/folder_name')
        time.sleep(1)
        self.ElementCheck.random_click('id','com.bugua.fight:id/check_box_select')
        result = self.ElementCheck.existence('name','完成(3/8)')
        self.ElementCheck.check_assertTrue(result,msg='选择图片后计数fail')
        self.d.find_element_by_id('com.bugua.fight:id/btn_submit').click()
        time.sleep(1)
        #删除一张图片
        delete = self.d.find_elements_by_id('com.bugua.fight:id/delete_emotion')
        delete[random.choice(range(0,len(delete)))].click()
        time.sleep(1)
        self.d.get_screenshot_as_file('.\\picture\\fatiezi.jpg')
        self.d.find_element_by_id('com.bugua.fight:id/btn_submit').click()
        time.sleep(10)
        self.d.find_element_by_name('H斗啊').click()
        time.sleep(2)
        print('发现所发帖子')
        self.d.get_screenshot_as_file('.\\picture\\fightpost.jpg')
        validate= self.d.find_elements_by_name(text)
        self.assertEqual(len(validate) , 1, msg='内容输入错误')

    def DiscussPostTest(self):
        """发讨论帖"""
        #点击【发帖】按钮
        self.d.find_element_by_id('com.bugua.fight:id/btn_new_topic').click()
        self.d.find_element_by_id('com.bugua.fight:id/click_type_discuss').click()
        #标题输入框输入标题
        self.d.find_element_by_id('com.bugua.fight:id/et_bbs_title').send_keys('来看看这些好玩的图片')
        #输入内容
        text='有这种图的就不要客气的拿出来吧!'
        self.d.find_element_by_id('com.bugua.fight:id/et_bbs_content').send_keys(text)
        #选图
        self.d.find_element_by_id('com.bugua.fight:id/emotion_thumb').click()
        checkbox = self.d.find_elements_by_id('com.bugua.fight:id/check_box_select')
        checkbox[0].click()
        time.sleep(1)
        result = self.ElementCheck.existence('name','预览')
        self.ElementCheck.check_assertTrue(result,msg='选择图片后预览按钮fail')
        time.sleep(1)
        result = self.ElementCheck.existence('name','完成(1/20)')
        self.ElementCheck.check_assertTrue(result,msg='选择图片后计数fail')
        time.sleep(1)
        # pic_select=self.d.find_elements_by_id('com.bugua.fight:id/pic_select')
        # pic_select[random.choice(range(1,len(checkbox)))].click()
        self.ElementCheck.random_click('id','com.bugua.fight:id/pic_select')
        time.sleep(1)
        self.d.find_element_by_id('com.bugua.fight:id/tv_selector').click()
        time.sleep(1)
        result = self.ElementCheck.existence('name','完成(2/20)')
        self.ElementCheck.check_assertTrue(result,msg='选择图片后计数fail')
        time.sleep(1)
        #其他相册中进行选图
        self.d.back()
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/tv_other','name','所有照片')
        self.ElementCheck.check_assertTrue(result,msg='其他相册按钮失败')
        #随机选择相册
        self.ElementCheck.random_click('id','com.bugua.fight:id/folder_name')
        time.sleep(1)
        self.ElementCheck.random_click('id','com.bugua.fight:id/check_box_select')
        result = self.ElementCheck.existence('name','完成(3/20)')
        self.ElementCheck.check_assertTrue(result,msg='选择图片后计数fail')
        self.d.find_element_by_id('com.bugua.fight:id/btn_submit').click()
        time.sleep(1)
        #删除一张图片
        delete = self.d.find_elements_by_id('com.bugua.fight:id/delete_emotion')
        delete[random.choice(range(0,len(delete)))].click()
        time.sleep(1)
        self.d.get_screenshot_as_file('.\\picture\\discusspost.jpg')
        self.d.find_element_by_id('com.bugua.fight:id/btn_submit').click()
        time.sleep(10)
        self.d.find_element_by_name('H来看看这些好玩的图片').click()
        time.sleep(2)
        print('发现所发帖子')
        self.d.get_screenshot_as_file('.\\picture\\fightpost.jpg')
        validate= self.d.find_elements_by_name(text)
        self.assertEqual(len(validate) , 1, msg='内容输入错误')




if __name__=="__main__":
    suite=unittest.TestSuite()
    suite.addTest(PostTest('Tv_theme_name_Test'))
    suite.addTest(PostTest('FindPostTest'))
    suite.addTest(PostTest('FightPostTest'))
    suite.addTest(PostTest('DiscussPostTest'))
    #执行用例
    runner = unittest.TextTestRunner()
    runner.run(suite)

