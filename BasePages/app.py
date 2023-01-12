# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
"""
__author__: wangxiaoxiang
"""
# ר�ŷ�app��ز���
import logging
from appium import webdriver
from BasePages.base_page import BasePage
from ModulesPages.main_page import MainPage
from Utils.yaml_info import YamlInfo


class App(BasePage):
    # ����
    def start(self, app_mul):
        data = YamlInfo.read_info(app_mul)
        if self.driver is None:
            logging.info(f"driverΪ:{self.driver}")
            # ��ʼ����������Ӧ��
            self.desired_caps = data.get('mulatorsetcaps')
            address_set = data.get('addressset')[0]

            # �ͻ��˺ͷ���˽�������
            self.driver = webdriver.Remote(address_set, self.desired_caps)
            # ��ʽ�ȴ���ÿһ�β���Ԫ�ص�ʱ�򣬶�̬����
            self.driver.implicitly_wait(40)
        else:
            # ����app
            logging.info(f"���� driver .")
            self.driver.start_activity(app_package=data['mulatorsetcaps']['appPackage'],
                                       app_activity=data['mulatorsetcaps']['appActivity'])
        return self

    # ֹͣ
    def stop(self):
        self.driver.quit()

    # ��ת��ҳ��
    def go_main(self):
        # ���
        return MainPage(self.driver)
