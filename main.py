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


def create_blog():
    with connection:
        with connection.cursor() as cursor:
            sql = """
            create table if not exists TechSpace.Blogs2(
            id int primary key auto_increment,
            title varchar(100),
            author_name varchar(100)
            )
            """
            cursor.execute(sql)
        connection.commit()

    
# create_blog()



modified = []
data_list = []
data = {}
with open('blog_list.txt', 'r') as f:
    # a = f.readlines()
    for line in f:
        if line[-1] == '\n':
            modified.append(line[:-1])
        else:
            modified.append(line)

    for l in modified:
        if l.startswith('id'):
            data['id'] = int(l.split(':')[1])
        elif l.startswith('title'):
            data['title'] = l.split(':')[1]
        elif l.startswith('author_name'):
            data['author_name'] = l.split(':')[1]
        elif l.startswith('-------------------------'):
            if data:
                data_list.append(data)
                data = {}
        if data:
            data_list.append(data)
    if data:
            data_list.append(data)
# print(data)        



def insert_into_blog(data):
    with connection:
        with connection.cursor() as cursor:
            sql = """
                insert into TechSpace.Blogs2(title, author_name)
                Values (%s, %s);
            """
            for data in data_list:
                cursor.execute(sql, (data['title'], data['author_name']))
            connection.commit()
insert_into_blog(data)

