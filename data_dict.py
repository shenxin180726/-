"""
创建一个数据库 dict  utf8格式
创建数据表 words
id    word     mean
将dict.txt 中的单词和解释插入到这个数据表
"""
import pymysql
import re
f = open("dict.txt","r")
db = pymysql.connect(host = "0.0.0.0",
                     port = 3306,
                     user = "root",
                     password = "123456",
                     database = "project_dict",
                     charset = "utf8")
cur = db.cursor()
args_list = []
for line in f:
    t = re.search(r"(\w+)\s+(.*)",line).groups()
    #  +表示匹配前面的字符出现1次或多次
    #  \w 表示匹配普通字符
    #  \s 表示匹配空字符， \S表示匹配飞空字符
    #  *表示出现零次或多次
    args_list.append(t)
try:
    sql = "insert into dict (word,mean) values (%s,%s);"
    cur.executemany(sql,args_list)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()
f.close()
cur.close()


