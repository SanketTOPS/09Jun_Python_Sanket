import pymysql

try:
    conn=pymysql.connect(host='localhost',user='root',password='',database='mydbapp')
    print("Database Connected!")
except Exception as e:
    print(e)

cur=conn.cursor()

# Create table
create_tbl="create table studinfo(id int primary key,name text,sub text)"
try:
    cur.execute(create_tbl)
    print("Table created successfully!")
except Exception as e:
    print(e)

# Insert Records
insert_data="insert into studinfo values (1,'Sanket','Python'),(2,'Nirav','JAVA'),(3,'Ashok','PHP'),(4,'Pritesh','Angular'),(5,'Mitesh','React')"
try:
    cur.execute(insert_data)
    conn.commit()
    print("Record inserted!")
except Exception as e:
    print(e)

# Update Record
update_data="update studinfo set name='Hitesh',sub='HTML' where id=5"
try:
    cur.execute(update_data)
    conn.commit()
    print("Record updated!")
except Exception as e:
    print(e)

# Delete Data
delete_data="delete from studinfo where id=5"
try:
    cur.execute(delete_data)
    conn.commit()
    print("Record deleted!")
except Exception as e:
    print(e)

# Select Data

select_data="select * from studinfo"
try:
    cur.execute(select_data)
    #data=cur.fetchall()
    #data=cur.fetchmany(2)
    data=cur.fetchone()
    print(data)
except Exception as e:
    print(e)