import sqlite3
con = sqlite3.connect('data.db')
cur = con.cursor()


cur.execute(''' CREATE TABLE IF NOT EXISTS login (username TEXT,password TEXT)

''')
con.commit()

def insert():
        print("enter your details")
        user = input("enter username")
        password = input("enter password")
        cur.execute(''' INSERT INTO login(username,password) values (?,?)''',(user,password))
        con.commit()
    


def get():
        cur.execute('SELECT * FROM login ')
        rows = cur.fetchall()
        for row in rows:
            print(row)

def varify(username,password):
        cur.execute('SELECT * FROM login WHERE username = ? AND password = ?',(username,password))
        rows = cur.fetchall()
        return len(rows) >0    


# insert()
    # res = varify('bintul',12345)
    # print(res)
# get()

if __name__ == "__main__":
    get()


