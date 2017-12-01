import pymysql as msq
import pymysql.cursors
import json


def getdata(sql):
    conn = msq.connect(host='taogushen.mysql.rds.aliyuncs.com',
                       port=3306,
                       user='tgs',
                       passwd='taotestgushen15',
                       db='tgs_test2',
                       cursorclass=pymysql.cursors.DictCursor,
                       charset='utf8'
                       )

    try:
        with conn.cursor( ) as cursor:
            # 执行sql语句结果存储到缓存
            aa = cursor.execute(sql)
            # 返回所有查询结果，结果是个list [{},{}]
            data = cursor.fetchall( )
            for i in data:
                for j in i:
                     # print (j,":",i[j])
                     return i[j]
    except:
        print("Error: unable to fetch data")
    finally:
        conn.close( )


def getnum(sql):
    conn = msq.connect(host='taogushen.mysql.rds.aliyuncs.com',
                       port=3306,
                       user='tgs',
                       passwd='taotestgushen15',
                       db='tgs_test2',
                       cursorclass=pymysql.cursors.DictCursor,
                       charset='utf8'
                       )

    try:
        with conn.cursor( ) as cursor:
            # 执行sql语句结果存储到缓存
            cursor.execute(sql)
            data = cursor.fetchall( )
            num = len(data)
            return num
    except:
        print("Error: unable to fetch data")
    finally:
        conn.close( )

# if __name__ == "__main__":
#     sql = "SELECT real_name FROM base_project WHERE trade_name like '%自动确认净值%'"
#     getdata(sql)
