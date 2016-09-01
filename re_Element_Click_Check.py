#__author__ = 'Gz'
#-*- coding: utf-8 -*-
import time
from extend import Appium_Extend
from appium.webdriver.common.touch_action import TouchAction
import os
import random
import unittest
class ElementCheck(object):

    def __init__(self, tester, driver):
        unittest.TestCase()
        self.tester = tester
        self.driver = driver
        self.Extend = Appium_Extend(driver)
    #等待元素超过多久报错,默认5S
    def wait_element(self,how,element,times=5):
        global validate
        global event
        global deadline
        deadline = 0
        while True:
            try:
                if how == 'id':
                    event = self.driver.find_element_by_id(element)
                elif how == 'name':
                    event =self.driver.find_element_by_name(element)
                elif how == 'class':
                    event = self.driver.find_element_by_class_name(element)
                elif how == 'xpath':
                    event = self.driver.find_element_by_xpath(element)
                elif how == 'classes':
                    element = element.split('[')
                    event = self.driver.find_elements_by_class_name(element[0])
                    event = event[int(element[1].split(']')[0])]
                elif how == 'ides':
                    element = element.split('[')
                    event = self.driver.find_elements_by_id(element[0])
                    event = event[int(element[1].split(']')[0])]
                validate = True
                print('找到元素，不进行等待')
                break
            except:
                time.sleep(1)
                deadline += 1
                if deadline <= times:
                    #print('等待',deadline,'秒')
                    continue
                else:
            #如果找不到元素进行截图，截图是按照当时时间来命名
            #判断如果没有指定失败图片且，同文件夹的名字为Fail_picture的文件夹新建一个
                    try:
                        os._exists(r'./Fail_picture') == False
                        os.mkdir(r'./Fail_picture')
                    except:
                        pass
                    #设置时间格式
                    ISOTIMEFORMAT='%Y%m%d_%X'
                    localtime = str(time.strftime(ISOTIMEFORMAT, time.localtime())).replace(':', '')
                    print('未找到要点击的元素页面截图为：',localtime)
                    #以时间命名截屏
                    self.driver.get_screenshot_as_file('./Fail_picture/'+ localtime +'.png')
                    #assert event, '没有找到想要获取的元素'
                    print('网络延迟，超过', times, '秒')
                    validate = False
                    break
        assert validate == True,'超过设定等待时间未发现元素'+element
        #返回一个元素
        return event
    #检查是否纯在某元素
    def existence(self, how, element):
        global validate
        global result
        global event
        global time_no
        try:
            if how == 'id':
                event = self.driver.find_element_by_id(element)
            elif how == 'name':
                event =self.driver.find_element_by_name(element)
            elif how == 'class':
                event = self.driver.find_element_by_class_name(element)
            elif how == 'xpath':
                event = self.driver.find_element_by_xpath(element)
            result = True
        except:
            #如果找不到元素进行截图，截图是按照当时时间来命名
            #判断如果没有指定失败图片且，同文件夹的名字为Fail_picture的文件夹新建一个
            try:
                os._exists(r'./Fail_picture') == False
                os.mkdir(r'./Fail_picture')
            except:
                pass
            #设置时间格式
            ISOTIMEFORMAT = '%Y%m%d_%X'
            localtime = str(time.strftime(ISOTIMEFORMAT, time.localtime())).replace(':', '')
            print('未找到想要获取的元素',element,'页面截图为：',localtime)
            #以时间来命名截屏
            self.driver.get_screenshot_as_file('./Fail_picture/'+ localtime + '.png')
            result = False
        return result
    #等待一类元素超过多久报错,默认5S
    def elements(self,how,element,times=5):
        global validate
        global event
        global deadline
        deadline = 0
        while True:
            try:
                if how == 'id':
                    event = self.driver.find_elements_by_id(element)
                elif how == 'name':
                    event =self.driver.find_elements_by_name(element)
                elif how == 'class':
                    event = self.driver.find_elements_by_class_name(element)
                elif how == 'xpath':
                    event = self.driver.find_elements_by_xpath(element)
                if len(event) > 0:
                    validate = True
                print('找到元素，不进行等待')
                break
            except:
                time.sleep(1)
                deadline += 1
                if deadline <= times:
                    #print('等待',deadline,'秒')
                    continue
                else:
            #如果找不到元素进行截图，截图是按照当时时间来命名
            #判断如果没有指定失败图片且，同文件夹的名字为Fail_picture的文件夹新建一个
                    try:
                        os._exists(r'./Fail_picture') == False
                        os.mkdir(r'./Fail_picture')
                    except:
                        pass
                    #设置时间格式
                    ISOTIMEFORMAT='%Y%m%d_%X'
                    localtime = str(time.strftime(ISOTIMEFORMAT, time.localtime())).replace(':', '')
                    print('未找到要点击的元素页面截图为：',localtime)
                    #以时间命名截屏
                    self.driver.get_screenshot_as_file('./Fail_picture/'+ localtime +'.png')
                    #assert event, '没有找到想要获取的元素'
                    print('网络延迟，超过', times, '秒')
                    validate = False
                    break
        assert validate == True,'超过设定等待时间未发现元素'+element
        #返回一个元素
        return event
    #元素检查和截图存放位置
    def click(self,how,element):
        event = self.wait_element(how,element)
        event.click()
    def click_jump(self, how1, element1, how2 = 0 , element2 = 0):
        global validate
        #点击元素1
        event1 = self.wait_element(how1,element1)
        event1.click()
        #通过一个元素是否存在对按键进行检验
        try:
            self.wait_element(how2,element2)
            return validate
        except:
            validate = False
        return validate
    #通过元素本身是否变化进行判断元素是否被点击
    def click_change(self, how, element,type='change'):
        #元素检查和截图存放位置
        global validate
        global event
         #截取元素点击前的图片
        event = self.wait_element(how,element)
        print(event)
        self.Extend.get_screenshot_by_element(event).write_to_file('./Temp', 'click_before')
        load = self.Extend.load_image('./Temp/click_before.png')
        event.click()
        if type == 'change':
            result = self.Extend.get_screenshot_by_element(event).same_as(load, 0)
            if result == False:
                validate = True
            else:
                validate = False
        #hide形式
        else:
            result = self.existence(how,element)
            if result == True:
                print('发现元素',element,'截图看是否一致')
                result_picture = self.Extend.get_screenshot_by_element(event).same_as(load, 0)
                if result_picture == False:
                    validate = True
                else:
                    validate = False
            else:
                print('隐藏元素',element,'成功')
                validate = True
        return validate
    #获取一个元素的name属性
    def attribute_name(self, how, element,same_thing='none'):
        global validate
        global result
        event = self.wait_element(how,element)
        result = event.get_attribute('name')
        if same_thing == 'none':
            pass
        else:
            if same_thing == result:
                result = True
            else:
                result = False
        return result
    #翻页随机点击表单中的同一种元素（可指定具有一定特点元素的）
    def random_click(self, how1, element1, type='click', how2=0, element2=0):
        global event
        global result
        event = self.elements(how1,element1)
        #获取屏幕分辨率
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        size = event[0].size
        if size["height"]<200:
            v_y = 200
        else:
            v_y = size["height"]
        #随机翻页并且随机选取元素
        time_no = 0
        while True:
            #翻页
            if len(event) > 1:
                for i in range(5):
                    self.driver.swipe(width*500/1080, height*1200/1766, width*500/1080, height*(1200-v_y)/1766)
                if type == 'click':
                    time.sleep(3)
                    event[random.choice(range(len(event)))].click()
                else:
                    time.sleep(3)
                    TouchAction(self.driver).long_press(event[random.choice(range(len(event)))]).wait(1).perform()
                result = True
                try:
                    if how2 == 'id':
                        event_check = self.driver.find_element_by_id(element2)
                    elif how2 == 'name':
                        event_check =self.driver.find_element_by_name(element2)
                    elif how2 == 'class':
                        event_check = self.driver.find_element_by_class_name(element2)
                    elif how2 == 'xpath':
                        event_check = self.driver.find_element_by_xpath(element2)
                    result = True
                    break
                except:
                    time_no += 1
                    self.driver.back()
                    if time_no == 20:
                        result = False
            #不翻页
            else:
                if type == 'click':
                    time.sleep(1)
                    event[random.choice(range(len(event)))].click()
                else:
                    time.sleep(1)
                    TouchAction(self.driver).long_press(event[random.choice(range(len(event)))]).wait(1).perform()
                result = True
                try:
                    if how2 == 'id':
                        event_check = self.driver.find_element_by_id(element2)
                    elif how2 == 'name':
                        event_check =self.driver.find_element_by_name(element2)
                    elif how2 == 'class':
                        event_check = self.driver.find_element_by_class_name(element2)
                    elif how2 == 'xpath':
                        event_check = self.driver.find_element_by_xpath(element2)
                    result = True
                    break
                except:
                    time_no += 1
                    self.driver.back()
                    if time_no == 20:
                        result = False
        return result
    #随机点一个元素并获取其name属性
    def random_click_get_name(self,how, element):
        events = self.elements(how,element)
        no = random.choice(range(len(events)))
        time.sleep(1)
        name = events[no].get_attribute('name')
        events[no].click()
        return name
    def random_click_get_other_name(self,how1, element1, how2, element2):
        global events1
        global events2
        events1 = self.elements(how1,element2)
        events2 = self.elements(how2,element2)
        no = random.choice(range(len(events1)))
        time.sleep(1)
        name = events2[no].get_attribute('name')
        events1[no].click()
        return name
    #逐个元素点击根据一个元素的Name属性判断是不想要点击的元素
    def reach_click(self, how1, element1, how2, element2, decide_name, *args):
        global time_no
        global event_check
        global result
        events = self.elements(how1,element1)
            #获取屏幕分辨率
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        size = event[0].size
        v_y = size["height"]
        #按照元素高度滑动并且选取第二个元素
        time_no = 0
        while True:
            self.driver.swipe(width*500/1080, height*1200/1766, width*500/1080, height*(1200-v_y)/1766)
            time.sleep(1)
            events[1].click()
            try:
                if how2 == 'id':
                    event_check = self.driver.find_element_by_id(element2)
                elif how2 == 'name':
                    event_check =self.driver.find_element_by_name(element2)
                elif how2 == 'class':
                    event_check = self.driver.find_element_by_class_name(element2)
                elif how2 == 'xpath':
                    event_check = self.driver.find_element_by_xpath(element2)
                event_check_name = event_check.get_attribute('name')
                if decide_name == 'same':
                    print('same')
                    assert event_check_name == args[0]
                else:
                    print('not same')
                    for i in args:
                        assert event_check_name != i
                result = True
                break
            except:
                time_no += 1
                self.driver.back()
                if time_no == 10:
                    result = False
                    break
        return result
    #滑动页面到下一个页面,查看元素变化
    def swipe_page_left_right(self, how, element, direction='left', type='different'):
        global validate
        global result
        global event
        global time_no
        try:
            if how == 'id':
                event = self.driver.find_element_by_id(element)
            elif how == 'name':
                event =self.driver.find_element_by_name(element)
            elif how == 'class':
                event = self.driver.find_element_by_class_name(element)
            elif how == 'xpath':
                event = self.driver.find_element_by_xpath(element)
        except:
            #如果找不到元素进行截图，截图是按照当时时间来命名
            #判断如果没有指定失败图片且，同文件夹的名字为Fail_picture的文件夹新建一个
            try:
                os._exists(r'./Fail_picture') == False
                os.mkdir(r'./Fail_picture')
            except:
                pass
            #设置时间格式
            ISOTIMEFORMAT = '%Y%m%d_%X'
            localtime = str(time.strftime(ISOTIMEFORMAT, time.localtime())).replace(':', '')
            print('未找到想要获取的元素页面截图为：',localtime)
            #以时间来命名截屏
            self.driver.get_screenshot_as_file('./Fail_picture/'+ localtime + '.png')
            result = False
        #获取屏幕分辨率
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        #滑动前判定元素截图
        self.Extend.get_screenshot_by_element(event).write_to_file('./Temp','Swipe_before')
        if direction == 'left':
            self.driver.swipe(width*1050/1080, height*500/1766, width*50/1080, height*500/1766)
        else:
            self.driver.swipe(width*50/1080, height*500/1766, width*1050/1080, height*500/1766)
        load = self.Extend.load_image('./Temp/Swipe_before.png')
        self.Extend.get_screenshot_by_element(event).write_to_file('./Temp','Swipe_after')
        result = self.Extend.get_screenshot_by_element(event).same_as(load, 0)
        if type=='different':
            if result == False:
                return True
            else:
                return False
        else:
            return result
    #滑动后元素是否隐藏
    def swipe_existence(self, how, element):
        global validate
        global result
        global event
        global time_no
        event = self.wait_element(how,element)
        #获取屏幕分辨率
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        self.Extend.get_screenshot_by_element(event).write_to_file('./Temp','Swipe_existence')
        #获取屏幕分辨率
        self.driver.swipe(width*500/1080, height*500/1766, width*500/1080, height*1000/1766)
        load = self.Extend.load_image('./Temp/Swipe_existence.png')
        try:
            result = self.Extend.get_screenshot_by_element(event).same_as(load, 0)
        except:
            result = False
        if result == False:
            result = True
        else:
            result = False
        return result
    #结果为真错误截图
    def check_assertTrue(self,exper,msg):
        if exper != True:
            try:
                os._exists(r'./Fail_picture') == False
                os.mkdir(r'./Fail_picture')
            except:
                pass
            #设置时间格式
            ISOTIMEFORMAT = '%Y%m%d_%X'
            localtime = str(time.strftime(ISOTIMEFORMAT, time.localtime())).replace(':', '')
            print('结果错误截图为：',localtime)
            #以时间来命名截屏
            self.driver.get_screenshot_as_file('./Fail_picture/'+ localtime + '.png')
        self.tester.assertTrue(exper, msg)
    #结果为假错误截图
    def check_assertFalse(self,exper,msg):
        if exper != False:
            try:
                os._exists(r'./Fail_picture') == False
                os.mkdir(r'./Fail_picture')
            except:
                pass
            #设置时间格式
            ISOTIMEFORMAT = '%Y%m%d_%X'
            localtime = str(time.strftime(ISOTIMEFORMAT, time.localtime())).replace(':', '')
            print('结果错误截图为：',localtime)
            #以时间来命名截屏
            self.driver.get_screenshot_as_file('./Fail_picture/'+ localtime + '.png')
        self.tester.assertFalse(exper, msg)
    #分享图片
    def share_picture_QQ(self):
        #单击直接发送按钮
        time.sleep(3)
        self.driver.find_element_by_id('com.bugua.fight:id/btn_send').click()
        #self.driver.find_element_by_name('QQ好友').click()
        time.sleep(2)
        #发送到QQ
        self.driver.find_element_by_name('QQ').click()
        time.sleep(2)
        self.driver.find_element_by_name('狗中极品').click()
        #点击发送
        time.sleep(2)
        self.driver.find_element_by_id('com.tencent.mobileqq:id/dialogRightBtn').click()
        time.sleep(5)
        try:
            self.driver.find_element_by_name('返回斗图神器').click()
        except:
            self.driver.find_element_by_name('返回斗图神器_测试版').click()
    def share_picture_kongjian(self):
        #单击直接发送按钮
        time.sleep(3)
        self.driver.find_element_by_id('com.bugua.fight:id/btn_send').click()
        time.sleep(2)
        #发送到QQ空间
        self.driver.find_element_by_name('QQ空间').click()
        time.sleep(2)
        #发送到QQ空间
        self.driver.find_element_by_name('QQ空间').click()
        #点击发送
        time.sleep(2)
        self.driver.find_element_by_id('com.tencent.mobileqq:id/dialogRightBtn').click()
        #点击返回斗图神器
        time.sleep(5)
        try:
            self.driver.find_element_by_name('返回斗图神器').click()
        except:
            self.driver.find_element_by_name('返回斗图神器_测试版').click()
    def share_picture_weixin(self):
        #单击直接发送按钮
        self.driver.find_element_by_id('com.bugua.fight:id/btn_send').click()
        time.sleep(2)
        # #临时没有微信号办法
        # self.driver.find_element_by_name('登录微信')
        #发送到微信
        self.driver.find_element_by_name('微信').click()
        time.sleep(2)
        #发送给管昭
        self.driver.find_element_by_name('管昭').click()
        time.sleep(2)
        self.driver.find_element_by_name('分享').click()
        time.sleep(1)
        self.driver.find_element_by_id('com.tencent.mm:id/a7m').click()
    def share_picture_pengyouquan(self):
        #单击直接发送按钮
        self.driver.find_element_by_id('com.bugua.fight:id/btn_send').click()
        time.sleep(2)
        # #临时没有微信号办法
        # self.driver.find_element_by_name('登录微信')
        #发送到朋友圈
        self.driver.find_element_by_name('朋友圈').click()
        #点击发送
        time.sleep(2)
        self.driver.find_element_by_name('发送').click()
    def share_picture_renren(self):
        #单击直接发送按钮
        self.driver.find_element_by_id('com.bugua.fight:id/btn_send').click()
        #发送到人人
        time.sleep(2)
        self.driver.find_element_by_name('人人').click()
    def share_picture_momo(self):
        #单击直接发送按钮
        self.driver.find_element_by_id('com.bugua.fight:id/btn_send').click()
        time.sleep(2)
        #发送到陌陌
        self.driver.find_element_by_name('陌陌').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.immomo.momo:id/signeditor_tv_text').send_keys('bugua')
        try:
            os._exists(r'./result') == False
            os.mkdir(r'./result')
        except:
            pass
        #设置时间格式
        ISOTIMEFORMAT = '%Y%m%d_%X'
        localtime = str(time.strftime(ISOTIMEFORMAT, time.localtime())).replace(':', '')
        print('结果错误截图为：',localtime)
        #以时间来命名截屏
        self.driver.get_screenshot_as_file('./result/momo'+ localtime + '.png')
        self.driver.back()
        self.driver.find_element_by_name('确认').click()
    def share_package_QQ(self):
        #H5分享
        try:
            self.driver.find_element_by_id('com.bugua.fight:id/btn_share').click()
        except:
            self.driver.find_element_by_name('分享表情包').click()
        time.sleep(2)
        #发送到QQ
        self.driver.find_element_by_name('QQ').click()
        time.sleep(2)
        #发送给狗中极品
        self.driver.find_element_by_name('狗中极品').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.tencent.mobileqq:id/dialogRightBtn').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.tencent.mobileqq:id/dialogLeftBtn').click()
    def share_package_kongjian(self):
        #H5分享
        try:
            self.driver.find_element_by_id('com.bugua.fight:id/btn_share').click()
        except:
            self.driver.find_element_by_name('分享表情包').click()
        time.sleep(2)
        #发送到QQ空间
        self.driver.find_element_by_name('QQ空间').click()
        time.sleep(2)
        #选择QQ空间
        self.driver.find_element_by_name('QQ空间').click()
        time.sleep(2)
        #H5分享
        self.driver.find_element_by_id('com.tencent.mobileqq:id/ivTitleBtnRightText').click()
    def share_package_weixin(self):
        #H5分享
        try:
            self.driver.find_element_by_id('com.bugua.fight:id/btn_share').click()
        except:
            self.driver.find_element_by_name('分享表情包').click()
        time.sleep(2)
        # #临时没有微信号办法
        # self.driver.find_element_by_name('登录微信')
        #发送到微信
        self.driver.find_element_by_name('微信').click()
        time.sleep(2)
        #发送给管昭
        self.driver.find_element_by_name('管昭').click()
        time.sleep(2)
        #点击分享
        self.driver.find_element_by_name('分享').click()
        time.sleep(2)
        #返回斗图神器
        self.driver.find_element_by_id('com.tencent.mm:id/a7m').click()
    def share_package_pengyouquan(self):
        #H5分享
        try:
            self.driver.find_element_by_id('com.bugua.fight:id/btn_share').click()
        except:
            self.driver.find_element_by_name('分享表情包').click()
        time.sleep(2)
        # #临时没有微信号办法
        # self.driver.find_element_by_name('登录微信')
        #发送到朋友圈
        self.driver.find_element_by_name('朋友圈').click()
        time.sleep(2)
        #点击发送
        self.driver.find_element_by_id('com.tencent.mm:id/eg').click()
    def share_package_renren(self):
        #H5分享
        try:
            self.driver.find_element_by_id('com.bugua.fight:id/btn_share').click()
        except:
            self.driver.find_element_by_name('分享表情包').click()
        time.sleep(2)
        #发送到人人
        self.driver.find_element_by_name('人人').click()
    #获取当前元素与指定元素进行图片对比
    def cintrast_element_picture(self,how,element,picture):
        #元素检查和截图存放位置
        global validate
        global result
        global event
        try:
            if how == 'id':
                event = self.driver.find_element_by_id(element)
            elif how == 'name':
                event =self.driver.find_element_by_name(element)
            elif how == 'class':
                event = self.driver.find_element_by_class_name(element)
            elif how == 'xpath':
                event = self.driver.find_element_by_xpath(element)
            elif how == 'classes':
                element = element.split('[')
                event = self.driver.find_elements_by_class_name(element[0])
                event = event[int(element[1].split(']')[0])]
            elif how == 'ides':
                element1 = element.split('[')
                event = self.driver.find_elements_by_id(element[0])
                event = event[int(element[1].split(']')[0])]
            #检查是否有Temp文件夹没有就新建一个
            try:
                os._exists(r'./Temp') == False
                os.mkdir(r'./Temp')
            except:
                pass
            #截取元素点击前的图片
            self.Extend.get_screenshot_by_element(event).write_to_file('./Temp', 'click_before')
        except:
            #如果找不到元素进行截图，截图是按照当时时间来命名
            #判断如果没有指定失败图片且，同文件夹的名字为Fail_picture的文件夹新建一个
            try:
                os._exists(r'./Fail_picture') == False
                os.mkdir(r'./Fail_picture')
            except:
                pass
            #设置时间格式
            ISOTIMEFORMAT = '%Y%m%d_%X'
            localtime = str(time.strftime(ISOTIMEFORMAT, time.localtime())).replace(':', '')
            print('未找到要点击的元素页面截图为：',localtime)
            #以时间来命名截屏
            self.driver.get_screenshot_as_file('./Fail_picture/'+ localtime + '.png')
            #assert event, '没有找到想要获取的元素'
            result = False
        load = self.Extend.load_image(picture)
        result = self.Extend.get_screenshot_by_element(event).same_as(load,0)
        return result
    #修改版
    #获取某元素的图片
    # def element_picture(self,how,element):
    #     event = self.wait_element(how,element)
    #     self.Extend.get_screenshot_by_element(event).write_to_file('./Temp', 'element')
    #     load = self.Extend.load_image('./Temp/element.png')
    #     return load
    #获取当前元素与指定元素截图进行图片对比
    # def cintrast_element_picture(self,how,element,load):
    #     #元素检查和截图存放位置
    #     global result
    #     event = self.wait_element(how,element)
    #     self.Extend.get_screenshot_by_element(event).write_to_file('./Temp', 'click_before')
    #     result = self.Extend.get_screenshot_by_element(event).same_as(load,0)
    #     return result








