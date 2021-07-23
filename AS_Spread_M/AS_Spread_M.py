

import datetime
import time

import pymysql
import requests
from lxml import etree
import json
from queue import Queue
import threading
from requests.exceptions import RequestException




from retrying import retry
import datetime
import re
import time

import pymysql
import requests
from lxml import etree
from requests.exceptions import RequestException

def call_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

# 正则和lxml混用
def parse_html(html):  # 正则专门有反爬虫的布局设置，不适合爬取表格化数据！



    selector = etree.HTML(html)
    Price = selector.xpath('//*[@id="app"]/div[2]/div[2]/div[5]/div/div[1]/div[1]/strong/text()')
    for item in Price:
        big_list.append(item)








def RemoveDot(item):
    f_l = []
    for it in item:

        f_str = "".join(it.split(","))
        f_l.append(f_str)

    return f_l




def remove_block(items):
    new_items = []
    for it in items:
        f = "".join(it.split())
        new_items.append(f)
    return new_items
def retry_if_io_error(exception):
    return isinstance(exception, ZeroDivisionError)






'''
1. 创建 URL队列, 响应队列, 数据队列 在init方法中
2. 在生成URL列表中方法中,把URL添加URL队列中
3. 在请求页面的方法中,从URL队列中取出URL执行,把获取到的响应数据添加响应队列中
4. 在处理数据的方法中,从响应队列中取出页面内容进行解析, 把解析结果存储数据队列中
5. 在保存数据的方法中, 从数据队列中取出数据,进行保存
6. 开启几个线程来执行上面的方法
'''

def run_forever(func):
    def wrapper(obj):
        while True:
            func(obj)
    return wrapper




def remove_douhao(num):
    num1 = "".join(num.split(","))
    f_num = str(num1)
    return f_num



class JSPool_M(object):

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
        patt = re.compile('<div class="stock-current"><strong>(.*?)</strong>',re.S)
        items = re.findall(patt,html)

        big_list.append(items[0])









def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='a_stock',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    try:

        cursor.executemany('insert into AS_SM (AS50_AS300,AS50_AS500,AS300_AS500) values (%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError :
        pass






if __name__ == '__main__':
    big_list = []
    AS50_url ='https://xueqiu.com/S/CSI000016'
    AS300_url ='https://xueqiu.com/S/SH000300'
    AS500_url ='https://xueqiu.com/S/CSI000905'


    jsp1 = JSPool_M(AS50_url)# 这里把请求和解析都进行了处理
    jsp1.page_parse_()
    jsp2 = JSPool_M(AS300_url)# 这里把请求和解析都进行了处理
    jsp2.page_parse_()
    jsp3 = JSPool_M(AS500_url)# 这里把请求和解析都进行了处理
    jsp3.page_parse_()




    AS50_=big_list[0]
    AS300_=big_list[1]
    AS500_=big_list[2]


    # 要价差，不要比价
    AS50_AS300 = float(AS50_)-float(AS300_)
    AS50_AS500 = float(AS50_)-float(AS500_)
    AS300_AS500 =float(AS300_)-float(AS500_)

    title_l = [AS50_AS300,AS50_AS500,AS300_AS500]

    ff_l = []
    f_tup = tuple(title_l)
    ff_l.append((f_tup))
    print(big_list)
    print(ff_l)
    insertDB(ff_l)
#1720
# 1803
# 3612
# 4555




# create table AS_SM(id int not null primary key auto_increment,  AS50_AS300 FLOAT,AS50_AS500 FLOAT,AS300_AS500 FLOAT, LastTime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP ) engine=InnoDB  charset=utf8;
