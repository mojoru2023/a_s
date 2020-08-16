import os
import time

import pymysql
import csv

# 数据处理好，看如何塞入execl中


def csv_dict_write(path,head,data):
    with open(path,'w',encoding='utf-8',newline='') as f:
        writer = csv.DictWriter(f,head)
        writer.writeheader()
        writer.writerows(data)
        return True


if __name__ =='__main__':
    big_list1  =[]
    big_list2  =[]
    f_dict = []
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='a_stock',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()



    for num in range(1, 301):
        sql = 'select code,fl_value,type from as_fvalue_type where id = %s ' % num
        # #执行sql语句
        cur.execute(sql)
        # #获取所有记录列表
        data = cur.fetchone()
        big_list1.append(data)


    for num in range(1, 301):
        sql = 'select name,code,v1,v2,v3,v4,v5 from code_netProfits where id = %s ' % num
        # #执行sql语句
        cur.execute(sql)
        # #获取所有记录列表
        data = cur.fetchone()
        big_list2.append(data)


    print(big_list1[1]["code"])
    print(big_list2[1]["code"])
    c1= big_list1[1]["code"]
    c2= big_list2[1]["code"]
    print(len(c1),len(c2[1:]),c1==c2[1:])

    for d1 in big_list1:
        for d2 in big_list2:
            if d1["code"] == d2["code"][1:]:
                # 合并字典
                d2.update(d1)
                f_dict.append(d2)

    head = ['name','code','v1','v2','v3','v4','v5','fl_value','type']
    l_path = os.getcwd()
    csv_dict_write('{0}/hs300.csv'.format(l_path),head,f_dict)
    print("数据导出完成～")

