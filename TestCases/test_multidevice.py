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
        # ����app
        self.app = App()
        self._platformName = os.getenv("name").strip('"')
        self._platformVersion = os.getenv("version").strip('"')
        logging.info(f"�ն�ϵͳ:{self._platformName}")
        logging.info(f"�ն˰汾:{self._platformVersion}")

    def setup(self):
        name = self._platformName
        version = self._platformVersion
        # �ж����ĸ��ն�ϵͳ�Ͱ汾
        if name == "android" and version == "6.0.0":
            app_mul = "mum"
        elif name == "ios" and version == "7.1.2":
            app_mul = "nox"
        else:
            app_mul = "nox"
        logging.info(f"�ն��豸:{app_mul}")
        self.main = self.app.start(app_mul).go_main()

    def teardown_class(self):
        # �ر�app
        self.app.stop()

    def test_search(self):
        logging.info(f"��������ҳ��->��������")
        # ������ҳ��->���������->��������ҳ��->������������->���ȡ��->������ҳ��
        result = self.main.goto_search().input_text().goto_main()
        assert result

    def test_search2(self):
        logging.info(f"��������ҳ��->��������")
        # ������ҳ��->���������->��������ҳ��->������������->���ȡ��->������ҳ��
        result = self.main.goto_search().input_text().goto_main()
        assert result
