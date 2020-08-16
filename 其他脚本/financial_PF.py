#！ -×- coding-utf-8 -*-

#链接 遍历 得到链接列表
# 初始链接


 # pages = 30 一共3页 遍历拼接
#http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/performance/index.phtml?s_i=&s_a=&s_c=&s_type=&reportdate=2018&quarter=2
# http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/performance/index.phtml?s_i=&s_a=&s_c=&s_type=&reportdate=2018&quarter=2&p=30

import re
import time
import requests
import datetime
import json
start = datetime.datetime.now()
from multiprocessing import Pool
from pymongo import MongoClient
import pymysql
from  pymysql import InternalError




# 1.请求部分
def get_one_page(url):
    req= requests.get(url)
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
        return  (encode_content)


# 2.解析部分
# '股票代码' + '股票名称' + '类型' + '公告日期' + '报告期' +'业绩预告摘要' + '业绩增幅'
# 标题就直接编写字符串去拼接就好了，没必要在爬区
# def parse_one_page(encode_content):
#     patt = re.compile('.*?<tr >.*?target="_blank">(.*?)</a>.*?target="_blank">(.*?)</a>' +
#                       '.*?<td><.*?>(.*?)</a>' + '.*?<td>(.*?)</td>' + '.*?<td>(.*?)</td>' +
#                       '.*?style="text-align:left">(.*?)</td>' +
#                       '.*?<td>(.*?)</td>.*?<td>(.*?)</td>'  +  '.*?</tr>',re.S)
#     items= re.findall(patt,encode_content)
#     for i in items:
#
#
#
#         #装入MongoDB中的格式
#         yield {
#             '股票代码':i[0],
#             '股票名称':i[1],
#             '类型':i[2],
#             '业绩增幅' :i[7]
#
#         }


#导出数据 以文件形式
# def get_to_file(content):
#     with open('result.csv','a',encoding='utf-8') as f:
#         f.write(json.dumps(content,ensure_ascii=False) + '\n')
#         f.close()


# 存入MongoDB 中
# def insert_to_Mongo(item):
#     client = MongoClient(host='localhost',port=27017)    #链接连接数据库
#     db = client.A_stock_docs       #建立数据库
#     p = db.Financial_PF            #在上面数据库中建立集合（表）
#     result = p.insert(item)  # 添加内容
#     print(result)

# 3. 总链接爬取的部分 (构造连续的url) 把构造连续urL作为主函数 都是单功能的，只是在最后引用是做循环遍历就好
# 让每个函数，包括主函数都只做一件事！
# start = datetime.datetime.now()


# 要等待解析完成之后再去调用下个url 不然解析会发生错误！
# 借鉴scrapy写一个初始链接然后递增的过程 困难在如何整合

#         #装入MongoDB中的格式
#         yield {
#             '股票代码':i[0],
#             '股票名称':i[1],
#             '类型':i[2],
#             '业绩增幅' :i[7]
#
#         }
# def main(offset):
#     url = "http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/performance/index.phtml?s_i=&s_a=&s_c=&s_type=&reportdate=2018&quarter=2&p=" +str(offset)
#     html = get_one_page(url)
#     item = parse_one_page(html)
#     for i in item:
#         insert_to_Mongo(i)




# start = datetime.datetime.now()

#执行主程序
# if __name__ =="__main__":
    #方案一：没有使用多进程
    # for i in range(1,31):
    #     main(i)
    # pool = Pool()
    # pool.map(main,[i for i in range(31)])
   #
    #
    # end = datetime.datetime.now()
    # print(100 * "-")
    # print(end - start)
# if __name__ == '__main__':
#     for i in range(30):
#         main(i+1)
#     pool = Pool
#     pool.map(main, [i * 10 for i in range(10)])
#
#









def parse_one_page(encode_content):
    patt = re.compile('.*?<tr >.*?target="_blank">(.*?)</a>.*?target="_blank">(.*?)</a>' +
                      '.*?<td><.*?>(.*?)</a>' + '.*?<td>(.*?)</td>' + '.*?<td>(.*?)</td>' +
                      '.*?style="text-align:left">(.*?)</td>' +
                      '.*?<td>(.*?)</td>.*?<td>(.*?)</td>'  +  '.*?</tr>',re.S)
    items= re.findall(patt,encode_content)
    # for i in items:
    #     print(i)
    content = []
    for item in items:
        content.append(item)
    return content


# 插入mysql中, 用异常异常捕捉把错误的匹配都给过滤掉要精细一些就清洗，但是短期不需要
#没有pass 是1200条记录
#有pass  也是1200条记录！

def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='a_stocks',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    try:

        cursor.executemany('insert into p_report (coding,name,style,publish_time,report_time,details,PE,changes) values (%s,%s,%s,%s,%s,%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except InternalError as e:
        print(e)
        pass



# url = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/performance/index.phtml?s_i=&s_a=&s_c=&s_type=%D4%A4%D4%F6&reportdate=2018&quarter=2&p=1'
# html = get_one_page(url)
# parse_one_page(html)




if __name__ == '__main__':
    for offset in range(1,67):
        url = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/performance/index.phtml?s_i=&s_a=&s_c=&s_type=&reportdate=2018&quarter=2&p=' + str(offset)
        html = get_one_page(url)
        content = parse_one_page(html)
        insertDB(content)
        print(offset)






