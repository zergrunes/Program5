'''
Marian Remoroza
Data Science
'''
import pandas as pd
import numpy as np
import sqlite3 as sql
import csv
with open('scores.csv', 'r') as fin:
    dr = csv.DictReader(fin)
    scores = [(i['Name'], i['Test 1'], i['Test 2'],
               i['Test 3'], i['Project']) for i in dr]
    print(scores)
    fin.close()
con = sql.connect('sql.db')
cur = con.cursor()
'''
cur.execute(
    'CREATE TABLE student(Name text, Test1 int, Test2 int, Test3 int, Project int)') '''
cur.executemany(
    'INSERT INTO student VALUES(?,?,?,?,?)', scores)
x = cur.execute('select * from student')
con.commit()

with open('profiles.csv', 'r') as f:
    dict = csv.DictReader(f)
    profile = [(i['name'], i['gpa'], i['major']) for i in dict]
    print(profile)
    f.close()
#cur.execute('CREATE TABLE student_info(name text, gpa float, major text)')
cur.executemany('INSERT INTO student_info VALUES(?,?,?)', profile)
y = cur.execute('select * from student_info')
con.commit()

print('\n Fetching student information...')
