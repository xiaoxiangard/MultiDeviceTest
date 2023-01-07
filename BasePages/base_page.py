# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
"""
__author__: wangxiaoxiang
"""
import logging
from appium.webdriver.webdriver import WebDriver


class BasePage:
    # driver: WebDriver ����м�������ע�ͣ������п�������ʹ��
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator):
        logging.info(f"��λ��:{by}, ��λ���ʽ: {locator}")
        # ����Ԫ��
        return self.driver.find_element(by, locator)

    def find_and_click(self, by, locator):
        logging.info(f"�������:")
        # �ҵ�Ԫ�ز����
        self.find(by, locator).click()

    def find_and_send(self, by, locator, text):
        logging.info(f"�������,��������Ϊ: {text}")
        # �ҵ�Ԫ�ز�����
        self.find(by, locator).send_keys(text)