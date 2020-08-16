

# 查询操作 
# sql = "select * from sales"
# cursor.execute(sql)

# 是否先用函数加sql语句把表头都处理好，后面再去处理插入的问题，也就是找表头，再根据爬取的数据进行插入！
#c插入操作！ 插入单一语句可以
contents = [('s06669','2018-01-30',888888888),('s034364010','2018-01-30',888888888),('s0311310','2018-01-30',888888888)]
for item in contents:
    content = []
    content.append(item)
    import pymysql
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='a_stocks',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    sql_insert = "insert into net_profit (coding,Time,Numbers) values (%s,%s,%s)"
    cursor.executemany(sql_insert,content)
    connection.commit()
    connection.close()


# 更新操作
# sql_update = 'update net_profit set Time = "%s" where id = "%d" '
# cursor.execute(sql_update % ('2020-08-08',1))
# connection.commit()
# connection.close()


# 删除操作

# sql_delete = "delete from net_profit where id = %d"
# cursor.execute(sql_delete % (2))
# connection.commit()
# connection.rollback()
# connection.close()

# result = cursor.fetchall()
# for i in result:
# 	print(i)


#建表格式成功 #净利润建表
create table net_profit (
id int not null primary key auto_increment,
coding varchar(11),
Time  date not null,
Numbers varchar(20));

#插入成功
# insert into net_profit (coding,Time,Numbers) values ('s000099','2018-01-30',888888888),('s000010','2018-01-30',888888888);


# 创建利润率 的列表
create table profit_ratio (
id int not null primary key auto_increment,
coding varchar(11),
Time  date not null,
Numbers varchar(20));


# 股本结构列表
create table shares_holder (
id int not null primary key auto_increment,
coding varchar(11),
Time  date not null,
Numbers varchar(20));



# mysql还是要解决插入中文的字符集设置的我问题！
create table p_report(
id int not null primary key auto_increment,
coding varchar(11),
name varchar(11) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_general_ci' ,
style varchar(6) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_general_ci',
publish_time date not null,
report_time date  not null,
details TEXT CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_general_ci' ,
PE varchar(20),
changes varchar(20)
) engine=InnoDB default charset=utf8;