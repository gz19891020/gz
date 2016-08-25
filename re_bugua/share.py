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

class ShareTest(unittest.TestCase):

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
        time.sleep(5)


    def tearDown(self):
        print('Test end')
        self.d.quit()
    #帖子单击图片进行直接发送
    def post_share_click_QQ(self):
        #随机点击一个帖子
        self.ElementCheck.random_click('id','com.bugua.fight:id/bbs_title')
        time.sleep(2)
        #单击帖子中的图片
        self.ElementCheck.random_click('id','com.bugua.fight:id/pic')
        time.sleep(5)
        #分享到QQ
        self.ElementCheck.share_picture_QQ()
    def post_share_click_kongjian(self):
        #随机点击一个帖子
        self.ElementCheck.random_click('id','com.bugua.fight:id/bbs_title')
        time.sleep(3)
        #单击帖子中的图片
        self.ElementCheck.random_click('id','com.bugua.fight:id/pic')
        time.sleep(5)
        #发送到QQ空间
        self.ElementCheck.share_picture_kongjian()
    def post_share_click_weixin(self):
        #随机点击一个帖子
        self.ElementCheck.random_click('id','com.bugua.fight:id/bbs_title')
        time.sleep(2)
        #单击帖子中的图片
        self.ElementCheck.random_click('id','com.bugua.fight:id/pic')
        time.sleep(2)
        #发送到微信
        self.ElementCheck.share_picture_weixin()
    def post_share_click_pengyouquan(self):
        #随机点击一个帖子
        self.ElementCheck.random_click('id','com.bugua.fight:id/bbs_title')
        time.sleep(2)
        #单击帖子中的图片
        self.ElementCheck.random_click('id','com.bugua.fight:id/pic')
        time.sleep(2)
        #发送到朋友圈
        self.ElementCheck.share_picture_pengyouquan()
    def post_share_click_renren(self):
        #随机点击一个帖子
        self.ElementCheck.random_click('id','com.bugua.fight:id/bbs_title')
        time.sleep(2)
        #单击帖子中的图片
        self.ElementCheck.random_click('id','com.bugua.fight:id/pic')
        time.sleep(2)
        #发送到人人
        self.ElementCheck.share_picture_renren()
    def post_share_click_momo(self):
        #随机点击一个帖子
        self.ElementCheck.random_click('id','com.bugua.fight:id/bbs_title')
        time.sleep(2)
        #单击帖子中的图片
        self.ElementCheck.random_click('id','com.bugua.fight:id/pic')
        time.sleep(2)
        #发送到陌陌
        self.ElementCheck.share_picture_momo()
    #帖子长按图片进行直接发送
    def post_share_longpass_QQ(self):
        #随机点击一个帖子
        self.ElementCheck.random_click('id','com.bugua.fight:id/bbs_title')
        time.sleep(2)
        #单击帖子中的图片
        self.ElementCheck.random_click('id','com.bugua.fight:id/pic','long_pass')
        time.sleep(2)
        #分享到QQ
        self.ElementCheck.share_picture_QQ()
    def post_share_longpass_kongjian(self):
        #随机点击一个帖子
        self.ElementCheck.random_click('id','com.bugua.fight:id/bbs_title')
        time.sleep(2)
        #单击帖子中的图片
        self.ElementCheck.random_click('id','com.bugua.fight:id/pic','long_pass')
        time.sleep(2)
        #发送到QQ空间
        self.ElementCheck.share_picture_kongjian()
    def post_share_longpass_weixin(self):
        #随机点击一个帖子
        self.ElementCheck.random_click('id','com.bugua.fight:id/bbs_title')
        time.sleep(2)
        #单击帖子中的图片
        self.ElementCheck.random_click('id','com.bugua.fight:id/pic','long_pass')
        time.sleep(2)
        #发送到微信
        self.ElementCheck.share_picture_weixin()
    def post_share_longpass_pengyouquan(self):
        #随机点击一个帖子
        self.ElementCheck.random_click('id','com.bugua.fight:id/bbs_title')
        time.sleep(2)
        #单击帖子中的图片
        self.ElementCheck.random_click('id','com.bugua.fight:id/pic','long_pass')
        time.sleep(2)
        #发送到朋友圈
        self.ElementCheck.share_picture_pengyouquan()
    def post_share_longpass_renren(self):
        #随机点击一个帖子
        self.ElementCheck.random_click('id','com.bugua.fight:id/bbs_title')
        time.sleep(2)
        #单击帖子中的图片
        self.ElementCheck.random_click('id','com.bugua.fight:id/pic','long_pass')
        time.sleep(2)
        #发送到人人
        self.ElementCheck.share_picture_renren()
    def post_share_longpass_momo(self):
        #随机点击一个帖子
        self.ElementCheck.random_click('id','com.bugua.fight:id/bbs_title')
        time.sleep(2)
        #单击帖子中的图片
        self.ElementCheck.random_click('id','com.bugua.fight:id/pic','long_pass')
        time.sleep(2)
        #发送到陌陌
        self.ElementCheck.share_picture_momo()
    #主题图片墙单击图片进行直接发送
    def theme_picture_click_QQ(self):
        #点击主题
        #点击主题
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/theme_tv')
        self.ElementCheck.check_assertTrue(result,msg='进入主题失败')
        #点击发现更多主题
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/more_normal_theme','name','关注列表')
        self.ElementCheck.check_assertTrue(result, msg='未进入关注列表')
        #选择一个主题
        time.sleep(3)
        self.ElementCheck.random_click('id','com.bugua.fight:id/click_area')
        #点击图片墙
        self.d.find_element_by_name('图片墙').click()
        #点击图片
        self.ElementCheck.random_click('id','com.bugua.fight:id/jgznewpic_content')
        #分享到QQ
        self.ElementCheck.share_picture_QQ()
    def theme_picture_click_kongjian(self):
        #点击主题
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/theme_tv')
        self.ElementCheck.check_assertTrue(result,msg='进入主题失败')
        #点击发现更多主题
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/more_normal_theme','name','关注列表')
        self.ElementCheck.check_assertTrue(result, msg='未进入关注列表')
        #选择一个主题
        time.sleep(3)
        self.ElementCheck.random_click('id','com.bugua.fight:id/click_area')
        #点击图片墙
        self.d.find_element_by_name('图片墙').click()
        #点击图片
        self.ElementCheck.random_click('id','com.bugua.fight:id/jgznewpic_content')
        #发送到QQ空间
        self.ElementCheck.share_picture_kongjian()
    def theme_picture_click_weixin(self):
        #点击主题
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/theme_tv')
        self.ElementCheck.check_assertTrue(result,msg='进入主题失败')
        #点击发现更多主题
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/more_normal_theme','name','关注列表')
        self.ElementCheck.check_assertTrue(result, msg='未进入关注列表')
        #选择一个主题
        time.sleep(3)
        self.ElementCheck.random_click('id','com.bugua.fight:id/click_area')
        #点击图片墙
        self.d.find_element_by_name('图片墙').click()
        #点击图片
        self.ElementCheck.random_click('id','com.bugua.fight:id/jgznewpic_content')
        #发送到微信
        self.ElementCheck.share_picture_weixin()
    def theme_picture_click_pengyouquan(self):
        #点击主题
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/theme_tv')
        self.ElementCheck.check_assertTrue(result,msg='进入主题失败')
        #点击发现更多主题
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/more_normal_theme','name','关注列表')
        self.ElementCheck.check_assertTrue(result, msg='未进入关注列表')
        #选择一个主题
        time.sleep(3)
        self.ElementCheck.random_click('id','com.bugua.fight:id/click_area')
        #点击图片墙
        self.d.find_element_by_name('图片墙').click()
        #点击图片
        self.ElementCheck.random_click('id','com.bugua.fight:id/jgznewpic_content')
        #发送到朋友圈
        self.ElementCheck.share_picture_pengyouquan()
    def theme_picture_click_renren(self):
        #点击主题
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/theme_tv')
        self.ElementCheck.check_assertTrue(result,msg='进入主题失败')
        #点击发现更多主题
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/more_normal_theme','name','关注列表')
        self.ElementCheck.check_assertTrue(result, msg='未进入关注列表')
        #选择一个主题
        time.sleep(3)
        self.ElementCheck.random_click('id','com.bugua.fight:id/click_area')
        #点击图片墙
        self.d.find_element_by_name('图片墙').click()
        #点击图片
        self.ElementCheck.random_click('id','com.bugua.fight:id/jgznewpic_content')
        #发送到人人
        self.ElementCheck.share_picture_renren()
    def theme_picture_click_momo(self):
        #点击主题
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/theme_tv')
        self.ElementCheck.check_assertTrue(result,msg='进入主题失败')
        #点击发现更多主题
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/more_normal_theme','name','关注列表')
        self.ElementCheck.check_assertTrue(result, msg='未进入关注列表')
        #选择一个主题
        self.ElementCheck.random_click('id','com.bugua.fight:id/click_area')
        #点击图片墙
        time.sleep(3)
        self.d.find_element_by_name('图片墙').click()
        #点击图片
        self.ElementCheck.random_click('id','com.bugua.fight:id/jgznewpic_content')
        #发送到陌陌
        self.ElementCheck.share_picture_momo()
    #主题图片墙长按图片
    def theme_picture_longpass_QQ(self):
        #点击主题
        #点击主题
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/theme_tv')
        self.ElementCheck.check_assertTrue(result,msg='进入主题失败')
        #点击发现更多主题
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/more_normal_theme','name','关注列表')
        self.ElementCheck.check_assertTrue(result, msg='未进入关注列表')
        #选择一个主题
        time.sleep(3)
        self.ElementCheck.random_click('id','com.bugua.fight:id/click_area')
        #点击图片墙
        self.d.find_element_by_name('图片墙').click()
        #长按图片
        self.ElementCheck.random_click('id','com.bugua.fight:id/jgznewpic_content','long_pass')
        #分享到QQ
        self.ElementCheck.share_picture_QQ()
    def theme_picture_longpass_kongjian(self):
        #点击主题
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/theme_tv')
        self.ElementCheck.check_assertTrue(result,msg='进入主题失败')
        #点击发现更多主题
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/more_normal_theme','name','关注列表')
        self.ElementCheck.check_assertTrue(result, msg='未进入关注列表')
        #选择一个主题
        time.sleep(3)
        self.ElementCheck.random_click('id','com.bugua.fight:id/click_area')
        #点击图片墙
        self.d.find_element_by_name('图片墙').click()
        #长按图片
        self.ElementCheck.random_click('id','com.bugua.fight:id/jgznewpic_content','long_pass')
        #发送到QQ空间
        self.ElementCheck.share_picture_kongjian()
    def theme_picture_longpass_weixin(self):
        #点击主题
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/theme_tv')
        self.ElementCheck.check_assertTrue(result,msg='进入主题失败')
        #点击发现更多主题
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/more_normal_theme','name','关注列表')
        self.ElementCheck.check_assertTrue(result, msg='未进入关注列表')
        #选择一个主题
        time.sleep(3)
        self.ElementCheck.random_click('id','com.bugua.fight:id/click_area')
        #点击图片墙
        self.d.find_element_by_name('图片墙').click()
        #长按图片
        self.ElementCheck.random_click('id','com.bugua.fight:id/jgznewpic_content','long_pass')
        #发送到微信
        self.ElementCheck.share_picture_weixin()
    def theme_picture_longpass_pengyouquan(self):
        #点击主题
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/theme_tv')
        self.ElementCheck.check_assertTrue(result,msg='进入主题失败')
        #点击发现更多主题
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/more_normal_theme','name','关注列表')
        self.ElementCheck.check_assertTrue(result, msg='未进入关注列表')
        #选择一个主题
        time.sleep(3)
        self.ElementCheck.random_click('id','com.bugua.fight:id/click_area')
        #点击图片墙
        self.d.find_element_by_name('图片墙').click()
        #长按图片
        self.ElementCheck.random_click('id','com.bugua.fight:id/jgznewpic_content','long_pass')
        #发送到朋友圈
        self.ElementCheck.share_picture_pengyouquan()
    def theme_picture_longpass_renren(self):
        #点击主题
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/theme_tv')
        self.ElementCheck.check_assertTrue(result,msg='进入主题失败')
        #点击发现更多主题
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/more_normal_theme','name','关注列表')
        self.ElementCheck.check_assertTrue(result, msg='未进入关注列表')
        #选择一个主题
        time.sleep(3)
        self.ElementCheck.random_click('id','com.bugua.fight:id/click_area')
        #点击图片墙
        self.d.find_element_by_name('图片墙').click()
        #长按图片
        self.ElementCheck.random_click('id','com.bugua.fight:id/jgznewpic_content','long_pass')
        #发送到人人
        self.ElementCheck.share_picture_renren()
    def theme_picture_longpass_momo(self):
        #点击主题
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/theme_tv')
        self.ElementCheck.check_assertTrue(result,msg='进入主题失败')
        #点击发现更多主题
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/more_normal_theme','name','关注列表')
        self.ElementCheck.check_assertTrue(result, msg='未进入关注列表')
        #选择一个主题
        time.sleep(3)
        self.ElementCheck.random_click('id','com.bugua.fight:id/click_area')
        #点击图片墙
        self.d.find_element_by_name('图片墙').click()
        #长按图片
        self.ElementCheck.random_click('id','com.bugua.fight:id/jgznewpic_content','long_pass')
        #发送到陌陌
        self.ElementCheck.share_picture_momo()
    #新图单击直接发送按钮
    def now_picture_click_QQ(self):
        #点击发现
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/home_pic')
        self.ElementCheck.check_assertTrue(result,msg='发现按钮Fail')
        #点击新图
        self.d.find_element_by_id('com.bugua.fight:id/new_pic_tv').click()
        #随机获取图片
        self.ElementCheck.random_click('id','com.bugua.fight:id/jgznewpic_content')
        #分享到QQ
        self.ElementCheck.share_picture_QQ()
    def now_picture_click_kongjian(self):
        #点击发现
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/home_pic')
        self.ElementCheck.check_assertTrue(result,msg='发现按钮Fail')
        #点击新图
        self.d.find_element_by_id('com.bugua.fight:id/new_pic_tv').click()
        #随机获取图片
        self.ElementCheck.random_click('id','com.bugua.fight:id/jgznewpic_content')
        #发送到QQ空间
        self.ElementCheck.share_picture_kongjian()
    def now_picture_click_weixin(self):
        #点击发现
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/home_pic')
        self.ElementCheck.check_assertTrue(result,msg='发现按钮Fail')
        #点击新图
        self.d.find_element_by_id('com.bugua.fight:id/new_pic_tv').click()
        #随机获取图片
        self.ElementCheck.random_click('id','com.bugua.fight:id/jgznewpic_content')
        #发送到微信
        self.ElementCheck.share_picture_weixin()
    def now_picture_click_pengyouquan(self):
        #点击发现
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/home_pic')
        self.ElementCheck.check_assertTrue(result,msg='发现按钮Fail')
        #点击新图
        self.d.find_element_by_id('com.bugua.fight:id/new_pic_tv').click()
        #随机获取图片
        self.ElementCheck.random_click('id','com.bugua.fight:id/jgznewpic_content')
        #发送到朋友圈
        self.ElementCheck.share_picture_pengyouquan()
    def now_picture_click_renren(self):
        #点击发现
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/home_pic')
        self.ElementCheck.check_assertTrue(result,msg='发现按钮Fail')
        #点击新图
        self.d.find_element_by_id('com.bugua.fight:id/new_pic_tv').click()
        #随机获取图片
        self.ElementCheck.random_click('id','com.bugua.fight:id/jgznewpic_content')
        #发送到人人
        self.ElementCheck.share_picture_renren()
    def now_picture_click_momo(self):
        #点击发现
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/home_pic')
        self.ElementCheck.check_assertTrue(result,msg='发现按钮Fail')
        #点击新图
        self.d.find_element_by_id('com.bugua.fight:id/new_pic_tv').click()
        #随机获取图片
        self.ElementCheck.random_click('id','com.bugua.fight:id/jgznewpic_content')
        #发送到陌陌
        self.ElementCheck.share_picture_momo()
    #新图长按直接发送按钮
    def now_picture_longpass_QQ(self):
        #点击发现
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/home_pic')
        self.ElementCheck.check_assertTrue(result,msg='发现按钮Fail')
        #点击新图
        self.d.find_element_by_id('com.bugua.fight:id/new_pic_tv').click()
        #随机长按图片
        self.ElementCheck.random_click('id','com.bugua.fight:id/jgznewpic_content','long_pass')
        #分享到QQ
        self.ElementCheck.share_picture_QQ()
    def now_picture_longpass_kongjian(self):
        #点击发现
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/home_pic')
        self.ElementCheck.check_assertTrue(result,msg='发现按钮Fail')
        #点击新图
        self.d.find_element_by_id('com.bugua.fight:id/new_pic_tv').click()
        #随机长按图片
        self.ElementCheck.random_click('id','com.bugua.fight:id/jgznewpic_content','long_pass')
        #发送到QQ空间
        self.ElementCheck.share_picture_kongjian()
    def now_picture_longpass_weixin(self):
        #点击发现
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/home_pic')
        self.ElementCheck.check_assertTrue(result,msg='发现按钮Fail')
        #点击新图
        self.d.find_element_by_id('com.bugua.fight:id/new_pic_tv').click()
        #随机长按图片
        self.ElementCheck.random_click('id','com.bugua.fight:id/jgznewpic_content','long_pass')
        #发送到微信
        self.ElementCheck.share_picture_weixin()
    def now_picture_longpass_pengyouquan(self):
        #点击发现
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/home_pic')
        self.ElementCheck.check_assertTrue(result,msg='发现按钮Fail')
        #点击新图
        self.d.find_element_by_id('com.bugua.fight:id/new_pic_tv').click()
        #随机长按图片
        self.ElementCheck.random_click('id','com.bugua.fight:id/jgznewpic_content','long_pass')
        #发送到朋友圈
        self.ElementCheck.share_picture_pengyouquan()
    def now_picture_longpass_renren(self):
        #点击发现
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/home_pic')
        self.ElementCheck.check_assertTrue(result,msg='发现按钮Fail')
        #点击新图
        self.d.find_element_by_id('com.bugua.fight:id/new_pic_tv').click()
        #随机长按图片
        self.ElementCheck.random_click('id','com.bugua.fight:id/jgznewpic_content','long_pass')
        #单击直接发送按钮
        self.d.find_element_by_id('com.bugua.fight:id/btn_send').click()
        #发送到人人
        self.d.find_element_by_name('人人').click()
        result = self.ElementCheck.existence('name','下一步')
        self.ElementCheck.check_assertTrue(result,msg='点击人人失败')
        self.d.back()
    def now_picture_longpass_momo(self):
        #点击发现
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/home_pic')
        self.ElementCheck.check_assertTrue(result,msg='发现按钮Fail')
        #点击新图
        self.d.find_element_by_id('com.bugua.fight:id/new_pic_tv').click()
        #随机长按图片
        self.ElementCheck.random_click('id','com.bugua.fight:id/jgznewpic_content','long_pass')
        #发送到陌陌
        self.ElementCheck.share_picture_momo()
    #关注页面单击图片
    def recommend_share_click_QQ(self):
        #点击发现
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/home_pic')
        self.ElementCheck.check_assertTrue(result,msg='发现按钮Fail')
        #点击关注
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/focus_tv')
        self.ElementCheck.check_assertTrue(result,msg='关注集合页面Fail')
        #点击用户推荐
        result = self.ElementCheck.click_change('name','用户推荐')
        self.ElementCheck.check_assertTrue(result,msg='用户推荐页面Fail')
        #获取第一个用户的名字
        user_name = self.ElementCheck.attribute_name('xpath', '//android.support.v7.widget.RecyclerView/\
                                                 android.widget.LinearLayout[2]/\
                                                 android.widget.LinearLayout[1]/\
                                                 android.widget.LinearLayout[1]/\
                                                 android.widget.TextView[1]')
        self.ElementCheck.click_change('ides','com.bugua.fight:id/followBtn[0]')
        #检查关注
        self.d.back()
        #下拉刷新页面
        size = self.d.get_window_size()
        width = size['width']
        height = size['height']
        self.d.swipe(width*280/1080, height*500/1776, width*280/1080, height*1500/1776)
        self.ElementCheck.random_click('id','com.bugua.fight:id/pic')
        #分享到QQ
        self.ElementCheck.share_picture_QQ()
        #取消对用户的关注
        self.d.back()
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/my_pic')
        self.ElementCheck.check_assertTrue(result,msg='进入我的页面失败')
        result = self.ElementCheck.click_jump('name','关注')
        self.ElementCheck.check_assertTrue(result,msg='进入关注页面失败')
        result = self.ElementCheck.existence('name', user_name)
        self.ElementCheck.check_assertTrue(result,msg='未发现关注的推荐用户')
        result = self.ElementCheck.click_jump('name','已关注','name','关注')
        self.ElementCheck.check_assertTrue(result,msg='已关注按钮失败')
        self.d.back()
        time.sleep(2)
        self.d.find_element_by_name('关注').click()
        result = self.ElementCheck.existence('name', user_name)
        self.assertFalse(result, msg='发现关注的推荐用户')
    def recommend_share_click_kongjian(self):
        #点击发现
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/home_pic')
        self.ElementCheck.check_assertTrue(result,msg='发现按钮Fail')
        #点击关注
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/focus_tv')
        self.ElementCheck.check_assertTrue(result,msg='关注集合页面Fail')
        #点击用户推荐
        result = self.ElementCheck.click_change('name','用户推荐')
        self.ElementCheck.check_assertTrue(result,msg='用户推荐页面Fail')
        #获取第一个腿甲用户的名字
        user_name = self.ElementCheck.attribute_name('xpath', '//android.support.v7.widget.RecyclerView/\
                                                 android.widget.LinearLayout[2]/\
                                                 android.widget.LinearLayout[1]/\
                                                 android.widget.LinearLayout[1]/\
                                                 android.widget.TextView[1]')
        self.ElementCheck.click_change('ides','com.bugua.fight:id/followBtn[0]')
        #检查关注
        self.d.back()
        #下拉刷新页面
        size = self.d.get_window_size()
        width = size['width']
        height = size['height']
        self.d.swipe(width*280/1080, height*500/1776, width*280/1080, height*1500/1776)
        self.ElementCheck.random_click('id','com.bugua.fight:id/pic')
        #发送到QQ空间
        self.ElementCheck.share_picture_kongjian()
        #取消对用户的关注
        self.d.back()
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/my_pic')
        self.ElementCheck.check_assertTrue(result,msg='进入我的页面失败')
        result = self.ElementCheck.click_jump('name','关注')
        self.ElementCheck.check_assertTrue(result,msg='进入关注页面失败')
        result = self.ElementCheck.existence('name', user_name)
        self.ElementCheck.check_assertTrue(result,msg='未发现关注的推荐用户')
        result = self.ElementCheck.click_jump('name','已关注','name','关注')
        self.ElementCheck.check_assertTrue(result,msg='已关注按钮失败')
        self.d.back()
        time.sleep(2)
        self.d.find_element_by_name('关注').click()
        result = self.ElementCheck.existence('name', user_name)
        self.assertFalse(result, msg='发现关注的推荐用户')
    def recommend_share_click_weixin(self):
        #点击发现
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/home_pic')
        self.ElementCheck.check_assertTrue(result,msg='发现按钮Fail')
        #点击关注
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/focus_tv')
        self.ElementCheck.check_assertTrue(result,msg='关注集合页面Fail')
        #点击用户推荐
        result = self.ElementCheck.click_change('name','用户推荐')
        self.ElementCheck.check_assertTrue(result,msg='用户推荐页面Fail')
        #获取第一个腿甲用户的名字
        user_name = self.ElementCheck.attribute_name('xpath', '//android.support.v7.widget.RecyclerView/\
                                                 android.widget.LinearLayout[2]/\
                                                 android.widget.LinearLayout[1]/\
                                                 android.widget.LinearLayout[1]/\
                                                 android.widget.TextView[1]')
        self.ElementCheck.click_change('ides','com.bugua.fight:id/followBtn[0]')
        #检查关注
        self.d.back()
        #下拉刷新页面
        size = self.d.get_window_size()
        width = size['width']
        height = size['height']
        self.d.swipe(width*280/1080, height*500/1776, width*280/1080, height*1500/1776)
        self.ElementCheck.random_click('id','com.bugua.fight:id/pic')
        #发送到微信
        self.ElementCheck.share_picture_weixin()
        #取消对用户的关注
        self.d.back()
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/my_pic')
        self.ElementCheck.check_assertTrue(result,msg='进入我的页面失败')
        result = self.ElementCheck.click_jump('name','关注')
        self.ElementCheck.check_assertTrue(result,msg='进入关注页面失败')
        result = self.ElementCheck.existence('name', user_name)
        self.ElementCheck.check_assertTrue(result,msg='未发现关注的推荐用户')
        result = self.ElementCheck.click_jump('name','已关注','name','关注')
        self.ElementCheck.check_assertTrue(result,msg='已关注按钮失败')
        self.d.back()
        time.sleep(2)
        self.d.find_element_by_name('关注').click()
        result = self.ElementCheck.existence('name', user_name)
        self.assertFalse(result, msg='发现关注的推荐用户')
    def recommend_share_click_pengyouquan(self):
        #点击发现
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/home_pic')
        self.ElementCheck.check_assertTrue(result,msg='发现按钮Fail')
        #点击关注
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/focus_tv')
        self.ElementCheck.check_assertTrue(result,msg='关注集合页面Fail')
        #点击用户推荐
        result = self.ElementCheck.click_change('name','用户推荐')
        self.ElementCheck.check_assertTrue(result,msg='用户推荐页面Fail')
        #获取第一个腿甲用户的名字
        user_name = self.ElementCheck.attribute_name('xpath', '//android.support.v7.widget.RecyclerView/\
                                                 android.widget.LinearLayout[2]/\
                                                 android.widget.LinearLayout[1]/\
                                                 android.widget.LinearLayout[1]/\
                                                 android.widget.TextView[1]')
        self.ElementCheck.click_change('ides','com.bugua.fight:id/followBtn[0]')
        #检查关注
        self.d.back()
        #下拉刷新页面
        size = self.d.get_window_size()
        width = size['width']
        height = size['height']
        self.d.swipe(width*280/1080, height*500/1776, width*280/1080, height*1500/1776)
        self.ElementCheck.random_click('id','com.bugua.fight:id/pic')
        #发送到朋友圈
        self.ElementCheck.share_picture_pengyouquan()
        #取消对用户的关注
        self.d.back()
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/my_pic')
        self.ElementCheck.check_assertTrue(result,msg='进入我的页面失败')
        result = self.ElementCheck.click_jump('name','关注')
        self.ElementCheck.check_assertTrue(result,msg='进入关注页面失败')
        result = self.ElementCheck.existence('name', user_name)
        self.ElementCheck.check_assertTrue(result,msg='未发现关注的推荐用户')
        result = self.ElementCheck.click_jump('name','已关注','name','关注')
        self.ElementCheck.check_assertTrue(result,msg='已关注按钮失败')
        self.d.back()
        time.sleep(2)
        self.d.find_element_by_name('关注').click()
        result = self.ElementCheck.existence('name', user_name)
        self.assertFalse(result, msg='发现关注的推荐用户')
    def recommend_share_click_renren(self):
        #点击发现
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/home_pic')
        self.ElementCheck.check_assertTrue(result,msg='发现按钮Fail')
        #点击关注
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/focus_tv')
        self.ElementCheck.check_assertTrue(result,msg='关注集合页面Fail')
        #点击用户推荐
        result = self.ElementCheck.click_change('name','用户推荐')
        self.ElementCheck.check_assertTrue(result,msg='用户推荐页面Fail')
        #获取第一个腿甲用户的名字
        user_name = self.ElementCheck.attribute_name('xpath', '//android.support.v7.widget.RecyclerView/\
                                                 android.widget.LinearLayout[2]/\
                                                 android.widget.LinearLayout[1]/\
                                                 android.widget.LinearLayout[1]/\
                                                 android.widget.TextView[1]')
        self.ElementCheck.click_change('ides','com.bugua.fight:id/followBtn[0]')
        #检查关注
        self.d.back()
        #下拉刷新页面
        size = self.d.get_window_size()
        width = size['width']
        height = size['height']
        self.d.swipe(width*280/1080, height*500/1776, width*280/1080, height*1500/1776)
        self.ElementCheck.random_click('id','com.bugua.fight:id/pic')
        #发送到人人
        self.ElementCheck.share_picture_renren()
        #取消对用户的关注
        self.d.back()
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/my_pic')
        self.ElementCheck.check_assertTrue(result,msg='进入我的页面失败')
        result = self.ElementCheck.click_jump('name','关注')
        self.ElementCheck.check_assertTrue(result,msg='进入关注页面失败')
        result = self.ElementCheck.existence('name', user_name)
        self.ElementCheck.check_assertTrue(result,msg='未发现关注的推荐用户')
        result = self.ElementCheck.click_jump('name','已关注','name','关注')
        self.ElementCheck.check_assertTrue(result,msg='已关注按钮失败')
        self.d.back()
        time.sleep(2)
        self.d.find_element_by_name('关注').click()
        result = self.ElementCheck.existence('name', user_name)
        self.assertFalse(result, msg='发现关注的推荐用户')
    # def recommend_share_click_momo(self):
    #     #点击发现
    #     result = self.ElementCheck.click_change('id','com.bugua.fight:id/home_pic')
    #     self.ElementCheck.check_assertTrue(result,msg='发现按钮Fail')
    #     #点击关注
    #     result = self.ElementCheck.click_change('id','com.bugua.fight:id/focus_tv')
    #     self.ElementCheck.check_assertTrue(result,msg='关注集合页面Fail')
    #     #点击用户推荐
    #     result = self.ElementCheck.click_change('name','用户推荐')
    #     self.ElementCheck.check_assertTrue(result,msg='用户推荐页面Fail')
    #     #获取第一个腿甲用户的名字
    #     user_name = self.ElementCheck.attribute_name('xpath', '//android.support.v7.widget.RecyclerView/\
    #                                              android.widget.LinearLayout[2]/\
    #                                              android.widget.LinearLayout[1]/\
    #                                              android.widget.LinearLayout[1]/\
    #                                              android.widget.TextView[1]')
    #     self.ElementCheck.click_change('ides','com.bugua.fight:id/followBtn[0]')
    #     #检查关注
    #     self.d.back()
    #     #下拉刷新页面
    #     size = self.d.get_window_size()
    #     width = size['width']
    #     height = size['height']
    #     self.d.swipe(width*280/1080, height*500/1776, width*280/1080, height*1500/1776)
    #     self.ElementCheck.random_click('id','com.bugua.fight:id/pic')
    #     #发送到陌陌
    #     self.ElementCheck.share_picture_momo()
    #     #取消对用户的关注
    #     self.d.back()
    #     result = self.ElementCheck.click_change('id','com.bugua.fight:id/my_pic')
    #     self.ElementCheck.check_assertTrue(result,msg='进入我的页面失败')
    #     result = self.ElementCheck.click_jump('name','关注')
    #     self.ElementCheck.check_assertTrue(result,msg='进入关注页面失败')
    #     result = self.ElementCheck.existence('name', user_name)
    #     self.ElementCheck.check_assertTrue(result,msg='未发现关注的推荐用户')
    #     result = self.ElementCheck.click_jump('name','已关注','name','关注')
    #     self.ElementCheck.check_assertTrue(result,msg='已关注按钮失败')
    #     self.d.back()
    #     time.sleep(2)
    #     self.d.find_element_by_name('关注').click()
    #     result = self.ElementCheck.existence('name', user_name)
    #     self.assertFalse(result, msg='发现关注的推荐用户')
    # 关注页面长按图片
    def recommend_share_longpass_QQ(self):
        #点击发现
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/home_pic')
        self.ElementCheck.check_assertTrue(result,msg='发现按钮Fail')
        #点击关注
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/focus_tv')
        self.ElementCheck.check_assertTrue(result,msg='关注集合页面Fail')
        #点击用户推荐
        result = self.ElementCheck.click_change('name','用户推荐')
        self.ElementCheck.check_assertTrue(result,msg='用户推荐页面Fail')
        #获取第一个用户的名字
        user_name = self.ElementCheck.attribute_name('xpath', '//android.support.v7.widget.RecyclerView/\
                                                 android.widget.LinearLayout[2]/\
                                                 android.widget.LinearLayout[1]/\
                                                 android.widget.LinearLayout[1]/\
                                                 android.widget.TextView[1]')
        self.ElementCheck.click_change('ides','com.bugua.fight:id/followBtn[0]')
        #检查关注
        self.d.back()
        #下拉刷新页面
        size = self.d.get_window_size()
        width = size['width']
        height = size['height']
        self.d.swipe(width*280/1080, height*500/1776, width*280/1080, height*1500/1776)
        self.ElementCheck.random_click('id','com.bugua.fight:id/pic','long_pass')
        #分享到QQ
        self.ElementCheck.share_picture_QQ()
        #取消对用户的关注
        self.d.back()
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/my_pic')
        self.ElementCheck.check_assertTrue(result,msg='进入我的页面失败')
        result = self.ElementCheck.click_jump('name','关注')
        self.ElementCheck.check_assertTrue(result,msg='进入关注页面失败')
        result = self.ElementCheck.existence('name', user_name)
        self.ElementCheck.check_assertTrue(result,msg='未发现关注的推荐用户')
        result = self.ElementCheck.click_jump('name','已关注','name','关注')
        self.ElementCheck.check_assertTrue(result,msg='已关注按钮失败')
        self.d.back()
        time.sleep(2)
        self.d.find_element_by_name('关注').click()
        result = self.ElementCheck.existence('name', user_name)
        self.assertFalse(result, msg='发现关注的推荐用户')
    def recommend_share_longpass_kongjian(self):
        #点击发现
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/home_pic')
        self.ElementCheck.check_assertTrue(result,msg='发现按钮Fail')
        #点击关注
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/focus_tv')
        self.ElementCheck.check_assertTrue(result,msg='关注集合页面Fail')
        #点击用户推荐
        result = self.ElementCheck.click_change('name','用户推荐')
        self.ElementCheck.check_assertTrue(result,msg='用户推荐页面Fail')
        #获取第一个腿甲用户的名字
        user_name = self.ElementCheck.attribute_name('xpath', '//android.support.v7.widget.RecyclerView/\
                                                 android.widget.LinearLayout[2]/\
                                                 android.widget.LinearLayout[1]/\
                                                 android.widget.LinearLayout[1]/\
                                                 android.widget.TextView[1]')
        self.ElementCheck.click_change('ides','com.bugua.fight:id/followBtn[0]')
        #检查关注
        self.d.back()
        #下拉刷新页面
        size = self.d.get_window_size()
        width = size['width']
        height = size['height']
        self.d.swipe(width*280/1080, height*500/1776, width*280/1080, height*1500/1776)
        self.ElementCheck.random_click('id','com.bugua.fight:id/pic','long_pass')
        #发送到QQ空间
        self.ElementCheck.share_picture_kongjian()
        #取消对用户的关注
        self.d.back()
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/my_pic')
        self.ElementCheck.check_assertTrue(result,msg='进入我的页面失败')
        result = self.ElementCheck.click_jump('name','关注')
        self.ElementCheck.check_assertTrue(result,msg='进入关注页面失败')
        result = self.ElementCheck.existence('name', user_name)
        self.ElementCheck.check_assertTrue(result,msg='未发现关注的推荐用户')
        result = self.ElementCheck.click_jump('name','已关注','name','关注')
        self.ElementCheck.check_assertTrue(result,msg='已关注按钮失败')
        self.d.back()
        time.sleep(2)
        self.d.find_element_by_name('关注').click()
        result = self.ElementCheck.existence('name', user_name)
        self.assertFalse(result, msg='发现关注的推荐用户')
    def recommend_share_longpass_weixin(self):
        #点击发现
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/home_pic')
        self.ElementCheck.check_assertTrue(result,msg='发现按钮Fail')
        #点击关注
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/focus_tv')
        self.ElementCheck.check_assertTrue(result,msg='关注集合页面Fail')
        #点击用户推荐
        result = self.ElementCheck.click_change('name','用户推荐')
        self.ElementCheck.check_assertTrue(result,msg='用户推荐页面Fail')
        #获取第一个腿甲用户的名字
        user_name = self.ElementCheck.attribute_name('xpath', '//android.support.v7.widget.RecyclerView/\
                                                 android.widget.LinearLayout[2]/\
                                                 android.widget.LinearLayout[1]/\
                                                 android.widget.LinearLayout[1]/\
                                                 android.widget.TextView[1]')
        self.ElementCheck.click_change('ides','com.bugua.fight:id/followBtn[0]','long_pass')
        #检查关注
        self.d.back()
        #下拉刷新页面
        size = self.d.get_window_size()
        width = size['width']
        height = size['height']
        self.d.swipe(width*280/1080, height*500/1776, width*280/1080, height*1500/1776)
        self.ElementCheck.random_click('id','com.bugua.fight:id/pic')
        #发送到微信
        self.ElementCheck.share_picture_weixin()
        #取消对用户的关注
        self.d.back()
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/my_pic')
        self.ElementCheck.check_assertTrue(result,msg='进入我的页面失败')
        result = self.ElementCheck.click_jump('name','关注')
        self.ElementCheck.check_assertTrue(result,msg='进入关注页面失败')
        result = self.ElementCheck.existence('name', user_name)
        self.ElementCheck.check_assertTrue(result,msg='未发现关注的推荐用户')
        result = self.ElementCheck.click_jump('name','已关注','name','关注')
        self.ElementCheck.check_assertTrue(result,msg='已关注按钮失败')
        self.d.back()
        time.sleep(2)
        self.d.find_element_by_name('关注').click()
        result = self.ElementCheck.existence('name', user_name)
        self.assertFalse(result, msg='发现关注的推荐用户')
    def recommend_share_longpass_pengyouquan(self):
        #点击发现
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/home_pic')
        self.ElementCheck.check_assertTrue(result,msg='发现按钮Fail')
        #点击关注
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/focus_tv')
        self.ElementCheck.check_assertTrue(result,msg='关注集合页面Fail')
        #点击用户推荐
        result = self.ElementCheck.click_change('name','用户推荐')
        self.ElementCheck.check_assertTrue(result,msg='用户推荐页面Fail')
        #获取第一个腿甲用户的名字
        user_name = self.ElementCheck.attribute_name('xpath', '//android.support.v7.widget.RecyclerView/\
                                                 android.widget.LinearLayout[2]/\
                                                 android.widget.LinearLayout[1]/\
                                                 android.widget.LinearLayout[1]/\
                                                 android.widget.TextView[1]')
        self.ElementCheck.click_change('ides','com.bugua.fight:id/followBtn[0]','long_pass')
        #检查关注
        self.d.back()
        #下拉刷新页面
        size = self.d.get_window_size()
        width = size['width']
        height = size['height']
        self.d.swipe(width*280/1080, height*500/1776, width*280/1080, height*1500/1776)
        self.ElementCheck.random_click('id','com.bugua.fight:id/pic')
        #发送到朋友圈
        self.ElementCheck.share_picture_pengyouquan()
        #取消对用户的关注
        self.d.back()
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/my_pic')
        self.ElementCheck.check_assertTrue(result,msg='进入我的页面失败')
        result = self.ElementCheck.click_jump('name','关注')
        self.ElementCheck.check_assertTrue(result,msg='进入关注页面失败')
        result = self.ElementCheck.existence('name', user_name)
        self.ElementCheck.check_assertTrue(result,msg='未发现关注的推荐用户')
        result = self.ElementCheck.click_jump('name','已关注','name','关注')
        self.ElementCheck.check_assertTrue(result,msg='已关注按钮失败')
        self.d.back()
        time.sleep(2)
        self.d.find_element_by_name('关注').click()
        result = self.ElementCheck.existence('name', user_name)
        self.assertFalse(result, msg='发现关注的推荐用户')
    def recommend_share_longpass_renren(self):
        #点击发现
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/home_pic')
        self.ElementCheck.check_assertTrue(result,msg='发现按钮Fail')
        #点击关注
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/focus_tv')
        self.ElementCheck.check_assertTrue(result,msg='关注集合页面Fail')
        #点击用户推荐
        result = self.ElementCheck.click_change('name','用户推荐')
        self.ElementCheck.check_assertTrue(result,msg='用户推荐页面Fail')
        #获取第一个腿甲用户的名字
        user_name = self.ElementCheck.attribute_name('xpath', '//android.support.v7.widget.RecyclerView/\
                                                 android.widget.LinearLayout[2]/\
                                                 android.widget.LinearLayout[1]/\
                                                 android.widget.LinearLayout[1]/\
                                                 android.widget.TextView[1]')
        self.ElementCheck.click_change('ides','com.bugua.fight:id/followBtn[0]','long_pass')
        #检查关注
        self.d.back()
        #下拉刷新页面
        size = self.d.get_window_size()
        width = size['width']
        height = size['height']
        self.d.swipe(width*280/1080, height*500/1776, width*280/1080, height*1500/1776)
        self.ElementCheck.random_click('id','com.bugua.fight:id/pic')
        #发送到人人
        self.ElementCheck.share_picture_renren()
        #取消对用户的关注
        self.d.back()
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/my_pic')
        self.ElementCheck.check_assertTrue(result,msg='进入我的页面失败')
        result = self.ElementCheck.click_jump('name','关注')
        self.ElementCheck.check_assertTrue(result,msg='进入关注页面失败')
        result = self.ElementCheck.existence('name', user_name)
        self.ElementCheck.check_assertTrue(result,msg='未发现关注的推荐用户')
        result = self.ElementCheck.click_jump('name','已关注','name','关注')
        self.ElementCheck.check_assertTrue(result,msg='已关注按钮失败')
        self.d.back()
        time.sleep(2)
        self.d.find_element_by_name('关注').click()
        result = self.ElementCheck.existence('name', user_name)
        self.assertFalse(result, msg='发现关注的推荐用户')
    # def recommend_share_longpass_momo(self):
    #     #点击发现
    #     result = self.ElementCheck.click_change('id','com.bugua.fight:id/home_pic')
    #     self.ElementCheck.check_assertTrue(result,msg='发现按钮Fail')
    #     #点击关注
    #     result = self.ElementCheck.click_change('id','com.bugua.fight:id/focus_tv')
    #     self.ElementCheck.check_assertTrue(result,msg='关注集合页面Fail')
    #     #点击用户推荐
    #     result = self.ElementCheck.click_change('name','用户推荐')
    #     self.ElementCheck.check_assertTrue(result,msg='用户推荐页面Fail')
    #     #获取第一个腿甲用户的名字
    #     user_name = self.ElementCheck.attribute_name('xpath', '//android.support.v7.widget.RecyclerView/\
    #                                              android.widget.LinearLayout[2]/\
    #                                              android.widget.LinearLayout[1]/\
    #                                              android.widget.LinearLayout[1]/\
    #                                              android.widget.TextView[1]')
    #     self.ElementCheck.click_change('ides','com.bugua.fight:id/followBtn[0]','long_pass')
    #     #检查关注
    #     self.d.back()
    #     #下拉刷新页面
    #     size = self.d.get_window_size()
    #     width = size['width']
    #     height = size['height']
    #     self.d.swipe(width*280/1080, height*500/1776, width*280/1080, height*1500/1776)
    #     self.ElementCheck.random_click('id','com.bugua.fight:id/pic')
    #     #发送到陌陌
    #     self.ElementCheck.share_picture_momo()
    #     #取消对用户的关注
    #     self.d.back()
    #     result = self.ElementCheck.click_change('id','com.bugua.fight:id/my_pic')
    #     self.ElementCheck.check_assertTrue(result,msg='进入我的页面失败')
    #     result = self.ElementCheck.click_jump('name','关注')
    #     self.ElementCheck.check_assertTrue(result,msg='进入关注页面失败')
    #     result = self.ElementCheck.existence('name', user_name)
    #     self.ElementCheck.check_assertTrue(result,msg='未发现关注的推荐用户')
    #     result = self.ElementCheck.click_jump('name','已关注','name','关注')
    #     self.ElementCheck.check_assertTrue(result,msg='已关注按钮失败')
    #     self.d.back()
    #     time.sleep(2)
    #     self.d.find_element_by_name('关注').click()
    #     result = self.ElementCheck.existence('name', user_name)
    #     self.assertFalse(result, msg='发现关注的推荐用户')
    #分类单击图片发送
    def class_h5_share_QQ(self):
        #点击分类
        self.d.find_element_by_id('com.bugua.fight:id/classify_pic').click()
        #点击一个表情包
        self.ElementCheck.random_click('id','com.bugua.fight:id/pkg_title')
        #h5分享QQ
        self.ElementCheck.share_package_QQ()
    def class_h5_share_kongjian(self):
        #点击分类
        self.d.find_element_by_id('com.bugua.fight:id/classify_pic').click()
        #点击一个表情包
        self.ElementCheck.random_click('id','com.bugua.fight:id/pkg_title')
        #H5分享QQ空间
        self.ElementCheck.share_package_kongjian()
    def class_h5_share_weixin(self):
        #点击分类
        self.d.find_element_by_id('com.bugua.fight:id/classify_pic').click()
        #点击一个表情包
        self.ElementCheck.random_click('id','com.bugua.fight:id/pkg_title')
        #H5分享到微信
        self.ElementCheck.share_package_weixin()
    def class_h5_share_pengyouquan(self):
        #点击分类
        self.d.find_element_by_id('com.bugua.fight:id/classify_pic').click()
        #点击一个表情包
        self.ElementCheck.random_click('id','com.bugua.fight:id/pkg_title')
        #H5分享朋友圈
        self.ElementCheck.share_package_pengyouquan()
    def class_h5_share_renren(self):
        #点击分类
        self.d.find_element_by_id('com.bugua.fight:id/classify_pic').click()
        #点击一个表情包
        self.ElementCheck.random_click('id','com.bugua.fight:id/pkg_title')
        #H5分享人人
        self.ElementCheck.share_package_renren()
    #推荐的表情包分享
    def package_h5_share_QQ(self):
        #点击发现
        self.ElementCheck.click_change('id','com.bugua.fight:id/home_pic')
        time.sleep(2)
        #点击关注
        self.ElementCheck.click_change('id','com.bugua.fight:id/focus_tv')
        time.sleep(2)
        #点击表情包推荐
        self.ElementCheck.click_jump('name','表情包推荐')
        time.sleep(2)
        #随机点击表情包
        self.ElementCheck.random_click('class','android.widget.ImageView')
        time.sleep(2)
        #h5分享QQ
        self.ElementCheck.share_package_QQ()
    def package_h5_share_kongjian(self):
        #点击发现
        self.ElementCheck.click_change('id','com.bugua.fight:id/home_pic')
        time.sleep(2)
        #点击关注
        self.ElementCheck.click_change('id','com.bugua.fight:id/focus_tv')
        time.sleep(2)
        #点击表情包推荐
        self.ElementCheck.click_jump('name','表情包推荐')
        time.sleep(2)
        #随机点击表情包
        self.ElementCheck.random_click('class','android.widget.ImageView')
        time.sleep(2)
        #H5分享QQ空间
        self.ElementCheck.share_package_kongjian()
    def package_h5_share_weixin(self):
        #点击发现
        self.ElementCheck.click_change('id','com.bugua.fight:id/home_pic')
        time.sleep(2)
        #点击关注
        self.ElementCheck.click_change('id','com.bugua.fight:id/focus_tv')
        time.sleep(2)
        #点击表情包推荐
        self.ElementCheck.click_jump('name','表情包推荐')
        time.sleep(2)
        #随机点击表情包
        self.ElementCheck.random_click('class','android.widget.ImageView')
        time.sleep(2)
        #H5分享到微信
        self.ElementCheck.share_package_weixin()
    def package_h5_share_pengyouquan(self):
        #点击发现
        self.ElementCheck.click_change('id','com.bugua.fight:id/home_pic')
        time.sleep(2)
        #点击关注
        self.ElementCheck.click_change('id','com.bugua.fight:id/focus_tv')
        time.sleep(2)
        #点击表情包推荐
        self.ElementCheck.click_jump('name','表情包推荐')
        time.sleep(2)
        #随机点击表情包
        self.ElementCheck.random_click('class','android.widget.ImageView')
        time.sleep(2)
        #H5分享朋友圈
        self.ElementCheck.share_package_pengyouquan()
    def package_h5_share_renren(self):
        #点击发现
        self.ElementCheck.click_change('id','com.bugua.fight:id/home_pic')
        time.sleep(2)
        #点击关注
        self.ElementCheck.click_change('id','com.bugua.fight:id/focus_tv')
        time.sleep(2)
        #点击表情包推荐
        self.ElementCheck.click_jump('name','表情包推荐')
        time.sleep(2)
        #随机点击表情包
        self.ElementCheck.random_click('class','android.widget.ImageView')
        time.sleep(2)
        #H5分享人人
        self.ElementCheck.share_package_renren()
    #改图结果分享
    def chang_picture_share_qq(self):
        #点击制图
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/zhitu_pic')
        self.ElementCheck.check_assertTrue(result,msg='制图按钮失灵，进入制图页面失败')
        #点击更多
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/more_tv')
        self.ElementCheck.check_assertTrue(result,msg='点击更多失败')
        #点击改图
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/edit_pic','name','图片')
        self.ElementCheck.check_assertTrue(result,msg='进入改图选图页面失败')
        #随机选择图片
        self.ElementCheck.random_click('id','com.bugua.fight:id/pic_select')
        #对文字输入框内输入内容
        time.sleep(1)
        self.d.find_element_by_class_name('android.widget.EditText').clear()
        self.d.find_element_by_class_name('android.widget.EditText').send_keys('bugua')
        #点击保存/分享
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/btn_next','id','com.bugua.fight:id/btn_finish')
        self.ElementCheck.check_assertTrue(result,msg='保存/分享Fail')
        #QQ分享
        #self.d.find_element_by_id('com.bugua.fight:id/share_to_qq').click()
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/share_to_qq','name','QQ空间')
        self.ElementCheck.check_assertTrue(result,msg='分享到QQ，QQ启动Fail')
        time.sleep(2)
        self.d.find_element_by_name('狗中极品').click()
        #点击发送
        time.sleep(2)
        self.d.find_element_by_id('com.tencent.mobileqq:id/dialogRightBtn').click()
        time.sleep(5)
        try:
            self.d.find_element_by_name('返回斗图神器').click()
        except:
            self.d.find_element_by_name('返回斗图神器_测试版').click()
    def chang_picture_share_kongjian (self):
        #点击制图
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/zhitu_pic')
        self.ElementCheck.check_assertTrue(result,msg='制图按钮失灵，进入制图页面失败')
        #点击更多
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/more_tv')
        self.ElementCheck.check_assertTrue(result,msg='点击更多失败')
        #点击改图
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/edit_pic','name','图片')
        self.ElementCheck.check_assertTrue(result,msg='进入改图选图页面失败')
        #随机选择图片
        self.ElementCheck.random_click('id','com.bugua.fight:id/pic_select')
        #对文字输入框内输入内容
        time.sleep(1)
        self.d.find_element_by_class_name('android.widget.EditText').clear()
        self.d.find_element_by_class_name('android.widget.EditText').send_keys('bugua')
        #点击保存/分享
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/btn_next','id','com.bugua.fight:id/btn_finish')
        self.ElementCheck.check_assertTrue(result,msg='保存/分享Fail')
        #分享到空间
        #self.d.find_element_by_id('com.bugua.fight:id/share_to_qzone').click()
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/share_to_qzone','name','QQ空间')
        self.ElementCheck.check_assertTrue(result,msg='分享到QQ空间，QQ启动Fail')
        time.sleep(2)
        #发送到QQ空间
        self.d.find_element_by_name('QQ空间').click()
        #点击发送
        time.sleep(2)
        self.d.find_element_by_id('com.tencent.mobileqq:id/dialogRightBtn').click()
        #点击返回斗图神器
        time.sleep(5)
        try:
            self.d.find_element_by_name('返回斗图神器').click()
        except:
            self.d.find_element_by_name('返回斗图神器_测试版').click()
    def chang_picture_share_weixin(self):
        #点击制图
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/zhitu_pic')
        self.ElementCheck.check_assertTrue(result,msg='制图按钮失灵，进入制图页面失败')
        #点击更多
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/more_tv')
        self.ElementCheck.check_assertTrue(result,msg='点击更多失败')
        #点击改图
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/edit_pic','name','图片')
        self.ElementCheck.check_assertTrue(result,msg='进入改图选图页面失败')
        #随机选择图片
        self.ElementCheck.random_click('id','com.bugua.fight:id/pic_select')
        #对文字输入框内输入内容
        time.sleep(1)
        self.d.find_element_by_class_name('android.widget.EditText').clear()
        self.d.find_element_by_class_name('android.widget.EditText').send_keys('bugua')
        #点击保存/分享
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/btn_next','id','com.bugua.fight:id/btn_finish')
        self.ElementCheck.check_assertTrue(result,msg='保存/分享Fail')
        #分享到微信
        #self.d.find_element_by_id('com.bugua.fight:id/share_to_wechat').click()
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/share_to_wechat','name','选择')
        self.ElementCheck.check_assertTrue(result,msg='分享到微信，微信启动Fail')
        time.sleep(2)
        #发送给管昭
        self.d.find_element_by_name('管昭').click()
        time.sleep(2)
        self.d.find_element_by_id('com.tencent.mm:id/bhe').click()
        time.sleep(1)
        self.d.find_element_by_id('com.tencent.mm:id/a7b').click()
    def chang_picture_share_pengyouquan(self):
        #点击制图
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/zhitu_pic')
        self.ElementCheck.check_assertTrue(result,msg='制图按钮失灵，进入制图页面失败')
        #点击更多
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/more_tv')
        self.ElementCheck.check_assertTrue(result,msg='点击更多失败')
        #点击改图
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/edit_pic','name','图片')
        self.ElementCheck.check_assertTrue(result,msg='进入改图选图页面失败')
        #随机选择图片
        self.ElementCheck.random_click('id','com.bugua.fight:id/pic_select')
        #对文字输入框内输入内容
        time.sleep(1)
        self.d.find_element_by_class_name('android.widget.EditText').clear()
        self.d.find_element_by_class_name('android.widget.EditText').send_keys('bugua')
        #点击保存/分享
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/btn_next','id','com.bugua.fight:id/btn_finish')
        self.ElementCheck.check_assertTrue(result,msg='保存/分享Fail')
        #分享到朋友圈
        #self.d.find_element_by_id('com.bugua.fight:id/share_to_moments').click()
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/share_to_moments','name','发送')
        self.ElementCheck.check_assertTrue(result,msg='分享到朋友圈，微信启动Fail')
        #点击发送
        time.sleep(2)
        self.d.find_element_by_name('发送').click()
    #制图模板分享
    def template_picture_share_QQ(self):
        #点击制图
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/zhitu_pic','id','com.bugua.fight:id/fight_tv')
        self.ElementCheck.check_assertTrue(result,msg='制图按钮失灵，进入制图页面失败')
        #在制图页面下选择一个模板
        self.ElementCheck.random_click('xpath','//android.support.v7.widget.RecyclerView/android.widget.FrameLayout')
        #文字输入框
        self.d.find_element_by_id('com.bugua.fight:id/et_text').click()
        #点击清空按钮
        self.d.find_element_by_id('com.bugua.fight:id/btn_clean').click()
        #输入内容(利用adb命令输入）
        os.system('adb shell input text bugua')
        #保存/分享
        self.ElementCheck.click_jump('id','com.bugua.fight:id/btn_next','name','完成')
        #self.d.find_element_by_id('com.bugua.fight:id/btn_next').click()
        #QQ分享
        #self.d.find_element_by_id('com.bugua.fight:id/share_to_qq').click()
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/share_to_qq','name','QQ空间')
        self.ElementCheck.check_assertTrue(result,msg='分享到QQ，QQ启动Fail')
        time.sleep(2)
        self.d.find_element_by_name('狗中极品').click()
        #点击发送
        time.sleep(2)
        self.d.find_element_by_id('com.tencent.mobileqq:id/dialogRightBtn').click()
        time.sleep(5)
        try:
            self.d.find_element_by_name('返回斗图神器').click()
        except:
            self.d.find_element_by_name('返回斗图神器_测试版').click()
    def template_picture_share_kongjian(self):
        #点击制图
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/zhitu_pic','id','com.bugua.fight:id/fight_tv')
        self.ElementCheck.check_assertTrue(result,msg='制图按钮失灵，进入制图页面失败')
        #在制图页面下选择一个模板
        self.ElementCheck.random_click('xpath','//android.support.v7.widget.RecyclerView/android.widget.FrameLayout')
        #文字输入框
        self.d.find_element_by_id('com.bugua.fight:id/et_text').click()
        #点击清空按钮
        self.d.find_element_by_id('com.bugua.fight:id/btn_clean').click()
        #输入内容(利用adb命令输入）
        os.system('adb shell input text bugua')
        #保存/分享
        self.ElementCheck.click_jump('id','com.bugua.fight:id/btn_next','name','完成')
        #self.d.find_element_by_id('com.bugua.fight:id/btn_next').click()
        #分享到空间
        #self.d.find_element_by_id('com.bugua.fight:id/share_to_qzone').click()
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/share_to_qzone','name','QQ空间')
        self.ElementCheck.check_assertTrue(result,msg='分享到QQ空间，QQ启动Fail')
        time.sleep(2)
        #发送到QQ空间
        self.d.find_element_by_name('QQ空间').click()
        #点击发送
        time.sleep(2)
        self.d.find_element_by_id('com.tencent.mobileqq:id/dialogRightBtn').click()
        #点击返回斗图神器
        time.sleep(5)
        try:
            self.d.find_element_by_name('返回斗图神器').click()
        except:
            self.d.find_element_by_name('返回斗图神器_测试版').click()
    def template_picture_share_weixin(self):
        #点击制图
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/zhitu_pic','id','com.bugua.fight:id/fight_tv')
        self.ElementCheck.check_assertTrue(result,msg='制图按钮失灵，进入制图页面失败')
        #在制图页面下选择一个模板
        self.ElementCheck.random_click('xpath','//android.support.v7.widget.RecyclerView/android.widget.FrameLayout')
        #文字输入框
        self.d.find_element_by_id('com.bugua.fight:id/et_text').click()
        #点击清空按钮
        self.d.find_element_by_id('com.bugua.fight:id/btn_clean').click()
        #输入内容(利用adb命令输入）
        os.system('adb shell input text bugua')
        #保存/分享
        self.ElementCheck.click_jump('id','com.bugua.fight:id/btn_next','name','完成')
        #self.d.find_element_by_id('com.bugua.fight:id/btn_next').click()
        #分享到微信
        #self.d.find_element_by_id('com.bugua.fight:id/share_to_wechat').click()
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/share_to_wechat','name','选择')
        self.ElementCheck.check_assertTrue(result,msg='分享到微信，微信启动Fail')
        time.sleep(2)
        #发送给管昭
        self.d.find_element_by_name('管昭').click()
        time.sleep(2)
        self.d.find_element_by_id('com.tencent.mm:id/bhe').click()
        time.sleep(1)
        self.d.find_element_by_id('com.tencent.mm:id/a7b').click()
    def template_picture_share_pengyouquan(self):
        #点击制图
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/zhitu_pic','id','com.bugua.fight:id/fight_tv')
        self.ElementCheck.check_assertTrue(result,msg='制图按钮失灵，进入制图页面失败')
        #在制图页面下选择一个模板
        self.ElementCheck.random_click('xpath','//android.support.v7.widget.RecyclerView/android.widget.FrameLayout')
        #文字输入框
        self.d.find_element_by_id('com.bugua.fight:id/et_text').click()
        #点击清空按钮
        self.d.find_element_by_id('com.bugua.fight:id/btn_clean').click()
        #输入内容(利用adb命令输入）
        os.system('adb shell input text bugua')
        #保存/分享
        self.ElementCheck.click_jump('id','com.bugua.fight:id/btn_next','name','完成')
        #self.d.find_element_by_id('com.bugua.fight:id/btn_next').click()
        #分享到朋友圈
        #self.d.find_element_by_id('com.bugua.fight:id/share_to_moments').click()
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/share_to_moments','name','发送')
        self.ElementCheck.check_assertTrue(result,msg='分享到朋友圈，微信启动Fail')
        #点击发送
        time.sleep(2)
        self.d.find_element_by_name('发送').click()
    #装逼模板分享
    def zhuangbi_share_QQ(self):
        #点击制图
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/zhitu_pic')
        self.ElementCheck.check_assertTrue(result,msg='制图按钮失灵，进入制图页面失败')
        #点击装b区
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/show_off_tv')
        self.ElementCheck.check_assertTrue(result,msg='进入装b区Fail')
        time.sleep(3)
        #点击一个分区
        a = {'1':'表白','2':'恶搞','3':'红包','4':'证书','5':'游戏','6':'炫富'}
        no = str(random.choice(range(1,5)))
        location =str( '//android.widget.TextView[@text="%s"]/..' % a[no])
        print(location)
        self.ElementCheck.click('xpath',location)
        #选择模板
        time.sleep(2)
        self.ElementCheck.random_click('xpath','//android.widget.ImageView')
        time.sleep(5)
        # #随机点击今日新上中的图
        # temlpe = 'com.bugua.fight:id/template'+'%d'% (random.choice(range(0,2)))
        # self.d.find_element_by_id(temlpe).click()
        # time.sleep(3)
        #下拉屏幕到低端
        size = self.d.get_window_size()
        w = size['width']
        h = size['height']
        self.d.swipe(w*500/1080,h*1800/1920,w*500/1080,h*100/1920)
        #寻找图片添加按钮
        try:
            view = self.d.find_elements_by_id('com.bugua.fight:id/pic_add_view')
            for i in range(len(view)):
                view[i].click()
                time.sleep(0.5)
                self.ElementCheck.random_click('id','com.android.documentsui:id/icon_thumb')
                time.sleep(0.5)
                self.d.find_element_by_id('com.bugua.fight:id/cut_btn').click()
        except:
            pass
        try:
            text = self.d.find_elements_by_id('com.bugua.fight:id/cool_input_et')
            for i in range(len(text)):
                text[i].send_keys('bugua')
        except:
            pass
        time.sleep(0.5)
        self.ElementCheck.click_jump('id','com.bugua.fight:id/template_make','id','com.bugua.fight:id/btn_finish')
        #QQ分享
        #self.d.find_element_by_id('com.bugua.fight:id/share_to_qq').click()
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/share_to_qq','name','QQ空间')
        self.ElementCheck.check_assertTrue(result,msg='分享到QQ，QQ启动Fail')
        time.sleep(2)
        self.d.find_element_by_name('狗中极品').click()
        #点击发送
        time.sleep(2)
        self.d.find_element_by_id('com.tencent.mobileqq:id/dialogRightBtn').click()
        time.sleep(5)
        try:
            self.d.find_element_by_name('返回斗图神器').click()
        except:
            self.d.find_element_by_name('返回斗图神器_测试版').click()
    def zhuangbi_share_kongjian(self):
        #点击制图
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/zhitu_pic')
        self.ElementCheck.check_assertTrue(result,msg='制图按钮失灵，进入制图页面失败')
        #点击装b区
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/show_off_tv')
        self.ElementCheck.check_assertTrue(result,msg='进入装b区Fail')
        time.sleep(3)
        #点击一个分区
        a = {'1':'表白','2':'恶搞','3':'红包','4':'证书','5':'游戏','6':'炫富'}
        no = str(random.choice(range(1,5)))
        location =str( '//android.widget.TextView[@text="%s"]/..' % a[no])
        print(location)
        self.ElementCheck.click('xpath',location)
        #选择模板
        time.sleep(2)
        self.ElementCheck.random_click('xpath','//android.widget.ImageView')
        time.sleep(5)
        # #随机点击今日新上中的图
        # temlpe = 'com.bugua.fight:id/template'+'%d'% (random.choice(range(0,2)))
        # self.d.find_element_by_id(temlpe).click()
        # time.sleep(3)
        #下拉屏幕到低端
        size = self.d.get_window_size()
        w = size['width']
        h = size['height']
        self.d.swipe(w*500/1080,h*1800/1920,w*500/1080,h*100/1920)
        #寻找图片添加按钮
        try:
            view = self.d.find_elements_by_id('com.bugua.fight:id/pic_add_view')
            for i in range(len(view)):
                view[i].click()
                time.sleep(0.5)
                self.ElementCheck.random_click('id','com.android.documentsui:id/icon_thumb')
                time.sleep(0.5)
                self.d.find_element_by_id('com.bugua.fight:id/cut_btn').click()
        except:
            pass
        try:
            text = self.d.find_elements_by_id('com.bugua.fight:id/cool_input_et')
            
            for i in range(len(text)):
                text[i].send_keys('bugua')
        except:
            pass
        time.sleep(0.5)
        self.ElementCheck.click_jump('id','com.bugua.fight:id/template_make','id','com.bugua.fight:id/btn_finish')
        #分享到空间
        #self.d.find_element_by_id('com.bugua.fight:id/share_to_qzone').click()
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/share_to_qzone','name','QQ空间')
        self.ElementCheck.check_assertTrue(result,msg='分享到QQ空间，QQ启动成功')
        time.sleep(2)
        #发送到QQ空间
        self.d.find_element_by_name('QQ空间').click()
        #点击发送
        time.sleep(2)
        self.d.find_element_by_id('com.tencent.mobileqq:id/dialogRightBtn').click()
        #点击返回斗图神器
        time.sleep(5)
        try:
            self.d.find_element_by_name('返回斗图神器').click()
        except:
            self.d.find_element_by_name('返回斗图神器_测试版').click()
    def zhuangbi_share_weixin(self):
        #点击制图
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/zhitu_pic')
        self.ElementCheck.check_assertTrue(result,msg='制图按钮失灵，进入制图页面失败')
        #点击装b区
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/show_off_tv')
        self.ElementCheck.check_assertTrue(result,msg='进入装b区Fail')
        time.sleep(3)
        #点击一个分区
        a = {'1':'表白','2':'恶搞','3':'红包','4':'证书','5':'游戏','6':'炫富'}
        no = str(random.choice(range(1,5)))
        location =str( '//android.widget.TextView[@text="%s"]/..' % a[no])
        print(location)
        self.ElementCheck.click('xpath',location)
        #选择模板
        time.sleep(2)
        self.ElementCheck.random_click('xpath','//android.widget.ImageView')
        time.sleep(5)
        # #随机点击今日新上中的图
        # temlpe = 'com.bugua.fight:id/template'+'%d'% (random.choice(range(0,2)))
        # self.d.find_element_by_id(temlpe).click()
        # time.sleep(3)
        #下拉屏幕到低端
        size = self.d.get_window_size()
        w = size['width']
        h = size['height']
        self.d.swipe(w*500/1080,h*1800/1920,w*500/1080,h*100/1920)
        #寻找图片添加按钮
        try:
            view = self.d.find_elements_by_id('com.bugua.fight:id/pic_add_view')
            for i in range(len(view)):
                view[i].click()
                time.sleep(0.5)
                self.ElementCheck.random_click('id','com.android.documentsui:id/icon_thumb')
                time.sleep(0.5)
                self.d.find_element_by_id('com.bugua.fight:id/cut_btn').click()
        except:
            pass
        try:
            text = self.d.find_elements_by_id('com.bugua.fight:id/cool_input_et')
            print(len(text))
            for i in range(len(text)):
                text[i].send_keys('bugua')
        except:
            pass
        time.sleep(0.5)
        self.ElementCheck.click_jump('id','com.bugua.fight:id/template_make','id','com.bugua.fight:id/btn_finish')
        #分享到微信
        #self.d.find_element_by_id('com.bugua.fight:id/share_to_wechat').click()
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/share_to_wechat','name','选择')
        self.ElementCheck.check_assertTrue(result,msg='分享到微信，微信启动Fail')
        time.sleep(2)
        #发送给管昭
        self.d.find_element_by_name('管昭').click()
        time.sleep(2)
        self.d.find_element_by_id('com.tencent.mm:id/bhe').click()
        time.sleep(1)
        self.d.find_element_by_id('com.tencent.mm:id/a7b').click()
    def zhuangbi_share_pengyouquan(self):
        #点击制图
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/zhitu_pic')
        self.ElementCheck.check_assertTrue(result,msg='制图按钮失灵，进入制图页面失败')
        #点击装b区
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/show_off_tv')
        self.ElementCheck.check_assertTrue(result,msg='进入装b区Fail')
        time.sleep(3)
        #点击一个分区
        a = {'1':'表白','2':'恶搞','3':'红包','4':'证书','5':'游戏','6':'炫富'}
        no = str(random.choice(range(1,5)))
        location =str( '//android.widget.TextView[@text="%s"]/..' % a[no])
        print(location)
        self.ElementCheck.click('xpath',location)
        #选择模板
        time.sleep(2)
        self.ElementCheck.random_click('xpath','//android.widget.ImageView')
        time.sleep(5)
        # #随机点击今日新上中的图
        # temlpe = 'com.bugua.fight:id/template'+'%d'% (random.choice(range(0,2)))
        # self.d.find_element_by_id(temlpe).click()
        # time.sleep(3)
        #下拉屏幕到低端
        size = self.d.get_window_size()
        w = size['width']
        h = size['height']
        self.d.swipe(w*500/1080,h*1800/1920,w*500/1080,h*100/1920)
        #寻找图片添加按钮
        try:
            view = self.d.find_elements_by_id('com.bugua.fight:id/pic_add_view')
            for i in range(len(view)):
                view[i].click()
                time.sleep(0.5)
                self.ElementCheck.random_click('id','com.android.documentsui:id/icon_thumb')
                time.sleep(0.5)
                self.d.find_element_by_id('com.bugua.fight:id/cut_btn').click()
        except:
            pass
        try:
            text = self.d.find_elements_by_id('com.bugua.fight:id/cool_input_et')
            print(len(text))
            for i in range(len(text)):
                text[i].send_keys('bugua')
        except:
            pass
        time.sleep(0.5)
        self.ElementCheck.click_jump('id','com.bugua.fight:id/template_make','id','com.bugua.fight:id/btn_finish')
        #分享到朋友圈
        #self.d.find_element_by_id('com.bugua.fight:id/share_to_moments').click()
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/share_to_moments','name','发送')
        self.ElementCheck.check_assertTrue(result,msg='分享到朋友圈，微信启动Fail')
        #点击发送
        time.sleep(2)
        self.d.find_element_by_name('发送').click()

if __name__=="__main__":
    #编辑用例
    suite = unittest.TestSuite()
    # suite.addTest(ShareTest('post_share_click_QQ'))
    # suite.addTest(ShareTest('post_share_click_kongjian'))
    # suite.addTest(ShareTest('post_share_click_weixin'))
    # suite.addTest(ShareTest('post_share_click_pengyouquan'))
    # suite.addTest(ShareTest('post_share_click_renren'))
    # suite.addTest(ShareTest('post_share_click_momo'))
    # suite.addTest(ShareTest('post_share_longpass_QQ'))
    # suite.addTest(ShareTest('post_share_longpass_kongjian'))
    # suite.addTest(ShareTest('post_share_longpass_weixin'))
    suite.addTest(ShareTest('post_share_longpass_pengyouquan'))
    # suite.addTest(ShareTest('post_share_longpass_renren'))
    # suite.addTest(ShareTest('post_share_longpass_momo'))
    # suite.addTest(ShareTest('theme_picture_click_QQ'))
    # suite.addTest(ShareTest('theme_picture_click_kongjian'))
    # suite.addTest(ShareTest('theme_picture_click_weixin'))
    # suite.addTest(ShareTest('theme_picture_click_pengyouquan'))
    # suite.addTest(ShareTest('theme_picture_click_renren'))
    # suite.addTest(ShareTest('theme_picture_click_momo'))
    # suite.addTest(ShareTest('theme_picture_longpass_QQ'))
    # suite.addTest(ShareTest('theme_picture_longpass_kongjian'))
    # suite.addTest(ShareTest('theme_picture_longpass_weixin'))
    # suite.addTest(ShareTest('theme_picture_longpass_pengyouquan'))
    # suite.addTest(ShareTest('theme_picture_longpass_renren'))
    # suite.addTest(ShareTest('theme_picture_longpass_momo'))
    # suite.addTest(ShareTest('now_picture_click_QQ'))
    # suite.addTest(ShareTest('now_picture_click_kongjian'))
    # suite.addTest(ShareTest('now_picture_click_weixin'))
    # suite.addTest(ShareTest('now_picture_click_pengyouquan'))
    # suite.addTest(ShareTest('now_picture_click_renren'))
    # suite.addTest(ShareTest('now_picture_click_momo'))
    # suite.addTest(ShareTest('now_picture_longpass_QQ'))
    # suite.addTest(ShareTest('now_picture_longpass_kongjian'))
    # suite.addTest(ShareTest('now_picture_longpass_weixin'))
    # suite.addTest(ShareTest('now_picture_longpass_pengyouquan'))
    # suite.addTest(ShareTest('now_picture_longpass_renren'))
    # suite.addTest(ShareTest('now_picture_longpass_momo'))
    # suite.addTest(ShareTest('recommend_share_click_QQ'))
    # suite.addTest(ShareTest('recommend_share_click_kongjian'))
    # suite.addTest(ShareTest('recommend_share_click_weixin'))
    # suite.addTest(ShareTest('recommend_share_click_pengyouquan'))
    # suite.addTest(ShareTest('recommend_share_click_renren'))
    #suite.addTest(ShareTest('recommend_share_click_momo'))#陌陌分享后有使用性问题
    # suite.addTest(ShareTest('recommend_share_longpass_QQ'))
    # suite.addTest(ShareTest('recommend_share_longpass_kongjian'))
    # suite.addTest(ShareTest('recommend_share_longpass_weixin'))
    # suite.addTest(ShareTest('recommend_share_longpass_pengyouquan'))
    # suite.addTest(ShareTest('recommend_share_longpass_renren'))
    # suite.addTest(ShareTest('recommend_share_longpass_momo'))
    # suite.addTest(ShareTest('class_h5_share_QQ'))
    # suite.addTest(ShareTest('class_h5_share_kongjian'))
    # suite.addTest(ShareTest('class_h5_share_weixin'))
    # suite.addTest(ShareTest('class_h5_share_pengyouquan'))
    # suite.addTest(ShareTest('class_h5_share_renren'))
    # suite.addTest(ShareTest('package_h5_share_QQ'))
    # suite.addTest(ShareTest('package_h5_share_kongjian'))
    # suite.addTest(ShareTest('package_h5_share_weixin'))
    # suite.addTest(ShareTest('package_h5_share_pengyouquan'))
    # suite.addTest(ShareTest('package_h5_share_renren'))
    # suite.addTest(ShareTest('chang_picture_share_qq'))
    # suite.addTest(ShareTest('chang_picture_share_kongjian'))
    # suite.addTest(ShareTest('chang_picture_share_weixin'))
    # suite.addTest(ShareTest('chang_picture_share_pengyouquan'))
    # suite.addTest(ShareTest('template_picture_share_QQ'))
    # suite.addTest(ShareTest('template_picture_share_kongjian'))
    # suite.addTest(ShareTest('template_picture_share_weixin'))
    # suite.addTest(ShareTest('template_picture_share_pengyouquan'))
    # suite.addTest(ShareTest('zhuangbi_share_QQ'))
    # suite.addTest(ShareTest('zhuangbi_share_kongjian'))
    # suite.addTest(ShareTest('zhuangbi_share_weixin'))
    # suite.addTest(ShareTest('zhuangbi_share_pengyouquan'))





    #执行用例
    runner = unittest.TextTestRunner()
    runner.run(suite)