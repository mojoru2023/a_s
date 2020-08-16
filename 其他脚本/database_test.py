#! -*- coding:utf-8 -*-

import re
import requests
import pandas as pd
from multiprocessing import Pool


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





# l_time = []
# l_values=[]


#净利润爬取
# def parse_one_page(encode_content):
#     patt = re.compile(' <td style="text-align:center">(.*?)</td>' +
#                       '.*?<td style="text-align:center">(.*?)</td>'+'.*?<font style=',re.S)
#     items = re.findall(patt,encode_content)
#     for i in items:
#         l_time.append(i[0])
#         l_values.append(i[1])
#
#
# encode_content= get_one_page(url)
# parse_one_page(encode_content)
#
#


#净利润率解析
# def parse_net_raito(encode_content):
#         patt = re.compile(' <td style="text-align:center">(.*?)</td>' +
#                           '.*?<td style="text-align:center">(.*?)</td>'+'.*?<font style=',re.S)
#         items = re.findall(patt,encode_content)
#         for i in items:
#             print(i)



#股本结构解析

def parse_holders(encode_content):
    patt = re.compile('<td><div align="center">(.*?)</div></td>' +
                      '.*?<td><div align="center">(.*?)万股</div></td>' +
                      '.*?</tr>',re.S)
    items = re.findall(patt,encode_content)
    for i in items:
        print(i)


def main(coding):
    url = 'http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_StockStructureHistory/stockid/' + coding + '/stocktype/TotalStock.phtml'
    html = get_one_page(url)
    parse_holders(html)





if __name__ =="__main__":

    for i in range(1, 999):
        n = str(i)
        s = n.zfill(3)
        pool = Pool()
        pool.map(main, [i for i in ("600" + s, "000" + s, "300" + s)])



# data = {"timing":l_time,"net_profits":l_values}
# frame = pd.DataFrame(data)
# print(frame)


# 瓶颈1：大规模爬取数据
# 瓶颈2：批量处理数据
# 瓶颈3：批量插入数据到时候数据库中，目的是为了好分析