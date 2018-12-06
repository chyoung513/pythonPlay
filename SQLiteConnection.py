import sqlite3

print(sqlite3.version)
print(sqlite3.sqlite_version)

conn = sqlite3.connect('C:\MLPlay\SQLWork\sqlLite\sqlLiteTest.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM suppliers')

limit = cursor.fetchmany(2)

for row in limit:
    print('{}  {}  {}  {}  {}'.format(row[0], row[1], row[2], row[3], row[4]))

sql = 'SELECT COUNT(*), SUM(cost), MAX(cost) FROM suppliers'
cursor.execute(sql)

one = cursor.fetchone()
print(one)

# DB 생성
conn = sqlite3.connect('C:\MLPlay\SQLWork\sqlLite\sqlLiteDBTest.db')         #sqlite3.connect(':memory:')로 하면 memory 디비를 생성함   
cursor = conn.cursor()

sql = '''
        CREATE TABLE IF NOT EXISTS tblbooks(
            title text,
            published_date text,
            pages integer,
            recommend integer
        );
        '''
cursor.execute(sql)
conn.commit()

#cursor = cursor.execute('PRAGMA table_info(tblbooks)')
binddata = [('R', '2018-12-08', 500, 5), ('빅데이터', '2018-12-08', 500, 8), ('머신러닝', '2018-09-09', 460, 8)]
cursor.executemany('INSERT INTO tblbooks VALUES(?, ?, ?, ?)', binddata)

conn.commit()
cursor = cursor.execute('SELECT * FROM tblbooks')
for row in cursor:
    print(row)


############ csv파일의 내용을 디비에 저장
import csv

input_file = './input.csv'
sql = '''
        CREATE TABLE IF NOT EXISTS suppliers(
            supplier_name varchar(20),
            invoice_number varchar(20),
            part_number varchar(20),
            cost float,
            purchase_date date
        );
    '''
cursor.execute(sql)
conn.commit()

# 기존에 데이터가 존재하면 삭제
sql = 'DELETE FROM suppliers'
cursor.execute(sql)
conn.commit()

with open(input_file, 'r') as f:
    file_reader = csv.reader(f, delimiter = ',')
    hearder = next(file_reader)

    for line in file_reader:
        cursor.execute('INSERT INTO suppliers VALUES (?, ?, ?, ?, ?)', line)
conn.commit()
conn.close()