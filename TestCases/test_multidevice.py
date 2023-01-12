# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
"""
__author__: wangxiaoxiang
"""
import logging
import os
from BasePages.app import App


class TestContact:
    _platformName = None
    _platformVersion = None

    def setup_class(self):
        # 启动app
        self.app = App()
        self._platformName = os.getenv("name").strip('"')
        self._platformVersion = os.getenv("version").strip('"')
        logging.info(f"终端系统:{self._platformName}")
        logging.info(f"终端版本:{self._platformVersion}")

    def setup(self):
        name = self._platformName
        version = self._platformVersion
        # 判断是哪个终端系统和版本
        if name == "android" and version == "6.0.0":
            app_mul = "mum"
        elif name == "ios" and version == "7.1.2":
            app_mul = "nox"
        else:
            app_mul = "nox"
        logging.info(f"终端设备:{app_mul}")
        self.main = self.app.start(app_mul).go_main()

    def teardown_class(self):
        # 关闭app
        self.app.stop()

    def test_search(self):
        logging.info(f"进入搜索页面->输入内容")
        # 进入主页面->点击搜索框->进入搜索页面->输入搜索内容->点击取消->返回主页面
        result = self.main.goto_search().input_text().goto_main()
        assert result

    def test_search2(self):
        logging.info(f"进入搜索页面->输入内容")
        # 进入主页面->点击搜索框->进入搜索页面->输入搜索内容->点击取消->返回主页面
        result = self.main.goto_search().input_text().goto_main()
        assert result
