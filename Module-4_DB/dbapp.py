import sqlite3

try:
    conn=sqlite3.connect('testdb.db')
    print("Database connected!")
except Exception as e:
    print(e)

# Create table
create_tbl="create table studinfo(id int primary key,name text,city text)"
try:
    conn.execute(create_tbl)
    print("Table created successfully!")
except Exception as e:
    print(e)

# Insert Records
insert_data="insert into studinfo values    Sanket','Python'),(2,'Nirav','JAVA'),(3,'Ashok','PHP'),(4,'Pritesh','Angular'),(5,'Mitesh','React')"
try:
    conn.execute(insert_data)
    conn.commit()
    print("Record inserted!")
except Exception as e:
    print(e)

# Update Record
update_data="update studinfo set name='Hitesh',city='HTML' where id=5"
try:
    conn.execute(update_data)
    conn.commit()
    print("Record updated!")
except Exception as e:
    print(e)

# Delete Data
delete_data="delete from studinfo where id=5"
try:
    conn.execute(delete_data)
    conn.commit()
    print("Record deleted!")
except Exception as e:
    print(e)

# Select Data

cur=conn.cursor()
select_data="select * from studinfo"
try:
    cur.execute(select_data)
    data=cur.fetchall()
    #data=cur.fetchmany(5)
    #data=cur.fetchone()
    #print(data)

    n=1
    for i in data:
        #print(i)
        print(f"Student[{n}]={i[2]}")
        n+=1
except Exception as e:
    print(e)