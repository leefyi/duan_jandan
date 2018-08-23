#!/usr/local/bin python
# coding=utf-8
# @Time    : 2018/8/22 上午1:57
# @Author  : lifangyi
# @File    : file_generator.py
# @Software: PyCharm

import os
from bottle import template

# 将段子信息写入文件的方法
# 简单而朴实的原始方法

TXT_NAME = 'new_10.txt'
MD_NAME = 'new_10.md'
HTML_NAME = 'new_10.html'

base_dir = os.path.dirname(__file__)
file_dir = os.path.abspath(os.path.join(base_dir, '..'))
text_path = os.path.join(file_dir, TXT_NAME)
html_path = os.path.join(file_dir, HTML_NAME)


def duan_header_txt():
    with open(text_path, 'w', encoding='utf-8') as f:
        f.write('id author text like unlike')
        f.write('\n')


def duan_write_txt(duan_dict):
    with open(text_path, 'a', encoding='utf-8') as f:
        for k, v in duan_dict.items():
            id = k
            stream = ' '.join(v)
            f.write(stream)
            f.write('\n')


def duan_write_html(duan_dict):
    contents = []
    # 获取字典中的值list,作为动态生成html元素的值来源
    for k, v in duan_dict.items():
        contents.append(v)
    print(contents)

    # html动态内容
    template_content = """
    <html>
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <h1>jandan每日精选段子</h1>
    </head>
    <title>每日段子</title>
    <body>
    <p>煎蛋：<a href="www.jandan.net">http://www.jandan.net</a></p>
    % for id, author, duan_text, vote_like, vote_unlike in items:
    <h3>{{ author }}</h3>
    <p>{{ duan_text }}</p>
    <span><p>like:{{ vote_like }}</p><p>unlike:{{ vote_unlike }}</p></span>

    </body>
    </html>
    """

    html = template(template_content, items=contents)
    # 写html文件
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
