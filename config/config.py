#!/usr/local/bin python
# coding=utf-8
# @Time    : 2018/8/22 上午2:17
# @Author  : lifangyi
# @File    : config.py
# @Software: PyCharm

import yaml
import os


def get_yaml_local():
    """
    解析本项目yaml
    :return:
    """
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    print(BASE_DIR)
    path = os.path.join(BASE_DIR, 'settings.yaml')
    f = open(path)
    configs = yaml.load(f)
    f.close()
    return configs
