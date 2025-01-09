

# 2025.1.9统计 沪深300 成分股的当前股息率，同时下载股息走势图

# 数据源 https://eniu.com/gu/sh601288/dv


hushen300 =["688981","688599","688506","688472","688396","688303","688271","688256","688223","688187","688169","688126","688111","688082","688041","688036","688012","688009","688008","605499","605117","603993","603986","603833","603806","603799","603659","603501","603392","603369","603296","603288","603260","603259","603195","603019","601998","601995","601989","601988","601985","601939","601919","601916","601901","601899","601898","601888","601881","601878","601877","601872","601868","601865","601857","601838","601818","601816","601808","601800","601799","601788","601766","601728","601699","601698","601689","601688","601669","601668","601658","601633","601628","601618","601607","601601","601600","601398","601390","601377","601360","601336","601328","601319","601318","601288","601238","601236","601229","601225","601211","601186","601169","601166","601138","601136","601127","601117","601111","601100","601088","601066","601059","601021","601012","601009","601006","600999","600989","600958","600941","600938","600926","600919","600918","600905","600900","600893","600887","600886","600875","600845","600837","600809","600803","600795","600760","600745","600741","600690","600674","600660","600600","600588","600585","600584","600570","600547","600519","600515","600489","600482","600460","600438","600436","600426","600415","600406","600377","600372","600362","600346","600332","600309","600276","600233","600219","600196","600188","600183","600176","600161","600160","600150","600115","600111","600104","600089","600085","600066","600061","600050","600048","600039","600036","600031","600030","600029","600028","600027","600026","600025","600023","600019","600018","600016","600015","600011","600010","600009","600000","301269","300999","300979","300896","300832","300782","300760","300759","300750","300661","300628","300502","300498","300450","300442","300433","300418","300413","300408","300394","300347","300316","300308","300274","300124","300122","300059","300033","300015","300014","003816","002938","002920","002916","002812","002736","002714","002709","002648","002601","002594","002555","002493","002475","002466","002463","002460","002459","002422","002415","002371","002352","002311","002304","002271","002252","002241","002236","002230","002180","002179","002142","002129","002074","002050","002049","002028","002027","002007","002001","001979","001965","001289","000999","000983","000977","000975","000963","000938","000895","000876","000858","000807","000800","000792","000786","000776","000768","000725","000708","000661","000651","000630","000625","000617","000596","000568","000538","000425","000408","000338","000333","000301","000166","000157","000100","000063","000002","000001"]

import base64
import sqlite3
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from lxml import etree
from selenium import webdriver
import time
import uuid


class BS4Parse():
    def __init__(self, html_doc):
        self.soup = BeautifulSoup(html_doc, 'html.parser')

    def parseOneElement(self, tagName):
        trans_list = []
        for single_tag in self.soup.select(tagName):
            trans_list.append(" ".join(single_tag.text.split()))
        tagText = " ".join(trans_list)
        return tagText, trans_list

    def fetchAllText(self):
        AllText = "".join(self.soup.get_text().split())
        return AllText


def generate_unique_id():
    unique_id = str(uuid.uuid4())[:8].lower()
    return unique_id


driver = webdriver.Chrome()

def translate_date(date_string):
    # 原始日期字符串
    # 转换为 datetime 对象
    date_object = datetime.strptime(date_string, '%b %d %Y')

    # 将 datetime 对象格式化为 ISO 8601 格式（YYYY-MM-DD）
    formatted_date = date_object.strftime('%Y-%m-%d')
    return formatted_date # 输出: 2023-09-11

def parse_html(html_doc,url):
    element = etree.HTML(html_doc)

    title = element.xpath(
        '/html/body/div[4]/div/div[1]/div/div[1]/div/div[1]/div[1]/h3/a/text()')
    dv = element.xpath(
        '//*[@id="infoBox股息率"]/text()')


    for i1,i2 in zip(title,dv):
        print(i1,",",i2)

    # 等待页面加载完成（可以根据需要调整时间）
    # time.sleep(5)
    # driver.get(url)  # 替换为包含 Canvas 的网页 URL
    # # 执行 JavaScript 获取 Canvas 图像数据
    # canvas_image = driver.execute_script("""
    #     var canvas = document.querySelector('canvas'); // 找到 Canvas 元素
    #     if (canvas) {
    #         return canvas.toDataURL('image/png'); // 获取 PNG 格式的数据 URL
    #     } else {
    #         return null; // 如果没有找到 Canvas，返回 null
    #     }
    # """)
    #
    # # 关闭 WebDriver
    # driver.quit()
    #
    # # 检查返回值并下载图片
    # if canvas_image is not None:
    #     # 提取 Base64 编码部分
    #     base64_data = canvas_image.split(',')[1]
    #
    #     # 解码 Base64 数据并保存为文件
    #     image_data = base64.b64decode(base64_data)
    #     with open('canvas_image.png', 'wb') as file:
    #         file.write(image_data)
    #
    #     print("图片已成功下载！")
    # else:
    #     print("未找到 Canvas 元素，请检查网页或选择器。")




def fetch_data(url):
    driver.get(url)
    time.sleep(2)
    html = driver.page_source
    return html


def to_integer(string):
    if "," in string:
        ret = "".join(string.split(","))
    else:
        ret = string

    if string == "":
        ret = "0"

    return ret




def insert_into_DB(dbname, tbname, dt_tuple_list):
    connection = sqlite3.connect(dbname)
    cursor = connection.cursor()

    # 创建表（如果不存在）
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {tbname} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date_ TEXT UNIQUE,
        open_ TEXT,
        high_ TEXT,
        low_ TEXT,
        close_ TEXT,
        adj_close TEXT,
        volume_ TEXT
    )
    ''')

    try:
        for item in dt_tuple_list:
            date_value = item[0]

            # 查询日期是否已存在
            cursor.execute(f'SELECT COUNT(*) FROM {tbname} WHERE date_ = ?', (date_value,))
            exists = cursor.fetchone()[0] > 0

            if not exists:
                # 插入数据
                cursor.execute(
                    f'INSERT INTO {tbname} (date_, open_, high_, low_, close_, adj_close, volume_) VALUES (?, ?, ?, ?, ?, ?, ?)',
                    item
                )
                print(f'向SQLite中添加数据成功: {item}')
            else:
                print(f'日期 {date_value} 已存在，跳过插入。')

        connection.commit()
    except Exception as e:
        print(f"插入数据出错: {e}")
    finally:
        connection.close()



if __name__ == '__main__':
    # https://eniu.com/gu/sz000002  sh

    for item in hushen300:
        sh_stock_url = "https://eniu.com/gu/" + "sh" + item
        sz_stock_url = "https://eniu.com/gu/" + "sz" + item
        # 未收录此股票
        sh_stock_html_doc = fetch_data(sh_stock_url)
        sz_stock_html_doc = fetch_data(sz_stock_url)
        if "未收录此股票" not in sh_stock_html_doc:
             parse_html(sh_stock_html_doc,sh_stock_url+"/dv")
        if "未收录此股票" not in sz_stock_html_doc:
             parse_html(sz_stock_html_doc,sz_stock_url+"/dv")
        time.sleep(2)






    #
    # dt_tuple_list = []
    # # 数据库名称和表名
    # db_name = 'us_invest.db'
    # table_name = 'nas100_index'
    #
    # url = 'https://finance.yahoo.com/quote/%5EIXIC/history/'
    # html_doc = fetch_data(url)
    #



    # high_ = element.xpath(
    #     '//*[@id="nimbus-app"]/section/section/section/article/div[1]/div[3]/table/tbody/tr/td[3]/text()')
    # low_ = element.xpath(
    #     '//*[@id="nimbus-app"]/section/section/section/article/div[1]/div[3]/table/tbody/tr/td[4]/text()')
    # close_ = element.xpath(
    #     '//*[@id="nimbus-app"]/section/section/section/article/div[1]/div[3]/table/tbody/tr/td[5]/text()')
    # adj_close = element.xpath(
    #     '//*[@id="nimbus-app"]/section/section/section/article/div[1]/div[3]/table/tbody/tr/td[6]/text()')
    # volume_ = element.xpath(
    #     '//*[@id="nimbus-app"]/section/section/section/article/div[1]/div[3]/table/tbody/tr/td[7]/text()')
    #
    # for i1, i2, i3, i4, i5, i6, i7 in zip(date_, open_, high_, low_, close_, adj_close, volume_):
    #     modified_list1 = [item if item != "-" else "" for item in [i1, i2, i3, i4, i5, i6, i7]]
    #     integer_list = [to_integer(x) for x in modified_list1]
    #     last_list = [translate_date(integer_list[0])] + integer_list[1:]
    #
    #     dt_tuple_list.append(tuple(last_list))
    #
    # driver.quit()
    # insert_into_DB(db_name, table_name, dt_tuple_list)
    #
    #
    #


