import MySQLdb
import csv
from datetime import datetime, date

input_file = './input.csv'
config = {'host': 'localhost', 'user': 'root', 'password': '1111',
          'db': 'scott', 'port': 3306, 'charset':'utf8'}

try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    
    # table만들기
    cursor.execute('DROP TABLE IF EXISTS suppliers')
    createTableSql = '''
        CREATE TABLE suppliers(
            supplier_name varchar(20),
            invoice_number varchar(20),
            part_number varchar(20),
            cost float,
            purchase_date date
        );
        '''
    cursor.execute(createTableSql)
    conn.commit()

    # 초기 데이터 존재시 삭제
    cursor.execute('TRUNCATE TABLE suppliers')
    conn.commit()

    with open(input_file, 'r') as f:
        file = csv.reader(f, delimiter=',')

        header = next(file)  # 현재 위치를 return 및 그 다음줄로 커서 이동

        for row in file:
            cursor.execute('INSERT INTO suppliers VALUES(%s, %s, %s, %s, %s)', row)

        conn.commit()

    cursor.execute('SELECT * FROM SUPPLIERS')

    for (name, number, part_number, cost, date) in cursor:
        print('{}  {}  {}  {}  {}'.format(name, number, part_number, cost, date))

except MySQLdb.Error as e:
    print(e)
finally:
    conn.close()
