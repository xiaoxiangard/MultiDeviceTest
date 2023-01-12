# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
"""
__author__: wangxiaoxiang
"""
import yaml


# 处理yaml数据
class YamlInfo:

    # 定义类方法，不用再去实例化
    @classmethod
    def read_info(cls, mul):
        # 读取yaml数据,判断哪个机器
        if mul == "mum":
            with open('../Data/mulator_mum.yaml', 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
        else:
            with open('../Data/mulator_nox.yaml', 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)

        return data
