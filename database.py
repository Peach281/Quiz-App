import sqlite3
con = sqlite3.connect('data1.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS details(
            username text,
            email text PRIMARY KEY,
            password text
            )''')
con.commit()
con.close()