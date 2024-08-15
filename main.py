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

# def create_blog():
#     with connection:
#         with connection.cursor() as cursor:
#             sql = """
#             create table if not exists TechSpace.Blogs(
#             id int primary key auto_increment,
#             title varchar(100),
#             author_name varchar(100)
#             )
#             """
#             cursor.execute(sql)
#         connection.commit()

    
# create_blog()
    


# def insert_into_blog(blog_name, author):
#     with connection:
#         with connection.cursor() as cursor:
#             sql = """
#                 insert into TechSpace.Blogs(title, author_name)
#                 Values (%s, %s);
#             """
#             cursor.execute(sql, (blog_name, author))
#         connection.commit()

# insert_into_blog("title3", 'author3')

# def get_blog():
#     with connection.cursor() as cursor:
#         sql = "SELECT * FROM TechSpace.Blogs"
#         cursor.execute(sql)
#         return cursor.fetchall()
    
# print(get_blog())


# def write_to_file(blog_list: List) -> None:
#     with open('blog_list.txt', 'w') as f:
#         for b in blog_list:
#             for key, value in b.items():
#                 f.write(f"{key}: {value}\n") 
#             f.write("-------------------------------- \n")

# write_to_file(get_blog())





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












# def update_blog(id, title):
#     with connection:
#         with connection.cursor() as cursor:
#             sql = f"""update TechSpace.Blogs 
#                 set title = %s 
#                 where id = %s;"""
#             cursor.execute(sql, (title, id))
#         connection.commit()

# update_blog(5, "python blog")

# def get_single_blog(id):
#     with connection.cursor() as cursor:
#         sql = """
#             select * from TechSpace.Blogs 
#             where id = %s;
#             """
#         cursor.execute(sql, (id))
#         result = cursor.fetchone()
#         return result
        

# print(get_single_blog(5))


# def filter_by_name(title):
#     with connection.cursor() as cursor:
#         sql = f"""
#             select * from TechSpace.Blogs 
#             where title like "%{title}%"
#             """
#         cursor.execute(sql)
#         result = cursor.fetchall()
#         return result
    
# print(filter_by_name('python'))


# def delete_blog(id):
#     with connection:
#         with connection.cursor() as cursor:
#             sql = """
#                 delete from TechSpace.Blogs 
#                 where id = %s
#             """
#             cursor.execute(sql, (id))
#         connection.commit()


# delete_blog(5)






























# =======================================================================================================================
