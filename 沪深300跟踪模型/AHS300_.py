







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
    ahs300_pool =["600519","600928","300017","601108","603799","600011","601933","601997","600369","002044","601838","601318","600958","002714","600036","601857","603501","600809","002304","002252","600926","600489","601808","000858","601628","002001","600109","600028","600900","002624","603288","300413","600015","002602","601166","000001","002558","000002","600332","300433","601788","002475","002415","600585","600390","600030","600104","601668","600867","600016","002352","601601","600887","600031","601009","000538","601766","601229","600000","000568","600703","000876","600535","000776","601211","002456","601012","000963","601186","600019","601988","603160","601390","002673","000166","600999","601878","601328","000725","300059","601336","601800","600018","600547","601066","600436","603986","000938","600919","601899","600009","002027","600085","601088","601225","300003","600998","601155","601989","002120","002294","002493","601398","600309","600183","600606","002230","000415","601985","601288","600340","601881","002311","600741","603993","300347","600346","601939","002773","000338","600406","000333","000423","601006","002241","600848","600674","002050","601877","601018","600276","603019","600061","601555","601727","600816","002008","002410","601633","000898","601898","002736","000768","600893","300124","603259","603899","002555","601618","002594","603833","002411","000661","000157","600233","000425","002032","300024","000069","000656","600487","002271","000063","601818","600438","601669","600372","601377","600352","300498","002739","600118","300122","002179","600522","600498","600655","000895","600111","600705","300408","600690","300136","002202","600177","600023","002841","600176","600299","600663","600271","600362","600004","300033","600637","601577","002236","601828","000703","002146","600068","002508","000100","002007","600795","600170","002466","600089","002945","000671","000651","600208","600066","600398","601360","601138","000629","300070","300015","600027","600837","600038","600188","001979","601216","300144","600516","002422","002601","600977","600153","002958","002916","000627","601688","002607","300142","601238","601198","002460","000709","601169","601162","601901","002081","000630","002939","000728","002010","600570","601992","000723","002153","600482","600760","002024","601888","002142","600297","601021","002938","601298","603260","601698","600588","600989","601998","000625","000413","600968","600010","601111","600100","600115","601212","600029","600221","600583","600733"]


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
























#create table ash300_mons(id int not null primary key auto_increment, ash600519  float,ash600928  float,ash300017  float,ash601108  float,ash603799  float,ash600011  float,ash601933  float,ash601997  float,ash600369  float,ash002044  float,ash601838  float,ash601318  float,ash600958  float,ash002714  float,ash600036  float,ash601857  float,ash603501  float,ash600809  float,ash002304  float,ash002252  float,ash600926  float,ash600489  float,ash601808  float,ash000858  float,ash601628  float,ash002001  float,ash600109  float,ash600028  float,ash600900  float,ash002624  float,ash603288  float,ash300413  float,ash600015  float,ash002602  float,ash601166  float,ash000001  float,ash002558  float,ash000002  float,ash600332  float,ash300433  float,ash601788  float,ash002475  float,ash002415  float,ash600585  float,ash600390  float,ash600030  float,ash600104  float,ash601668  float,ash600867  float,ash600016  float,ash002352  float,ash601601  float,ash600887  float,ash600031  float,ash601009  float,ash000538  float,ash601766  float,ash601229  float,ash600000  float,ash000568  float,ash600703  float,ash000876  float,ash600535  float,ash000776  float,ash601211  float,ash002456  float,ash601012  float,ash000963  float,ash601186  float,ash600019  float,ash601988  float,ash603160  float,ash601390  float,ash002673  float,ash000166  float,ash600999  float,ash601878  float,ash601328  float,ash000725  float,ash300059  float,ash601336  float,ash601800  float,ash600018  float,ash600547  float,ash601066  float,ash600436  float,ash603986  float,ash000938  float,ash600919  float,ash601899  float,ash600009  float,ash002027  float,ash600085  float,ash601088  float,ash601225  float,ash300003  float,ash600998  float,ash601155  float,ash601989  float,ash002120  float,ash002294  float,ash002493  float,ash601398  float,ash600309  float,ash600183  float,ash600606  float,ash002230  float,ash000415  float,ash601985  float,ash601288  float,ash600340  float,ash601881  float,ash002311  float,ash600741  float,ash603993  float,ash300347  float,ash600346  float,ash601939  float,ash002773  float,ash000338  float,ash600406  float,ash000333  float,ash000423  float,ash601006  float,ash002241  float,ash600848  float,ash600674  float,ash002050  float,ash601877  float,ash601018  float,ash600276  float,ash603019  float,ash600061  float,ash601555  float,ash601727  float,ash600816  float,ash002008  float,ash002410  float,ash601633  float,ash000898  float,ash601898  float,ash002736  float,ash000768  float,ash600893  float,ash300124  float,ash603259  float,ash603899  float,ash002555  float,ash601618  float,ash002594  float,ash603833  float,ash002411  float,ash000661  float,ash000157  float,ash600233  float,ash000425  float,ash002032  float,ash300024  float,ash000069  float,ash000656  float,ash600487  float,ash002271  float,ash000063  float,ash601818  float,ash600438  float,ash601669  float,ash600372  float,ash601377  float,ash600352  float,ash300498  float,ash002739  float,ash600118  float,ash300122  float,ash002179  float,ash600522  float,ash600498  float,ash600655  float,ash000895  float,ash600111  float,ash600705  float,ash300408  float,ash600690  float,ash300136  float,ash002202  float,ash600177  float,ash600023  float,ash002841  float,ash600176  float,ash600299  float,ash600663  float,ash600271  float,ash600362  float,ash600004  float,ash300033  float,ash600637  float,ash601577  float,ash002236  float,ash601828  float,ash000703  float,ash002146  float,ash600068  float,ash002508  float,ash000100  float,ash002007  float,ash600795  float,ash600170  float,ash002466  float,ash600089  float,ash002945  float,ash000671  float,ash000651  float,ash600208  float,ash600066  float,ash600398  float,ash601360  float,ash601138  float,ash000629  float,ash300070  float,ash300015  float,ash600027  float,ash600837  float,ash600038  float,ash600188  float,ash001979  float,ash601216  float,ash300144  float,ash600516  float,ash002422  float,ash002601  float,ash600977  float,ash600153  float,ash002958  float,ash002916  float,ash000627  float,ash601688  float,ash002607  float,ash300142  float,ash601238  float,ash601198  float,ash002460  float,ash000709  float,ash601169  float,ash601162  float,ash601901  float,ash002081  float,ash000630  float,ash002939  float,ash000728  float,ash002010  float,ash600570  float,ash601992  float,ash000723  float,ash002153  float,ash600482  float,ash600760  float,ash002024  float,ash601888  float,ash002142  float,ash600297  float,ash601021  float,ash002938  float,ash601298  float,ash603260  float,ash601698  float,ash600588  float,ash600989  float,ash601998  float,ash000625  float,ash000413  float,ash600968  float,ash600010  float,ash601111  float,ash600100  float,ash600115  float,ash601212  float,ash600029  float,ash600221  float,ash600583  float,ash600733  float,LastTime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP ) engine=InnoDB  charset=utf8;

# 0,30  1-7 * * 1-5   /usr/local/bin/python3.6 /root/AHS300_.py
#
# 0 19 1,15 * *  /usr/local/bin/python3.6 /root/cron_AHS300_.py