# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
"""
__author__: wangxiaoxiang
"""
import logging
from BasePages.app import App


class TestContact:

    def setup_class(self):
        # 启动app
        self.app = App()

    def setup(self):
        self.main = self.app.start().go_main()

    def teardown_class(self):
        # 关闭app
        self.app.stop()

    def test_search(self):
        logging.info(f"进入搜索页面输入内容")
        # 进入主页面->点击搜索框->进入搜索页面->输入搜索内容->点击取消->返回主页面
        result = self.main.goto_search().input_text().goto_main()
        assert result

    def test_search2(self):
        logging.info(f"进入搜索页面输入内容")
        # 进入主页面->点击搜索框->进入搜索页面->输入搜索内容->点击取消->返回主页面
        result = self.main.goto_search().input_text().goto_main()
        assert result
