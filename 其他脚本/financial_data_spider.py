#! -*- coding:utf-8 -*-

import re
import requests
import pymongo





# #请求html
#  selenium 版本与浏览器又有兼容的问题
# driver = webdriver.Chrome()
# driver = webdriver.get('http://data.eastmoney.com')
#
# response = driver.text
# print(response.text)

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










# 新浪净利润 正则表达式
#     patt = re.compile('<td style="text-align:center">(.*?)</td>'+
#                       '.*?<td style="text-align:center">(.*?)</td>'+
#                       '.*?</tr>',re.S)
#     items= re.findall(patt,html)

# 新浪 营业利润率 正则表达式
#     patt = re.compile('<td style="text-align:center">(.*?)</td>'
#                       + '.*?<td style="text-align:center">(.*?)</td>'
#                       + '.*?</tr>',re.S)
#

# 新浪  股本结构 正则表达式
    #
    # patt = re.compile('.*? <td><div align="center">(.*?)</div></td>'
    #                   + '.*?<td><div align="center">(.*?)万股</div></td>'
    #                   +'.*?</tr>',re.S)

# 新浪业绩预报的正则表达式
#     patt = re.compile('.*?<tr >.*?target="_blank">(.*?)</a>.*?target="_blank">(.*?)</a>' +
#                       '.*?<td><.*?>(.*?)</a>' + '.*?<td>(.*?)</td>' + '.*?<td>(.*?)</td>' +
#                       '.*?style="text-align:left">(.*?)</td>' +
#                       '.*?<td>(.*?)</td>.*?<td>(.*?)</td>'  +  '.*?</tr>',re.S)

# '股票代码' + '股票名称' + '类型' + '公告日期' + '报告期' +'业绩预告摘要' + '业绩增幅'
# 标题就直接编写字符串去拼接就好了，没必要在爬区
def parse_one_page(encode_content):
    patt = re.compile('.*?<tr >.*?target="_blank">(.*?)</a>.*?target="_blank">(.*?)</a>' +
                      '.*?<td><.*?>(.*?)</a>' + '.*?<td>(.*?)</td>' + '.*?<td>(.*?)</td>' +
                      '.*?style="text-align:left">(.*?)</td>' +
                      '.*?<td>(.*?)</td>.*?<td>(.*?)</td>'  +  '.*?</tr>',re.S)
    items= re.findall(patt,encode_content)
    for i in items:
        print (i[0],i[1],i[2],i[3],i[4],i[5],i[7])



# 导出数据

# def write_to_file(content):
#     with open(result.csv,)

#
url = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/performance/index.phtml?s_i=&s_a=&s_c=&s_type=%D4%A4%D4%F6&reportdate=2018&quarter=2&p=6'

get_one_page(url)

parse_one_page(encode_content)


# 下载遍历的url列表

# def get_url(url):
#     for i in range(1,999):
#        n = str(i)
#        s = n.zfill(3)
#        for coding in ("600"+s,"000"+s,"300"+s):
#            url = 'http://vip.stock.finance.sina.com.cn/corp/view/vFD_FinanceSummaryHistory.php?stockid='+coding+'&type=NETPROFIT&cate=liru0'
#            yield url
#








