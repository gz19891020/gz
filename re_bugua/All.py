#__author__ = 'yuelian'
#-*- coding: utf-8 -*-
import unittest
from HTMLTestRunner import HTMLTestRunner
from Post_new import PostTest
from Edit_information import Edit_informationTest
from New_Drafting import DraftingTest
from Replies import RepliesTest
from Theme import ThemeTest
from New_picture import New_pictureTest
from Follow import Follow_Test
from Recommend import RecommendTest
from Suspension import Suspension_Test
from share import ShareTest

import time
import os


if __name__=="__main__":

    suite = unittest.TestSuite()
    suite.addTest(PostTest('Tv_theme_name_Test'))
    # suite.addTest(PostTest('FindPostTest'))
    # suite.addTest(PostTest('FightPostTest'))
    # suite.addTest(PostTest('DiscussPostTest'))
    suite.addTest(Edit_informationTest('HeadPortraitTest'))
    suite.addTest(Edit_informationTest('RenameTest'))
    suite.addTest(Edit_informationTest('SexTest'))
    suite.addTest(Edit_informationTest('SelfIntroductionTest'))
    suite.addTest(DraftingTest('MyProductionTest'))
    suite.addTest(DraftingTest('ChangePlanTest'))
    suite.addTest(DraftingTest('TemplateTest'))
    suite.addTest(DraftingTest('Fight_most_Test'))
    suite.addTest(DraftingTest('Fight_new_Test'))
    suite.addTest(DraftingTest('Fight_gif_Test'))
    suite.addTest(DraftingTest('Fight_popular_Test'))
    suite.addTest(DraftingTest('Classification_Test'))
    suite.addTest(DraftingTest('Page_swipe_Test'))
    suite.addTest(DraftingTest('zhuangbi_test'))
    suite.addTest(DraftingTest('losts_pic_one_click1'))
    suite.addTest(DraftingTest('losts_pic_one_click2'))
    suite.addTest(DraftingTest('text_gif_text'))
    suite.addTest(RepliesTest('EssenceTest'))
    suite.addTest(RepliesTest('PleaseTest'))
    suite.addTest(RepliesTest('All_areaTest'))
    suite.addTest(RepliesTest('post_send_box_hide'))
    suite.addTest(RepliesTest('all_area_send_box_hide'))
    suite.addTest(RepliesTest('one_click1'))
    suite.addTest(RepliesTest('one_click2'))
    suite.addTest(ThemeTest('Follow_Theme_Test1'))
    suite.addTest(ThemeTest('Follow_Theme_Test2'))
    suite.addTest(ThemeTest('Theme_picture1'))
    suite.addTest(ThemeTest('Theme_picture2'))
    suite.addTest(New_pictureTest('Picture1'))
    suite.addTest(New_pictureTest('Picture2'))
    suite.addTest(New_pictureTest('Top'))
    suite.addTest(Follow_Test('Follow_user1'))
    suite.addTest(Follow_Test('Follow_package1'))
    suite.addTest(RecommendTest('User_test1'))
    suite.addTest(Suspension_Test('weixin_suspension_test'))
    suite.addTest(Suspension_Test('qq_suspension_test'))
    # suite.addTest(ShareTest('post_share_click_QQ'))
    # suite.addTest(ShareTest('post_share_click_kongjian'))
    # suite.addTest(ShareTest('post_share_click_weixin'))
    # suite.addTest(ShareTest('post_share_click_pengyouquan'))
    # suite.addTest(ShareTest('post_share_click_renren'))
    # suite.addTest(ShareTest('post_share_click_momo'))
    # suite.addTest(ShareTest('post_share_longpass_QQ'))
    # suite.addTest(ShareTest('post_share_longpass_kongjian'))
    # suite.addTest(ShareTest('post_share_longpass_weixin'))
    # suite.addTest(ShareTest('post_share_longpass_pengyouquan'))
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
    # suite.addTest(ShareTest('recommend_share_click_QQ'))
    # suite.addTest(ShareTest('recommend_share_click_kongjian'))
    # suite.addTest(ShareTest('recommend_share_click_weixin'))
    # suite.addTest(ShareTest('recommend_share_click_pengyouquan'))
    # suite.addTest(ShareTest('recommend_share_click_renren'))
    # ##suite.addTest(ShareTest('recommend_share_click_momo'))#由于陌陌分享出去有特殊性暂时不适用
    # suite.addTest(ShareTest('recommend_share_longpass_QQ'))
    # suite.addTest(ShareTest('recommend_share_longpass_kongjian'))
    # suite.addTest(ShareTest('recommend_share_longpass_weixin'))
    # suite.addTest(ShareTest('recommend_share_longpass_pengyouquan'))
    # suite.addTest(ShareTest('recommend_share_longpass_renren'))
    # # suite.addTest(ShareTest('recommend_share_longpass_momo'))#由于陌陌分享出去有特殊性暂时不适用
    #直接执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    #定义自动化报告目录
    #新建当前时间文件夹
    ISOTIMEFORMAT = '%Y%m%d%X'
    localtime = str(time.strftime(ISOTIMEFORMAT, time.localtime())).replace(':', '')
    filename = 'C:\\Users\yuelian\Desktop\Automated Testing\Report\ALL_Report.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream = fp, title = '自动化测试报告' , description = '自动化测试报告')
    runner.run(suite)
    fp.close()