import sqlite3

connect = sqlite3.connect('pc_book.db')
cursor = connect.cursor()

cursor.execute('''
    create table if not exists pc (
        id integer primary key autoincrement,
        name text not null
    )
''')
cursor.execute('''
    create table if not exists time (
        id integer primary key autoincrement,
        name text not null
    )
''')
cursor.execute('''
    create table if not exists status (
        id integer primary key autoincrement,
        name text not null
    )
''')

cursor.execute('''
    create table if not exists booking (
        id integer primary key autoincrement,
        fio text not null,
        phone text not null,
        email text not null,
        date date not null,
        id_pc integer,
        id_time integer,
        id_status integer,
        foreign key (id_pc) references pc(id),
        foreign key (id_time) references time(id),
        foreign key (id_status) references status(id)
    )
''')
cursor.execute('''Create table if not exists admin (
id integer  primary key autoincrement,
login text not null unique,
password text not null unique)
''')


connect.commit()
connect.close()

