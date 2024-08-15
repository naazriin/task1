import pymysql
from typing import List

connection = pymysql.Connect(
    host='localhost',
    user='root',
    password='my-secret-pw',
    db='TechSpace',
    port=3307,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

def create_doctor_table():
    with connection:
        with connection.cursor() as cursor:
            sql = """
                create table if not exists doctor(
                doctor_id int primary key auto_increment,
                doctor_name varchar(30), 
                hospital_id int ,
                joining_date datetime,
                specialty varchar(30), 
                salary decimal(10),
                experience varchar(10)
                )

            """
            cursor.execute(sql)
        connection.commit()

# create_doctor_table()


with connection:
    def insert_table( name, hos_id, date, specialty,salary, experience):
        

            with connection.cursor() as cursor:
                sql = """
                    insert into doctor (doctor_name, hospital_id, joining_date, specialty,salary, experience)
                    values (%s, %s, %s, %s, %s, %s)
                """
                cursor.execute(sql, (name, hos_id, date, specialty,salary, experience))
            


    # insert_table('David', 1, '2005-02-10', 'Pediatric', 40000, 'NULL')
    # insert_table('Michael', 1, '2018-07-20', 'Oncologist', 20000, 'NULL')
    # insert_table('Sysan', 2, '2015-05-14', 'Garnacologist', 25000, 'NULL')
    # insert_table('Robert', 2, '2017-12-28', 'Pediatric', 28000, 'NULL')
    # insert_table('Linda', 3, '2004-06-04', 'Garnacologist', 42000, 'NULL')
    # insert_table('William', 3, '2012-09-11', 'Dermatologist', 30000, 'NULL')
    # insert_table('Richard', 4, '2014-08-20', 'Garnacologist', 32000, 'NULL')
    # insert_table('Karen', 4, '2011-10-17', 'Radiologist', 30000, 'NULL')
    # connection.commit()



def create_hospital_table():
    with connection:
        with connection.cursor() as cursor:
               sql = """create table if not exists hospital(
                hospital_id int primary key auto_increment,
                hospital_name varchar(30), 
                bed_count int
                )"""
               cursor.execute(sql)
        connection.commit()


# create_hospital_table()


with connection:
    def insert_hospital_table(name, bed):
            with connection.cursor() as cursor:
                sql = """ insert into hospital(hospital_name, bed_count)
                values(%s, %s) """ 
                cursor.execute(sql, (name, bed))
    insert_hospital_table('Mayo Clinic', 200)
    insert_hospital_table('Cleveland Clinic', 400)
    insert_hospital_table('Johns Hopkins', 1000)
    insert_hospital_table('UCLA Med Center', 1500)
    connection.commit()

          
