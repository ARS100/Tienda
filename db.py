import pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="1501",   
        database="tienda_web",
        cursorclass=pymysql.cursors.DictCursor
    )
