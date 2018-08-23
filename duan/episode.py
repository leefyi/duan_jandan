#!/usr/local/bin python
# coding=utf-8
# @Time    : 2018/8/22 上午12:56
# @Author  : lifangyi
# @File    : episode.py
# @Software: PyCharm


# 主程序
# 爬取jandan每日最新的n页段子
# 可配置项 后续更新

from requests_html import HTMLSession
from util import file_generator, mail_worker
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler

BASE_URL = 'http://jandan.net/duan/'
new_page = 0
# http://jandan.net/duan/page-75#comments

# 获取requests-html的session方法


def create_session():
    return HTMLSession()

# duan为静态页面，根据页码构造URL
# fString
# 构造每页请求的URL


def construct_url(page):
    url = BASE_URL + f'page-{page}#comments'
    return url

# 返回最新页


def get_current_page(url=BASE_URL):
    session = create_session()
    r = session.get(url)
    page_block = None
    try:
        page_block = r.html.find('span.current-comment-page')
    except Exception as e:
        print('finding page exception:', e)

    # page_block always contain 2 elements due to the layout of duan
    p = page_block[0]
    ptext = str(p.text)
    # get current page number in string format
    new_page = ptext.replace('[', '').replace(']', '')
    return new_page

# 解析每条段子的明细


def reveal_details(duan_element):

    # 该条段子的所有信息
    text = str(duan_element.text)
    # 观察样式，每行代表不同内容， 以换行符分割
    text_pieces = text.split('\n')
    # 作者
    author = text_pieces[0]
    # id
    id = text_pieces[2]
    # 段子内容，可呢能有多个，在第四个到倒数第二个元素分列，拼接起来
    duan = text_pieces[3:-1]
    duan_text = ''.join(duan)
    # 投票信息，包含举报 喜欢 不喜欢 吐槽，此处暂取喜欢、不喜欢
    votes = text_pieces[-1]
    # 分割投票信息，取出like和unlike的数值
    votes_pieces = votes.split(' ')
    like_raw = str(votes_pieces[2])
    vote_like = like_raw.replace('[', '').replace(']', '')
    unlike_raw = str(votes_pieces[4])
    vote_unlike = unlike_raw.replace('[', '').replace(']', '')

    duan_list = [id, author, duan_text, vote_like, vote_unlike]
    return duan_list

# 爬取信息主程序，默认10页


def loot(range_count=10):
    # 获取最新页码
    current_page = get_current_page(url=BASE_URL)
    print('current:', current_page)
    # session会智能地关闭，暂时不要费心这个
    loot_session = create_session()
    # 存储段子和其它信息的字典，key为段子id,形如3936569
    duan_dict = {}
    # 从第一页起连爬[range_count]页
    for i in range(range_count):
        page = int(current_page) - i
        url = construct_url(page)
        r = loot_session.get(url)
        duan_block = r.html.find('ol.commentlist > li')
        temp = []
        for d in duan_block:
            temp = reveal_details(d)
            index = temp[0]
            print(index)
            duan_dict[index] = temp
    return duan_dict


def job():
    result = loot(10)
    file_generator.duan_header_txt()
    file_generator.duan_write_txt(result)
    file_generator.duan_write_html(result)
    type_file = 'html'
    mail_worker.send_duan(type_file)


def job2():
    result = loot(10)
    file_generator.duan_header_txt()
    file_generator.duan_write_txt(result)
    type_file = 'txt'
    mail_worker.send_duan(type_file)


# if __name__ == '__main__':
#
#     # 粗糙简略的定时任务，太晚了，有空再弄个更灵活的
#     # 阻塞调度器
#     scheduler = BlockingScheduler()
#     # 该示例中的定时任务采用cron（cron）的方式，每一天执行一次。
#     scheduler.add_job(job, 'cron', day='*/1')
#     scheduler.start()

# 定时任务调度入口
def sched():

    # 粗糙简略的定时任务，太晚了，有空再弄个更灵活的
    # 阻塞调度器
    scheduler = BlockingScheduler()
    # 该示例中的定时任务采用cron（cron）的方式，每一天执行一次。
    scheduler.add_job(job, 'cron', day='*/1')
    scheduler.start()


if __name__ == '__main__':
    result = loot(10)
    file_generator.duan_header_txt()
    file_generator.duan_write_txt(result)
    file_generator.duan_write_html(result)
    type_file = 'html'
    mail_worker.send_duan(type_file)
