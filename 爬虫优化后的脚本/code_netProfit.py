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
    driver = webdriver.Chrome()

    driver.set_window_size(1200, 1200)  # 设置窗口大小
    driver.get(url)
    # time.sleep(3)
    html = driver.page_source
    driver.quit()
    # time.sleep(3)
    return html



def Python_sel_Mysql():
    # 使用cursor()方法获取操作游标
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='a_stock',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()
    # sql 语句
    for i in range(3598, 3634):
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
    cursor.executemany("insert into code_netProfits (name,code,v1,v2,v3,v4) values (%s,%s,%s,%s,%s,%s)", content)
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
        f_list = []

        url1 ='http://quotes.money.163.com/f10/lrb_'+str(num_code)+'.html#01c06'


        html1 = get_one_page(url1)
        try:

            selector = etree.HTML(html1)
            all_profits = selector.xpath('//*[@id="scrollTable"]/div[4]/table/tbody/tr[42]/td/text()')
            four_profts = all_profits[:4]
            cut_d = []
            for item in four_profts:
                t = "".join(item.split(","))
                cut_d.append(t)

            name = selector.xpath('/html/body/div[2]/div[1]/div[3]/table/tbody/tr/td[1]/h1/a/text()')
            code = selector.xpath('/html/body/div[2]/div[1]/div[3]/table/tbody/tr/td[1]/h1/span/a/text()')

            first_info = name + code + cut_d
            for item in first_info:

                big_list.append(item)


            l_t = tuple(big_list)
            f_list.append(l_t)
            insertDB(f_list)
            print(datetime.datetime.now())

        except:
            pass

# 筛选一季度最赚钱的贵金属企业
# select * from table_Finances WHERE type="贵金属" order by v1 desc;
# v4---->v1  就近

#
# create table code_netProfits(
# id int not null primary key auto_increment,
# name varchar(11),
# code varchar(11),
# v1 text,
# v2 text,
# v3 text,
# v4 text
# ) engine=InnoDB default charset=utf8;


# drop table code_netProfits;


# 1. 建表，先用id+TIME 把表结构建起来，用平安银行的日期把时间列给撑起来
# 2. sql语句每次，爬取一次就，先插入一列，列名为s+代码，然后再插入数据！批量爬取，批量进行操作！



