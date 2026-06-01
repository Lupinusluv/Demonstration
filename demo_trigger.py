import sqlite3

def get_user(db, uid):
    # SQL injection: uid 直接拼进查询
    cur = db.cursor()
    cur.execute("SELECT * FROM users WHERE id = " + str(uid))
    return cur.fetchone()

def run(expr):
    # eval 任意输入，远程代码执行风险
    return eval(expr)

def read(path):
    f = open(path)
    data = f.read()
    return data  # 文件句柄从不关闭
