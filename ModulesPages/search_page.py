# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
"""
__author__: wangxiaoxiang
"""
# ����ҳ��
import time
from appium.webdriver.common.mobileby import MobileBy
from BasePages.base_page import BasePage


class SearchPage(BasePage):

    def input_text(self):
        # ��������������
        self.find_and_send(MobileBy.ID, "com.xueqiu.android:id/search_input_text", "alibaba")
        time.sleep(5)
        from ModulesPages.main_page import MainPage
        return MainPage(self.driver)
