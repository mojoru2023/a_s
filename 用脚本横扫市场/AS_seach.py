

# 逻辑顺序：第一页，解析代码和页数，送给翻页的页数，解析第二页 解析代码和页数
#
# 1.登录第一页
# 2.解析代码的
# 3.解析页数的
# 4.翻页操作的
# 或者55也而已，直接把要翻页的页码通过测算得到一个列表，后面直接遍历这个礼拜即可！
# 陷阱挺深，逐渐增加了好几次，到了一定程度停止下来，后面在逐渐下降！手动可以处理


# js小陷阱用点击下一页给破掉了！
# body > div.con > div > div.page > a.next
# 1.翻页正常，第一页解析正常
# 2.翻页过快。没有时间解析
# 3.用selenium请求，翻页，解析
# 翻页小陷阱，定位不准xpath ,css定位都会失效 ,一个思路就统计页码标签的个数，统计出和之后赋值给# //*[@id="tbl_wrap"]/div/a[7] b


# -*- coding:utf8 -*-

# 写个小脚本就搞定了！
import re

import pymysql

import time
from selenium import webdriver
from lxml import etree
import datetime


#请求

def get_first_page():
    url = 'http://quote.eastmoney.com/center/gridlist.html#hs_a_board'
    # driver = webdriver.PhantomJS(service_args=SERVICE_ARGS)
    driver.set_window_size(1200, 1200)  # 设置窗口大小
    driver.get(url)
    # time.sleep(3)
    html = driver.page_source
    # time.sleep(3)
    return html


# 把首页和翻页处理？

def next_page():
    for i in range(1,192):  # selenium 循环翻页成功！
        driver.find_element_by_xpath('//*[@id="main-table_paginate"]/a[last()-1]').click()
        time.sleep(1)
        html = driver.page_source
        return html




# 用遍历打开网页59次来处理

    # print(html)  #正则还是有问题，选择了一个动态变动的颜色标记是不好的 最近浏览不是每次都有的！所以用数字的颜色取判断吧

def parse_html(html):  # 正则专门有反爬虫的布局设置，不适合爬取表格化数据！
    big_list = []
    selector = etree.HTML(html)
    name = selector.xpath('//*[@id="table_wrapper-table"]/tbody/tr/td[3]/a/text()')
    code = selector.xpath('//*[@id="table_wrapper-table"]/tbody/tr/td[2]/a/text()')
    now_price = selector.xpath('//*[@id="table_wrapper-table"]/tbody/tr/td[5]/span/text()')
    for i1,i2,i3 in zip(name,code,now_price):  # 两个列表分别遍历然后组成一个新的元组，或新的列表！

        big_list.append((i1,i2,i3))

    return big_list







#存储到MySQL中

def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='a_stock',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    try:
        cursor.executemany('insert into as1009 (name,code,now_price) values (%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except pymysql.err.IntegrityError :
        pass











if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=options)

    html = get_first_page()
    content = parse_html(html)
    time.sleep(1)
    insertDB(content)
    while True:
        html = next_page()
        content = parse_html(html)
        insertDB(content)
        print(datetime.datetime.now())





# 字段设置了唯一性 unique
#
# create table as1009(
# id int not null primary key auto_increment,
# name varchar(20),
# code varchar(12),
# now_price varchar(12),
# UNIQUE(name)
# ) engine=InnoDB  charset=utf8;

# drop table as1009;
