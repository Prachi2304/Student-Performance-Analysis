import sqlite3
def create_db():
    con=sqlite3.connect(database="rms.db")
    cur=con.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text,duration text,charges text,description text)")
    con.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS student(Name text,Roll INTEGER PRIMARY KEY AUTOINCREMENT,Course text,Gender text,Sem text,Sub1 text,Sub2 text,Sub3 text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS result(rid INTEGER PRIMARY KEY AUTOINCREMENT,roll text, name text,course text, marks1 text, marks2 text, marks3 text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,f_name text, l_name text, contact text, email text, question text, answer text, password text)")
    con.commit()
    con.close()
create_db()
