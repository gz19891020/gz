#__author__ = 'gz'
#-*- coding: utf-8 -*-

from appium import webdriver
import time
import unittest
import random
from appium.webdriver.common.touch_action import TouchAction
from extend import Appium_Extend
from Element_Click_Check import ElementCheck
from HTMLTestRunner import HTMLTestRunner
import  os


class DraftingTest(unittest.TestCase):

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
        self.extnd = Appium_Extend(self.d)
        self.ElementCheck = ElementCheck(self, self.d)
        time.sleep(5)

    def tearDown(self):
        print('Test end')
        self.d.quit()

    #def Fight_souch_Test(self):

    def Fight_most_Test(self):
        """制图使用最多页面"""
        #点击制图
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/zhitu_pic','id','com.bugua.fight:id/fight_tv')
        self.ElementCheck.check_assertTrue(result,msg='制图按钮失灵，进入制图页面失败')
        #点击使用最多
        result = self.ElementCheck.click_jump('name', '使用最多', 'name', '使用最多')
        self.ElementCheck.check_assertTrue(result,msg='进入制图页面失败')

    def Fight_new_Test(self):
        """制图最近模板页面"""
        #点击制图
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/zhitu_pic','id','com.bugua.fight:id/fight_tv')
        self.ElementCheck.check_assertTrue(result,msg='制图按钮失灵，进入制图页面失败')
        #点击最新模板
        result = self.ElementCheck.click_jump('name', '最新模板', 'name', '最新模板')
        self.ElementCheck.check_assertTrue(result,msg='进入制图页面失败')

    def Fight_gif_Test(self):
        """制图动态模板页面"""
        #点击制图
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/zhitu_pic','id','com.bugua.fight:id/fight_tv')
        self.ElementCheck.check_assertTrue(result,msg='制图按钮失灵，进入制图页面失败')
        #点击动态模板
        result = self.ElementCheck.click_jump('name', '动态模板', 'name', '动态模板')
        self.ElementCheck.check_assertTrue(result,msg='进入制图页面失败')
        #点击最热
        #获取最热和最新两个tab切换按钮
        result = self.ElementCheck.click_change('classes','android.support.v7.app.ActionBar$Tab[1]')
        self.ElementCheck.check_assertTrue(result, msg='最热点击后无反应')
        #点击最新
        #获取最热和最新两个tab切换按钮
        result = self.ElementCheck.click_change('classes','android.support.v7.app.ActionBar$Tab[0]')
        self.ElementCheck.check_assertTrue(result, msg='最新点击后无反应')

    def Fight_popular_Test(self):
        """制图当前流行页面"""
        #点击制图
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/zhitu_pic','id','com.bugua.fight:id/fight_tv')
        self.ElementCheck.check_assertTrue(result,msg='制图按钮失灵，进入制图页面失败')
        #点击当前流行
        result = self.ElementCheck.click_jump('name','当前流行')
        self.ElementCheck.check_assertTrue(result, msg='当前流行点击后无反应')

    def Classification_Test(self):
        """分类页面"""
        #点击制图
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/zhitu_pic','id','com.bugua.fight:id/fight_tv')
        self.ElementCheck.check_assertTrue(result,msg='制图按钮失灵，进入制图页面失败')
        #点击分类
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/category_tv','id','com.bugua.fight:id/module_classify_name')
        self.ElementCheck.check_assertTrue(result,msg='制图按钮失灵，进入制图页面失败')
        #随机点击一个分类
        result = self.ElementCheck.random_click('id','com.bugua.fight:id/module_classify_card_view','name','全部')
        self.ElementCheck.check_assertTrue(result,msg='分类失败')
        #点击最新
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/new_order_detail')
        self.ElementCheck.check_assertTrue(result, msg='最新点击后无反应')
        #点击热门
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/hot_order_detail')
        self.ElementCheck.check_assertTrue(result, msg='点击热门失败')

    def Page_swipe_Test(self):
        """制图页面滑动查看"""
        #点击制图
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/zhitu_pic','id','com.bugua.fight:id/fight_tv')
        self.ElementCheck.check_assertTrue(result,msg='制图按钮失灵，进入制图页面失败')
        #向左滑动到装b区
        result = self.ElementCheck.swipe_page_left_right('id','com.bugua.fight:id/show_off_tv','left')
        self.ElementCheck.check_assertTrue(result,msg='滑动页面失败')
        #向左滑动到分类
        result = self.ElementCheck.swipe_page_left_right('id','com.bugua.fight:id/category_tv')
        self.ElementCheck.check_assertTrue(result,msg='滑动页面失败')
        #向左滑动到更多
        result = self.ElementCheck.swipe_page_left_right('id','com.bugua.fight:id/more_tv')
        self.ElementCheck.check_assertTrue(result,msg='滑动页面失败')
        #更多向左滑动
        result = self.ElementCheck.swipe_page_left_right('id','com.bugua.fight:id/more_tv','left','same')
        self.ElementCheck.check_assertTrue(result,msg='滑动页面失败')
        #向右滑动到分类
        result = self.ElementCheck.swipe_page_left_right('id','com.bugua.fight:id/category_tv','right')
        self.ElementCheck.check_assertTrue(result,msg='滑动页面失败')
        #向右滑动到装b区
        result = self.ElementCheck.swipe_page_left_right('id','com.bugua.fight:id/show_off_tv','right')
        self.ElementCheck.check_assertTrue(result,msg='滑动页面失败')
        #向右滑动到斗图区
        result = self.ElementCheck.swipe_page_left_right('id','com.bugua.fight:id/fight_tv','right')
        self.ElementCheck.check_assertTrue(result,msg='滑动页面失败')
        #斗图区向右滑动
        result = self.ElementCheck.swipe_page_left_right('id','com.bugua.fight:id/fight_tv','right','same')
        self.ElementCheck.check_assertTrue(result,msg='滑动页面失败')

    def MyProductionTest(self):
        """制图我的制作页面"""
        #点击制图
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/zhitu_pic','id','com.bugua.fight:id/fight_tv')
        self.ElementCheck.check_assertTrue(result,msg='制图按钮失灵，进入制图页面失败')
        #点击更多
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/more_tv')
        self.ElementCheck.check_assertTrue(result,msg='点击更多失败')
        #点击我的制作
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/make_folder','name','表情包详情')
        self.ElementCheck.check_assertTrue(result,msg='进入我的制作页面失败')

    def ChangePlanTest(self):
        """制图改图页面"""
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
        self.d.find_element_by_class_name('android.widget.EditText').send_keys('我们是斗图神器')
        #修改背景颜色
        try:
            os._exists(r'./result') == False
            os.mkdir(r'./result')
        except:
            pass
        #点击文字背景色
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/btn_change_bg_color','id','com.bugua.fight:id/background_options')
        self.ElementCheck.check_assertTrue( result,msg='文字背景选择框失灵')
        self.d.get_screenshot_as_file('./result/background_options.jpg')
        #选择透明背景
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/btn_bg_color_2','id','com.bugua.fight:id/icon_bg_color_2')
        self.d.get_screenshot_as_file('./result/color2.jpg')
        self.ElementCheck.check_assertTrue( result,msg='透明背景失败')
        #选择白色背景
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/btn_bg_color_1','id','com.bugua.fight:id/icon_bg_color_1')
        self.d.get_screenshot_as_file('./result/color1.jpg')
        self.ElementCheck.check_assertTrue( result,msg='白色背景失败')
        #选择吸取背景
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/btn_bg_color_3','id','com.bugua.fight:id/btn_bg_color_3')
        self.d.get_screenshot_as_file('./result/color3.jpg')
        self.ElementCheck.check_assertTrue( result,msg='白色背景失败')
        #self.d.get_screenshot_as_file('./result/color3.jpg')
        #点击坐标位置为500，300的点
        self.d.tap([(500, 300)])
        self.d.get_screenshot_as_file('./result/color4.jpg')
        #点击字体颜色
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/btn_change_txt_color','id','com.bugua.fight:id/color_pick_area')
        self.ElementCheck.check_assertTrue( result,msg='字体颜色选择框失灵')
        #点击白色
        self.d.find_element_by_xpath('//android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ImageView[1]').click()
        self.d.get_screenshot_as_file('./result/white.jpg')
        #描边
        self.d.find_element_by_id('com.bugua.fight:id/radio_stroke').click()
        self.d.get_screenshot_as_file('./result/whiteStroke.jpg')
        self.d.find_element_by_id('com.bugua.fight:id/radio_stroke').click()
        #点击黑色
        self.d.find_element_by_xpath('//android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ImageView[2]').click()
        self.d.get_screenshot_as_file('./result/black.jpg')
        #描边
        self.d.find_element_by_id('com.bugua.fight:id/radio_stroke').click()
        self.d.get_screenshot_as_file('./result/blackStroke.jpg')
        self.d.find_element_by_id('com.bugua.fight:id/radio_stroke').click()
        #点击绿色
        self.d.find_element_by_xpath('//android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ImageView[3]').click()
        self.d.get_screenshot_as_file('./result/green.jpg')
        #描边
        self.d.find_element_by_id('com.bugua.fight:id/radio_stroke').click()
        self.d.get_screenshot_as_file('./result/greenStroke.jpg')
        self.d.find_element_by_id('com.bugua.fight:id/radio_stroke').click()
        #点击橘黄
        self.d.find_element_by_xpath('//android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ImageView[4]').click()
        self.d.get_screenshot_as_file('./result/orange.jpg')
        #描边
        self.d.find_element_by_id('com.bugua.fight:id/radio_stroke').click()
        self.d.get_screenshot_as_file('./result/orangeStroke.jpg')
        self.d.find_element_by_id('com.bugua.fight:id/radio_stroke').click()
        #点击红色
        self.d.find_element_by_xpath('//android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ImageView[5]').click()
        self.d.get_screenshot_as_file('./result/red.jpg')
        #描边
        self.d.find_element_by_id('com.bugua.fight:id/radio_stroke').click()
        self.d.get_screenshot_as_file('./result/redStroke.jpg')
        self.d.find_element_by_id('com.bugua.fight:id/radio_stroke').click()
        #移动文字输入框
        size=self.d.get_window_size()
        width=size['width']
        height=size['height']
        print(width,height)
        text1=self.d.find_elements_by_class_name("android.widget.EditText")
        print(len(text1))
        TouchAction(self.d).press(text1[1]).move_to(x=width*76/768, y=height*150/1184).release().perform()
        time.sleep(5)
        self.d.find_element_by_xpath('//android.widget.EditText[1]').click()
        #关闭文字框
        #选取所有的android.widget.ImageView元素
        text=self.d.find_elements_by_xpath("//android.widget.ImageView")
        #点击第三个android.widget.ImageView元素对应为开始的文字框的关闭按钮
        text[2].click()
        self.d.get_screenshot_as_file('./result/closetext.jpg')
        #新建文字框
        self.d.find_element_by_id('com.bugua.fight:id/btn_new').click()
        self.d.get_screenshot_as_file('./result/newtext.jpg')
        #将新建的文字框输入内容
        self.d.find_element_by_xpath('//android.widget.EditText[1]').clear()
        self.d.find_element_by_xpath('//android.widget.EditText[1]').send_keys('我们是斗图神器')
        #扩大文字框
        T=self.d.find_elements_by_xpath("//android.widget.ImageView")
        #print(len(T))
        TouchAction(self.d).long_press(T[3]).move_to(x=width*900/1080 , y=height*900/1920).release().perform()
        self.d.get_screenshot_as_file('./result/bigtext.jpg')
        #保存
        self.d.find_element_by_id('com.bugua.fight:id/btn_next').click()
        time.sleep(2)
        self.d.get_screenshot_as_file('./result/change_finsh.jpg')
        #点击完成按钮
        self.d.find_element_by_name('完成').click()

    def TemplateTest(self):
        """制图斗图制图"""
        #点击制图
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/zhitu_pic')
        self.ElementCheck.check_assertTrue(result,msg='制图按钮失灵，进入制图页面失败')
        #在制图页面下选择一个模板
        self.ElementCheck.random_click('xpath','//android.support.v7.widget.RecyclerView/android.widget.FrameLayout')
        #选择热门配文
        #第一次选择配文
        content = self.ElementCheck.random_click_get_name('xpath', '//android.widget.ListView/android.widget.TextView')
        time.sleep(2)
        #检查所选择的配文显示的是否正确
        result = self.ElementCheck.attribute_name('classes','android.widget.TextView[2]', content)
        self.ElementCheck.check_assertTrue(result ,msg='显示错误')
        self.d.get_screenshot_as_file('./result/Template_text1.jpg')
        #下拉配文内容（至最低端）
        self.d.swipe(500/1080, 1800/1920, 500/1080, 1200/1920)
        content = self.ElementCheck.random_click_get_name('xpath', '//android.widget.ListView/android.widget.TextView')
        result = self.ElementCheck.attribute_name('classes','android.widget.TextView[2]', content)
        self.ElementCheck.check_assertTrue(result ,msg='显示错误')
        #文字输入框
        self.d.find_element_by_id('com.bugua.fight:id/et_text').click()
        time.sleep(2)
        self.d.get_screenshot_as_file('./result/Template_edittext.jpg')
        #点击清空按钮
        self.d.find_element_by_id('com.bugua.fight:id/btn_clean').click()
        self.d.get_screenshot_as_file('./result/Template_clear.jpg')
        #输入内容(利用adb命令输入）
        os.system('adb shell input text bugua')
        #检查输入的配文显示的是否正确
        self.d.find_element_by_xpath('//android.widget.TextView[3]').get_attribute('name')\
        == 'bugua'
        self.d.get_screenshot_as_file('./result/Template_over.jpg')
        #保存
        self.d.find_element_by_id('com.bugua.fight:id/btn_next').click()
        time.sleep(2)
        self.d.get_screenshot_as_file('./result/Template_finsh.jpg')

    def zhuangbi_test(self):
        """制图装逼模板"""
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
        #选择模板
        # #随机点击今日新上中的图
        # temlpe = 'com.bugua.fight:id/template'+'%d'% (random.choice(range(0,2)))
        # self.d.find_element_by_id(temlpe).click()
        #下拉屏幕到低端
        time.sleep(3)
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
        #结果文件夹
        try:
            os._exists(r'./result') == False
            os.mkdir(r'./result')
        except:
            pass
        self.extnd.get_screenshot_by_element(self.d.find_element_by_id('com.bugua.fight:id/image_preview')).write_to_file('./result','zhuangbi')

    def losts_pic_one_click1(self):
        """制图海量生成模板页面单击"""
        #点击制图
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/zhitu_pic')
        self.ElementCheck.check_assertTrue(result,msg='制图按钮失灵，进入制图页面失败')
        #点击更多
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/more_tv')
        self.ElementCheck.check_assertTrue(result,msg='点击更多失败')
        #点击海量生成模板
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/lots_pic_one_click','name','一键生成')
        self.ElementCheck.check_assertTrue(result,msg='进入海量生成模板失败')
        #输入文字内容
        self.d.find_element_by_id('com.bugua.fight:id/et_content').send_keys('bugua')
        #点击一键生成
        self.d.find_element_by_id('com.bugua.fight:id/one_key_btn').click()
        time.sleep(5)
        #截取生成内容图片
        try:
            os._exists(r'./Temp') == False
            os.mkdir(r'./Temp')
        except:
            pass
        picture = self.d.find_element_by_id('com.bugua.fight:id/recyclerView')
        self.extnd.get_screenshot_by_element(picture).write_to_file('./Temp', 'lost_pic')
        load = self.extnd.load_image('./Temp/lost_pic.png')
        #点击换一批
        self.d.find_element_by_name('换一批').click()
        time.sleep(5)
        #对比内容
        result = self.extnd.get_screenshot_by_element(picture).same_as(load,0)
        self.assertFalse(result,msg='换一批失败')
        #选择图片分享出去
        self.ElementCheck.random_click('xpath','//android.widget.ImageView/..')
        #点击收藏
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/btn_save')
        self.ElementCheck.check_assertTrue(result,msg='收藏按钮失败')
        #分享到微信
        self.ElementCheck.share_picture_weixin()

    def losts_pic_one_click2(self):
        """制图海量生成模板页面单击"""
        #点击制图
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/zhitu_pic')
        self.ElementCheck.check_assertTrue(result,msg='制图按钮失灵，进入制图页面失败')
        #点击更多
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/more_tv')
        self.ElementCheck.check_assertTrue(result,msg='点击更多失败')
        #点击海量生成模板
        result = self.ElementCheck.click_jump('id','com.bugua.fight:id/lots_pic_one_click','name','一键生成')
        self.ElementCheck.check_assertTrue(result,msg='进入海量生成模板失败')
        #输入文字内容
        self.d.find_element_by_id('com.bugua.fight:id/et_content').send_keys('bugua')
        #点击一键生成
        self.d.find_element_by_id('com.bugua.fight:id/one_key_btn').click()
        time.sleep(5)
        #截取生成内容图片
        try:
            os._exists(r'./Temp') == False
            os.mkdir(r'./Temp')
        except:
            pass
        picture = self.d.find_element_by_id('com.bugua.fight:id/recyclerView')
        self.extnd.get_screenshot_by_element(picture).write_to_file('./Temp', 'lost_pic')
        load = self.extnd.load_image('./Temp/lost_pic.png')
        #点击换一批
        self.d.find_element_by_name('换一批').click()
        time.sleep(5)
        #对比内容
        result = self.extnd.get_screenshot_by_element(picture).same_as(load,0)
        self.assertFalse(result,msg='换一批失败')
        #选择图片分享出去
        self.ElementCheck.random_click('xpath', '//android.widget.ImageView/..', 'long_pass')
        time.sleep(2)
        #点击收藏
        result = self.ElementCheck.click_change('id','com.bugua.fight:id/btn_star')
        self.ElementCheck.check_assertTrue(result,msg='收藏按钮失败')
        #分享到微信
        self.ElementCheck.share_picture_weixin()








if __name__=="__main__":
    #编辑用例
    suite = unittest.TestSuite()
    #suite.addTest(DraftingTest('MyProductionTest'))
    # suite.addTest(DraftingTest('ChangePlanTest'))
    # suite.addTest(DraftingTest('TemplateTest'))
    #suite.addTest(DraftingTest('Fight_most_Test'))
    #suite.addTest(DraftingTest('Fight_new_Test'))
    #suite.addTest(DraftingTest('Fight_gif_Test'))
    #suite.addTest(DraftingTest('Fight_popular_Test'))
    # suite.addTest(DraftingTest('Classification_Test'))
    #suite.addTest(DraftingTest('Page_swipe_Test'))
    # suite.addTest(DraftingTest('zhuangbi_test'))
    suite.addTest(DraftingTest('losts_pic_one_click1'))
    suite.addTest(DraftingTest('losts_pic_one_click2'))
    #执行用例
    runner = unittest.TextTestRunner()
    runner.run(suite)
    #filename = 'C:/\Users/\yuelian/\Desktop/\Automated Testing/\Report/\DraftingTest.html'
    #fp = open(filename, 'wb')
    #runner = HTMLTestRunner(stream = fp , title='自动化测试报告' , description='自动化测试报告')
    #runner.run(suite)
