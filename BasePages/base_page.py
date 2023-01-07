# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
"""
__author__: wangxiaoxiang
"""
import logging
from appium.webdriver.webdriver import WebDriver


class BasePage:
    # driver: WebDriver 入参中加入类型注释，方法中可以正常使用
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator):
        logging.info(f"定位符:{by}, 定位表达式: {locator}")
        # 查找元素
        return self.driver.find_element(by, locator)

    def find_and_click(self, by, locator):
        logging.info(f"点击操作:")
        # 找到元素并点击
        self.find(by, locator).click()

    def find_and_send(self, by, locator, text):
        logging.info(f"输入操作,输入内容为: {text}")
        # 找到元素并输入
        self.find(by, locator).send_keys(text)