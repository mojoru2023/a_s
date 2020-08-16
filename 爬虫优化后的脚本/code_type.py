#! -*- coding:utf-8 -*-
import datetime
import re
import time


import requests
# import pymongo
import pymysql
from multiprocessing import Pool
from selenium import webdriver

# 捕获异常
from lxml import etree
from requests.exceptions import RequestException


# #请求html


def get_one_page(url):
    req = requests.get(url)
    #  requests 中文编码的终极办法！
    if req.encoding == 'ISO-8859-1':
        encodings = requests.utils.get_encodings_from_content(req.text)
        if encodings:
            encoding = encodings[0]
        else:
            encoding = req.apparent_encoding

        # encode_content = req.content.decode(encoding, 'replace').encode('utf-8', 'replace')
        global encode_content
        encode_content = req.content.decode(encoding, 'replace')  # 如果设置为replace，则会用?取代非法字符；
        return encode_content


def parse_one_page(html):
    f_list = []
    selector = etree.HTML(html)
    type = selector.xpath('//*[@id="newsTabs"]/div/ul/li/a/text()')

    for item in type:
        f_str = "".join(item.split())
        f_list.append(f_str)

    return f_list


def Python_sel_Mysql():
    # 使用cursor()方法获取操作游标
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='a_stock',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()
    # sql 语句
    for i in range(324, 3634):
        sql = 'select code from a_stock where id = %s ' % i
        # #执行sql语句
        cur.execute(sql)
        # #获取所有记录列表
        data = cur.fetchone()
        Num = data['code']
        yield Num


def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='a_stock',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    cursor.executemany("insert into table_Finances (name,code,v1,v2,v3,v4,type) values (%s,%s,%s,%s,%s,%s,%s)", content)
    connection.commit()
    connection.close()
    print('向MySQL中添加数据成功！')


# 平静还是在于像mysql中批量插入的问题

# 下载遍历的url列表

# 把　A股爬虫数据进行两方面优化：

# 1. 财务数据只取近５个季度的
# 2.同时加入板块的索引一部插入到新表中

        #
        # url1 = 'http://vip.stock.finance.sina.com.cn/corp/go.php/vFD_ProfitStatement/stockid/'+str(num_code)+'/ctrl/part/displaytype/4.phtml'
        # html1 = get_one_page(url1)
        #
        # selector = etree.HTML(html1)
        # all_profits = selector.xpath('//*[@id="ProfitStatementNewTable0"]/tbody/tr[23]/td/text()')
        # four_profts = all_profits[:4]
        # name = selector.xpath('//*[@id="toolbar"]/div[1]/h1/a/text()')
        # code = selector.xpath('//*[@id="toolbar"]/div[1]/h2/text()')
        #
        # first_info = name + code + four_profts +content2
        # for item in first_info:
        #
        #     big_list.append(item)
        #
        #
        #
        #
        #
        #
        # l_t = tuple(big_list)
        # f_list.append(l_t)
        # print(f_list)
        # # insertDB(f_list)
        # print(datetime.datetime.now())

# 筛选一季度最赚钱的贵金属企业
# select * from table_Finances WHERE type="贵金属" order by v1 desc;
# v4---->v1  就近

#
# create table table_Finances(
# id int not null primary key auto_increment,
# name varchar(11),
# code varchar(11),
# v1 text,
# v2 text,
# v3 text,
# v4 text,
# type text
# ) engine=InnoDB default charset=utf8;


# drop table table_Finances;


# 1. 建表，先用id+TIME 把表结构建起来，用平安银行的日期把时间列给撑起来
# 2. sql语句每次，爬取一次就，先插入一列，列名为s+代码，然后再插入数据！批量爬取，批量进行操作！


# ! -*- coding:utf-8 -*-
import datetime
import re
import time

import pyautogui
import requests
# import pymongo
import pymysql
from multiprocessing import Pool
from selenium import webdriver

# 捕获异常
from lxml import etree
from requests.exceptions import RequestException


# #请求html


def get_one_page(url):
    driver = webdriver.Chrome()

    driver.set_window_size(1200, 1200)  # 设置窗口大小
    driver.get(url)
    # time.sleep(3)
    html = driver.page_source
    driver.quit()
    # time.sleep(3)
    return html

def parse_one_page(html):
    selector = etree.HTML(html)
    type = selector.xpath('//*[@id="newsTabs"]/div/ul/li/a/text()')

    for item in type:
        big_list.append(item)

    return big_list


def Python_sel_Mysql():
    # 使用cursor()方法获取操作游标
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='a_stock',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()
    # sql 语句
    for i in range(1873, 3634):
        sql = 'select code from a_stock where id = %s ' % i
        # #执行sql语句
        cur.execute(sql)
        # #获取所有记录列表
        data = cur.fetchone()
        Num = data['code']
        yield Num


def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='a_stock',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    cursor.executemany("insert into code_type (types,code) values (%s,%s)", content)
    connection.commit()
    connection.close()
    print('向MySQL中添加数据成功！')


# 平静还是在于像mysql中批量插入的问题

# 下载遍历的url列表

# 把　A股爬虫数据进行两方面优化：

# 1. 财务数据只取近５个季度的
# 2.同时加入板块的索引一部插入到新表中
if __name__ == '__main__':
    for num_code in Python_sel_Mysql():
        big_list = []
        f_l =[]

        url2 = 'http://quotes.money.163.com/f10/hybk_' + str(num_code) + '.html#01g03'
        html2 = get_one_page(url2)
        content2 = parse_one_page(html2)
        big_list.append(num_code)
        l_s = tuple(big_list)
        f_l.append(l_s)

        insertDB(f_l)
        print(datetime.datetime.now())





        # # insertDB(f_list)
        # print(datetime.datetime.now())

# 筛选一季度最赚钱的贵金属企业
# select * from table_Finances WHERE type="贵金属" order by v1 desc;
# v4---->v1  就近

#
# create table code_type(
# id int not null primary key auto_increment,
# code varchar(11),
# types varchar(50)
# ) engine=InnoDB default charset=utf8;


# drop table code_type;


# 1. 建表，先用id+TIME 把表结构建起来，用平安银行的日期把时间列给撑起来
# 2. sql语句每次，爬取一次就，先插入一列，列名为s+代码，然后再插入数据！批量爬取，批量进行操作！




