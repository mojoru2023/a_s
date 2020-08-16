







import datetime
import time

import pymysql
import requests
from lxml import etree
import json
from queue import Queue
import threading
from requests.exceptions import RequestException






def run_forever(func):
    def wrapper(obj):
        while True:
            func(obj)
    return wrapper


def RemoveDot(item):
    f_l = []
    for it in item:

        f_str = "".join(it.split(","))
        ff_str = f_str +"00"
        f_l.append(ff_str)

    return f_l

def remove_douhao(num):
    num1 = "".join(num.split(","))
    f_num = str(num1)
    return f_num
def remove_block(items):
    new_items = []
    for it in items:
        f = "".join(it.split())
        new_items.append(f)
    return new_items


class ASHPool_M(object):

    def __init__(self,url):
        self.url = url

    def page_request(self):
        ''' 发送请求获取数据 '''
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
        }

        response = requests.get(self.url,headers=headers)
        if response.status_code == 200:
            html = response.text
            return html
        else:
            pass

    def page_parse_(self):
        '''根据页面内容使用lxml解析数据, 获取段子列表'''


        html  = self.page_request()
        element = etree.HTML(html)

        now_price = element.xpath('//*[@id="spFP"]/div[1]/span[1]/text()')
        for item in now_price:
            big_list.append(item)
        return big_list




def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='a_stock',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()

    try:
        # 用一个列表解析
        f_ash = ["ash" + str(cod) for cod in ahs300_pool]
        sp_func = lambda x: ",".join(x)
        f_lcode = sp_func(f_ash)

        f_ls = "%s," * len(ahs300_pool)# 这里错了
        cursor.executemany('insert into ash300_mons ({0}) values ({1})'.format(f_lcode, f_ls[:-1]), content)
        connection.commit()
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError:
        pass








if __name__ == '__main__':
    ahs300_pool = ["600036", "000001", "600998", "300347", "600999", "601881", "002475", "002916", "601155", "000069","000703", "600352", "000338", "600153", "002120", "002410", "600406", "000768", "600893", "601318","000938", "603019", "601138", "603993", "600019", "000858", "002032", "603288", "601899", "002236","600346", "600585", "601766", "601012", "300124", "600176"]

    big_list = []


    for it in ahs300_pool:

        if it[0] == "6":
            f_code = "sh"+it
        else:
            f_code = "sz" + it


        url = 'http://gu.qq.com/{0}/gp'.format(f_code)
        print(url)

        ashsp = ASHPool_M(url)# 这里把请求和解析都进行了处理
        ashsp.page_parse_()

    ff_l = []
    f_tup = tuple(big_list)
    ff_l.append((f_tup))
    print(ff_l)
    insertDB(ff_l)
























 # create table ash300_mons(id int not null primary key auto_increment,ash600036  float,ash000001  float,ash600998  float,ash300347  float,ash600999  float,ash601881  float,ash002475  float,ash002916  float,ash601155  float,ash000069  float,ash000703  float,ash600352  float,ash000338  float,ash600153  float,ash002120  float,ash002410  float,ash600406  float,ash000768  float,ash600893  float,ash601318  float,ash000938  float,ash603019  float,ash601138  float,ash603993  float,ash600019  float,ash000858  float,ash002032  float,ash603288  float,ash601899  float,ash002236  float,ash600346  float,ash600585  float,ash601766  float,ash601012  float,ash300124  float,ash600176  float,LastTime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP ) engine=InnoDB  charset=utf8;

# 0,30  1-7 * * 1-5   /usr/local/bin/python3.6 /root/AHS300_.py
#
# 0 19 1,15 * *  /usr/local/bin/python3.6 /root/cron_AHS300_.py