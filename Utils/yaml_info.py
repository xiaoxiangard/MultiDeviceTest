# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
"""
__author__: wangxiaoxiang
"""
import yaml


# ����yaml����
class YamlInfo:

    # �����෽����������ȥʵ����
    @classmethod
    def read_info(cls, mul):
        # ��ȡyaml����,�ж��ĸ�����
        if mul == "mum":
            with open('../Data/mulator_mum.yaml', 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
        else:
            with open('../Data/mulator_nox.yaml', 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)

        return data
