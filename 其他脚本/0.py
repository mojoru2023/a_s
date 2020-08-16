#测试代码运行时间
import datetime
import re
import json
import time

import pymysql
import requests
#多进程应用 ,进程池
from multiprocessing import Pool
#捕获异常
from lxml import etree
from requests.exceptions import RequestException

def get_one_page(url):
    #简单的用手机响应头请求
    headers = {"user-agent":'my-app/0.0.1'}
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None




def parse_one_page(html):
    big_list = []
    patt = re.compile('<span data-reactid=".u5c0piyvo6.0.2.3.2.0.$indexList10.0">(.*?):</span>',re.S)
    items = re.findall(patt,html)
    for item in items:
        big_list.append(item)
    return big_list





def write_to_file(content):
    with open('result.txt','a',encoding='utf-8') as f:
        #把字典形式再转换成字符串的形式
        f.write(json.dumps(content,ensure_ascii=False) + '\n')
        f.close()
#构造连续的url
def main(offset):
    url = "http://maoyan.com/board/4?offset=" +str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

start = datetime.datetime.now()

def Python_sel_Mysql():
    # 使用cursor()方法获取操作游标
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='a_stock',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()
    #sql 语句
    for i in range(1,3634):
        sql = 'select code from a_stock where id = %s ' % i
        # #执行sql语句
        cur.execute(sql)
        # #获取所有记录列表
        data = cur.fetchone()
        Num = data['code']
        yield Num


#执行主程序
if __name__ =="__main__":
    url = 'http://gu.qq.com/sh600547/gp'
    html = get_one_page(url)
    time.sleep(1)
    content = parse_one_page(html)
    print(content)







