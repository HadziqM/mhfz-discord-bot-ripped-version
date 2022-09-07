import time
from direc import *
from data import *

db = database()
conn = db.connect()
cur = conn.cursor()
a = open('discord.sql', 'r').read()
print('read')
cur.execute(a)
print('executed')
conn.commit()
print('success')
time.sleep(2)
