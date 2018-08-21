#!/usr/local/bin python
# coding=utf-8
# @Time    : 2018/8/22 上午1:57
# @Author  : lifangyi
# @File    : file_generator.py
# @Software: PyCharm

import os

# 将段子信息写入文件的方法
# 简单而朴实的原始方法

TXT_NAME = 'new_10.txt'
MD_NAME = 'new_10.md'

base_dir = os.path.dirname(__file__)
text_dir = os.path.abspath(os.path.join(base_dir, '..'))
text_path = os.path.join(text_dir, TXT_NAME)


def duan_header():
    with open(text_path, 'w') as f:
        f.write('id author text like unlike')
        f.write('\n')


def duan_write(duan_dict):
    with open(text_path, 'a') as f:
        for k, v in duan_dict.items():
            id = k
            print(id)
            stream = ' '.join(v)
            f.write(stream)
            f.write('\n')

