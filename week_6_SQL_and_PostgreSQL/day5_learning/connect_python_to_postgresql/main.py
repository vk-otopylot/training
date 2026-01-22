import psycopg2

conn = psycopg2.connect(database='company_db', user='postgres', password='vivek9484', host='localhost', port='5432')

# print('connection successfully.')

cur = conn.cursor()

# cur.execute('''create table employee(
# emp_id int primary key,
# name varchar(50),
# salary int,
# dept varchar(20));
# ''')
# print('table created successfully.')
#
# cur.execute('''insert into employee values
# (101, 'vivek k', 18500, 'IT'),
# (102, 'shani k', 16000, 'Sales'),
# (103, 'hardeep d', 20500, 'Hr');
# ''')
# print('data added successfully.')

# cur.execute('select * from employee')
# print(cur.fetchall())

# cur.execute('update employee set salary=17000 where emp_id=102')
# print('data updated successfully.')

cur.execute('delete from employee where emp_id=102')
print('data deleted successfully.')

conn.commit()
conn.close()
