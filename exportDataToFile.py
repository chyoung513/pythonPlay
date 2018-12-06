import MySQLdb
import csv

ouput_file = './output.csv'
input_file = './input.csv'
config = {'host': 'localhost', 'user': 'root', 'password': '1111',
          'db': 'scott', 'port': 3306, 'charset':'utf8'}

try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()

    with open(ouput_file, 'w') as f:
        file = csv.writer(f, delimiter = ',')

        header = ['Supplier Name', 'Invoice Number', 'Part Number', 'Cost', 'Purchase Date']
        file.writerow(header)

        sql = 'SELECT * FROM suppliers WHERE cost > 50000'
        cursor.execute(sql)

        for row in cursor:
            file.writerow(row)
except MySQLdb.error as e:
    print(e)
finally:
    conn.close()


