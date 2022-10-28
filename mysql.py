import pymysql
from datetime import datetime
import json

try:
#資料庫連線設定
#可縮寫db = pymysql.connect("localhost","root","root","30days" )
    db = pymysql.connect(host='localhost', port=3306, user='root', password='j83717410', database='mydb')
    #建立操作游標
    cursor = db.cursor()
    #SQL語法
    sql = 'SELECT * from emp;'
    #執行語法
    cursor.execute(sql)
    #選取all結果
    datas = cursor.fetchall()
    users = []
    data = {}
    for r in datas:
        user = {}
        user['id'] = r[0]
        user['name'] = r[1]
        user['emp'] = r[2]
        user['supervisor'] = r[3]
        user['hiredate'] = r[4]
        users.append(user)
    data['code'] = 0
    data['users'] = users
    print(data)
    # jsonStr = json.dumps(data)
    # print(jsonStr)
    cursor.close()
    #關閉連線
    db.close()
    # print(jsonStr)
except:
    print("error")