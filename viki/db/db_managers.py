import pymysql
from pymysql.err import ProgrammingError

import sqlalchemy as sa
from sqlalchemy import Table, Column, String, Integer, and_


class MysqlManager:
    def __init__(self):
        self.engine = sa.create_engine("mysql+pymysql://root:admin@127.0.0.1/", echo=True)
        self.meta = sa.MetaData()

    def create_db(self, db_name):
        db_name = db_name
        sql = "CREATE DATABASE IF NOT EXISTS " + str(db_name)
        self.engine.execute(sql)

    def read_db_list(self):
        return sa.inspect(self.engine).get_schema_names()    # https://stackoverflow.com/questions/22689895/list-of-databases-in-sqlalchemy

    def update_db_name(self, db_name):
        pass

    def delete_db(self):
        pass


class HallManager:
    def __init__(self, db_name, hall_name=None):
        self.engine = sa.create_engine("mysql+pymysql://root:admin@127.0.0.1/", echo=True)
        self.meta = sa.MetaData()
        self.engine.execute("USE {}".format(db_name))
        self.hall = Table(
            hall_name, self.meta,
            Column('id', Integer, primary_key=True),
            Column('programName', String(100)),
            Column('placeName', String(100)),
            Column('startDate', Integer),
            Column('endDate', Integer),
            Column('priceInfo', String(500)),
            Column('hyperLink', String(100)),
        )

    def create_hall(self):
        self.hall.create(self.engine, checkfirst=True)

    def read_hall_names(self):
        return self.meta.sorted_tables

    def update_hall_name(self):
        pass

    def delete_hall(self):
        self.hall.drop(self.engine, checkfirst=True)


class ProManager:
    def __init__(self, db_name, hall_name):
        self.engine = sa.create_engine("mysql+pymysql://root:admin@127.0.0.1/", echo=True)
        self.meta = sa.MetaData()
        self.engine.execute("USE {}".format(db_name))

        self.hall = Table(                              #이거 autoload 등 이용해서 생략할 수 있을거같음
            hall_name, self.meta,
            Column('id', Integer, primary_key=True),
            Column('programName', String(100)),
            Column('placeName', String(100)),
            Column('startDate', Integer),
            Column('endDate', Integer),
            Column('priceInfo', String(500)),
            Column('hyperLink', String(100)),
        )
        self.conn = self.engine.connect()

    def insert_pro(self, model_dict_or_list):           # id는 신경안써줘도 autoincrement
        if type(model_dict_or_list) is not list:
            model_dict_or_list = list(model_dict_or_list)
        insertion = self.hall.insert()
        self.conn.execute(insertion, model_dict_or_list)

    def select_pro_by_date(self, start_date, end_date):
        selection = self.hall.select().where(
            and_(
                self.hall.c.startDate >= start_date,
                self.hall.c.endDate <= end_date
            )
        )
        return self.conn.execute(selection)

    def update_pro(self):
        pass

    def delete_pro_by_date(self, start_date, end_date):
        deletion = self.hall.delete().where(
            and_(
                self.hall.c.startDate >= start_date,
                self.hall.c.endDate <= end_date
            )
        )
        self.conn.execute(deletion)



"""
# mysql connection
db = pymysql.connect(host='127.0.0.1', user='root', password='admin',
                     charset='utf8')

cur = db.cursor()

cur.execute("SELECT VERSION()")
version = cur.fetchone()
print("Database version: {}".format(version[0]))


cur.execute('SHOW DATABASES;')

sql = 'CREATE DATABASE IF NOT EXISTS test'
cur.execute(sql)


sql = 'USE test'
cur.execute(sql)
print(cur.fetchone())

sql = '''INSERT INTO CUSTOMERS (ID,NAME,AGE,ADDRESS,SALARY)
VALUES (1, 'Ramesh', 32, 'Ahmedabad', 2000.00 );'''
cur.execute(sql)


sql = 'SELECT * from CUSTOMERS'
cur.execute(sql)
rows = cur.fetchall()
print(rows)

sql = '''
    CREATE TABLE CUSTOMERS(
   ID   INT              NOT NULL,
   NAME VARCHAR (20)     NOT NULL,
   AGE  INT              NOT NULL,
   ADDRESS  CHAR (25) ,
   SALARY   DECIMAL (18, 2),       
   PRIMARY KEY (ID)
    );'''
cur.execute(sql)


"""

