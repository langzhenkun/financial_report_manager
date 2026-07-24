import pymysql
import os
from dotenv import load_dotenv

load_dotenv()


DB_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": os.getenv("DB_PASSWORD"),
    "database": "financial_report_db",
    "charset": "utf8mb4"
}

#连接数据库
def get_connection():
    connection = pymysql.connect(
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        database=DB_CONFIG["database"],
        charset=DB_CONFIG["charset"],
        cursorclass = pymysql.cursors.DictCursor#以后创建cursor时,会创建能够返回字典结果的cursor。
    )
    return connection