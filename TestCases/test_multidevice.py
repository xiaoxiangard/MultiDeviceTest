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
        # ����app
        self.app = App()

    def setup(self):
        self.main = self.app.start().go_main()

    def teardown_class(self):
        # �ر�app
        self.app.stop()

    def test_search(self):
        logging.info(f"��������ҳ����������")
        # ������ҳ��->���������->��������ҳ��->������������->���ȡ��->������ҳ��
        result = self.main.goto_search().input_text().goto_main()
        assert result

    def test_search2(self):
        logging.info(f"��������ҳ����������")
        # ������ҳ��->���������->��������ҳ��->������������->���ȡ��->������ҳ��
        result = self.main.goto_search().input_text().goto_main()
        assert result
