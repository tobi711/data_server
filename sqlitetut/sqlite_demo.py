import sqlite3 

from employee import Employee 
from employee import Visitor 


#good for tests 
conn = sqlite3.connect(':memory:')

#conn = sqlite3.connect('employee.db')
 
c = conn.cursor()

# c.execute("""CREATE TABLE employees ( 
#                 first text, 
#                 last text,
#                 pay integer 
#        )""")

c.execute("""CREATE TABLE mss1(
            Id integer PRIMARY KEY,
            mac text
) """)  

c.execute("""CREATE TABLE mss2(
            Id integer PRIMARY KEY,
            mac text
) """)   

c.execute("""CREATE TABLE mss3(
            Id integer PRIMARY KEY,
            mac text
) """)  

def insert_emp(emp): 
    with conn: 
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first':emp.first, 'last':emp.last, 'pay':emp.pay})
    

def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last':lastname})
    return c.fetchall() 


def update_pay(emp,pay):
    with conn: 
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""", 
                    {'first':emp.first, 'last':emp.last, 'pay': pay})

def remove_emp(emp):
    with conn: 
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
        {'first': emp.first, 'last':emp.last })
 
buffer_1 = ['1231','1333','4444']
counter = 1
for i in buffer_1:
    vis_1 = Visitor(i)
    c.execute("INSERT INTO mss1 VALUES ('{}','{}')".format(counter,vis_1.mac))
    conn.commit() 
    counter += 1 

buffer_2 = ['2222','2223','6666']
counter = 1
for i in buffer_2:
    vis_2 = Visitor(i)
    c.execute("INSERT INTO mss2 VALUES ('{}','{}')".format(counter,vis_2.mac))
    conn.commit() 
    counter += 1 

buffer_3 = ['8888','09999','3434']
counter = 1
for i in buffer_3:
    vis_3 = Visitor(i)
    c.execute("INSERT INTO mss3 VALUES ('{}','{}')".format(counter,vis_3.mac))
    conn.commit() 
    counter += 1 


# c.execute("INSERT INTO visitors VALUES ('{}','{}')".format(1,vis_1.mac))
# conn.commit() 

c.execute("SELECT * FROM mss1 ")
print(c.fetchall())


c.execute("SELECT * FROM mss2 ")
print(c.fetchall())


c.execute("SELECT * FROM mss3 ")
print(c.fetchall())

# emp_1 = Employee('John','Doe', 8000)
# emp_2 = Employee('Jane','Doe', 9000)

# insert_emp(emp_1)
# insert_emp(emp_2)

# emps = get_emps_by_name('Doe')
# print(emps)

# update_pay(emp_2,8888)
# remove_emp(emp_1)

# emps = get_emps_by_name('Doe')
# print(emps)


#c.execute("INSERT INTO employees VALUES ('{}','{}',{})".format(emp_1.first,emp_1.last,emp_1.pay))

# c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first,emp_1.last,emp_1.pay))
# conn.commit() 

# c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first':emp_2.first, 'last':emp_2.last, 'pay':emp_2.pay})
# conn.commit() 

# c.execute("SELECT * FROM employees WHERE last=? ", ('Schafer', ))
# print(c.fetchall())

# c.execute("SELECT * FROM employees WHERE last=:last", {'last':'Doe'})
# print(c.fetchall())

# conn.commit() 

conn.close() 


