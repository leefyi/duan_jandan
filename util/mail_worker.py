#!/usr/local/bin python
# coding=utf-8
# @Time    : 2018/8/22 上午2:10
# @Author  : lifangyi
# @File    : mail_worker.py
# @Software: PyCharm

import zmail
import datetime
import os
from config import config

# 发送段子邮件的方法
# 使用zmail库，相对精简一些
# 默认附件txt
# 其它情况暂发markdown


def send_duan(typet='txt'):

    # 从yaml配置文件里获取邮箱配置
    conf = config.get_yaml_local()
    username = conf['conf']['username']
    password = conf['conf']['password']
    file_name = 'new_10.txt'

    # 获得当期时间，放在邮件标题，易于区分
    today_time = datetime.datetime.now()
    title_time = today_time.strftime('%Y-%m-%d %H:%M:%S')
    # 邮件标题，内容提示，附件位置
    subject = 'jandan每日新段 - ' + title_time
    content_tip = '热乎的段子又来啦!详情请见附件呦喂～～'
    package_dir = os.path.dirname(__file__)
    base = os.path.abspath(os.path.join(package_dir, '..'))
    if typet == 'txt':
        file_name = 'new_10.txt'
    elif typet == 'html':
        file_name = 'new_10.html'
    else:
        file_name = 'new_10.md'
    attach_path = os.path.join(base, file_name)
    # 构造邮件内容
    mail_content = {
        'subject': subject,
        'content': content_tip,
        'attachments': attach_path
    }

    zserver = zmail.server(user=username, password=password)
    # 状态zserver.smtp_able()
    # 发送
    zserver.send_mail(username, mail_content)
