#! -*- coding:utf-8 -*-

import re
import requests
import pymongo
import pymysql
from multiprocessing import Pool

#捕获异常
from requests.exceptions import RequestException
# #请求html

def get_one_page(url):
    headers = {"user-agent":'my-app/0.0.1'}
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None
# 把代码最好都在网页上一次性抓下来！
def parse_one_page(html):
    patt = re.compile('<td style="text-align:center">(.*?)</td>'
                      + '.*?<td style="text-align:center">(.*?)</td>'
                      + '.*?</tr>', re.S)

    items= re.findall(patt,html)

    # 1.空列表，2.遍历子元素（元组）形式  3. 添加子元素到空列表中 4. 需要嵌套两个空列表
    # (总空列表，先把爬取的元组进行列表化再添加入代码，然后再进行元组化，最后把修改后的元组添加入总列表中，最后一个大列表，返回即可！)
    content = []
    for item in items:
        t_l_list = list(item)
        t_l_list.insert(0,'%s'% coding)
        l_t_tuple = tuple(t_l_list)
        content.append(l_t_tuple)
    return content




#存入数据库
#mysql建表，之后再插入 先用命令行尝试测试插入，保证表可以用，后面再测试批量插入数据，数据库
#还是要加强！ 建表，插入的SQL语句也有必要整理一下
# 插入数据库  连接成功，先找解决如何批量插入的问题
# mysql插入数据
def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='a_stocks',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    cursor.executemany("insert into profit_ratio (coding,Time,Numbers) values (%s,%s,%s)", content)
    connection.commit()
    connection.close()
    print('向MySQL中添加数据成功！')




if __name__ == '__main__':
    pool = Pool(4)
    for i in range(1,999):
        n = str(i)
        s = n.zfill(3)
        for coding in ("600"+s,"000"+s,"300"+s,"001"+s,"002"+s,"601"+s,"603"+s,):
            url = 'http://vip.stock.finance.sina.com.cn/corp/view/vFD_FinancialGuideLineHistory.php?stockid=' + coding + '&typecode=financialratios30'
            html = get_one_page(url)
            content = parse_one_page(html)
            insertDB(content)
            print(url)









# 1. 建表，先用id+TIME 把表结构建起来，用平安银行的日期把时间列给撑起来
# 2. sql语句每次，爬取一次就，先插入一列，列名为s+代码，然后再插入数据！批量爬取，批量进行操作！




