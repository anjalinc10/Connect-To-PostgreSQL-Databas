import psycopg2
import psycopg2.extras

hostname = 'localhost'
database = 'postgres'
username = 'postgres'
pwd='anjali'
port_id = 5432
conn=None
cur=None

try:
    with psycopg2.connect(host=hostname,dbname=database, user=username,password = pwd, port=port_id) as conn:

        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:

            cur.execute('DROP TABLE IF EXISTS employee')

            create_script = '''CREATE TABLE IF NOT EXISTS employee (id int PRIMARY KEY,
                                                        name varchar(40) NOT NULL,
                                                        salary int,
                                                        dept_id varchar(30))'''
            cur.execute(create_script)

            insert_script = 'INSERT INTO employee(id,name,salary,dept_id) VALUES(%s,%s,%s,%s)'
            insert_value = [(1,'anjali',1200,'D1'),(2,'Sachin',1450,'D2'),(3,'nilesh',3200,'D3'),(4,'gaurav',8990,'D4'),(5,'soham',9920,'D5')]
            for records in insert_value:
                cur.execute(insert_script,records)

            update_script = 'UPDATE employee SET salary = salary + (salary*0.5)'
            cur.execute(update_script)

            delete_script = 'DELETE FROM employee WHERE name = %s'
            delete_record = ('soham',)
            cur.execute(delete_script,delete_record)

            cur.execute('SELECT * FROM EMPLOYEE')
            for record in cur.fetchall():
                print(record['name'],record['salary'])


            conn.commit()

except Exception as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
