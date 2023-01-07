# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
"""
__author__: wangxiaoxiang
"""
# ��ҳҳ��
import time
from appium.webdriver.common.mobileby import MobileBy
from BasePages.base_page import BasePage


class MainPage(BasePage):

    def goto_search(self):
        # ����������
        self.find_and_click(MobileBy.ID, "com.xueqiu.android:id/tv_search")
        from ModulesPages.search_page import SearchPage
        return SearchPage(self.driver)

    def goto_main(self):
        # ������ҳ��
        self.find_and_click(MobileBy.ID, "com.xueqiu.android:id/action_close")
        time.sleep(5)
        res = self.find(MobileBy.XPATH, "//*[@text='�ҵ�']")
        return res
