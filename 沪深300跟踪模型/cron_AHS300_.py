# !/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import datetime
import pymysql
import pandas as pd

from sqlalchemy import create_engine
import pymysql
import pandas as pd
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import datetime

engine_Nas_Mons = create_engine('mysql+pymysql://root:123456@localhost:3306/a_stock')



sql_Nas_Mons = 'select ash600036,ash000001,ash600998,ash300347,ash600999,ash601881,ash002475,ash002916,ash601155,ash000069,ash000703,ash600352,ash000338,ash600153,ash002120,ash002410,ash600406,ash000768,ash600893,ash601318,ash000938,ash603019,ash601138,ash603993,ash600019,ash000858,ash002032,ash603288,ash601899,ash002236,ash600346,ash600585,ash601766,ash601012,ash300124,ash600176,LastTime from ash300_mons  ; '

ln = os.getcwd()


def savedt():

    df_js225 = pd.read_sql_query(sql_Nas_Mons, engine_Nas_Mons)
    excelFile3 = '{0}/{1}.xlsx'.format(ln, "ash300_Mons")  # 处理了文件属于当前目录下！
    df_js225.to_excel(excelFile3)



def sendmail():
    # 发送邮件参数设置
    sender = '291109028@qq.com'  # 发送者邮箱
    password = 'chtrpqnkhyvrcafa'  # 发送者邮箱授权码
    smtp_ip = 'smtp.qq.com'  # smtp服务器ip,根据发送者邮箱而定
    receiver = ['291109028@qq.com']  # 接收者邮箱
    title = 'ash300_Mons'  # 邮件主题
    content = 'ash300_Mons'  # 邮件内容
    annex_path = ln  # 报表存储路径，也是附件路径

    try:

        # 传入邮件发送者、接受者、抄送者邮箱以及主题
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = ','.join(receiver)
        message['Subject'] = Header(str(datetime.datetime.now().date()) + title, 'utf-8')

        # 添加邮件内容
        text_content = MIMEText(content)
        message.attach(text_content)

        # 添加附件

        # 首先是xlsx类型的附件

        xlsxpart3 = MIMEApplication(open('{0}/ash300_Mons.xlsx'.format(ln), 'rb').read())
        xlsxpart3.add_header('Content-Disposition', 'attachment', filename='ash300_Mons.xlsx')
        message.attach(xlsxpart3)

        # 登入邮箱发送报表
        server = smtplib.SMTP(smtp_ip)  # 端口默认是25,所以不用指定
        server.login(sender, password)
        server.sendmail(sender, receiver, message.as_string())
        server.quit()
        print('success!', datetime.datetime.now())

    except smtplib.SMTPException as e:
        print('error:', e, datetime.datetime.now())  # 打印错误


if __name__ == '__main__':
    savedt()
    sendmail()

# 0 19 1,15 * *  /usr/local/bin/python3.6 /root/cron_AHS300_.py
# 每个月的1号的19点钟运行xxx.sh
# 分钟、小时、日子可以更改，后两项为*就是monthly。