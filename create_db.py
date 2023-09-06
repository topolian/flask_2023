import sqlite3

con = sqlite3.connect("example.db")

cur = con.cursor()
sql_emails = '''
CREATE TABLE IF NOT EXISTS emails
(contactName text, emailValue text);
'''
sql_phones = '''
CREATE TABLE IF NOT EXISTS phones
(contactName text, phoneValue text);
'''

cur.execute(sql_emails)
cur.execute(sql_phones)
con.commit()
con.close()
