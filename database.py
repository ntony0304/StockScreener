'''sqlite database'''
import sqlite3
import traceback


class Database():
    def __init__(self, setting):
        self.db_setting = setting # copy all the attributes inside setting and assign to db_setting
        self.connection = sqlite3.connect(self.db_setting.database_file_location)



    def create_stock_table(self):
        #Date	Open	High	Low	Close	Adjusted_close	Volume
        cur = self.connection .cursor()
        try:
            cur.execute('''CREATE TABLE stocks (
            stock TEXT, date DATE,	open REAL,	high REAL,	low REAL,	close REAL, volume INT)''')#create table
            #Stock*',               'Open',     'High',     'Low',     'Last*',      Vol*
            self.connection.commit() #apply the changes to the database
            self.connection.close()
        except: #if the table exist just skip
            pass
    def database_connection(self):
        self.connection = sqlite3.connect(self.db_setting.database_file_location)
        return  self.connection

    def insert_data(self, stock, date, open, high, low, close, volume):
        conn = self.database_connection()
        cur = conn.cursor()
        query = '''INSERT INTO stocks VALUES ( ? , ?, ?, ?, ?, ?, ? ) '''

        try:
            cur.execute(query,(stock,date,open,high,low,close,volume))
            conn.commit()
        except:
            err = traceback.format_exc()
            print()
        cur.close()
        conn.close()

    def retrieve_row(self):
        query ='''SELECT * FROM stocks WHERE  stock = ?'''
        conn = self.database_connection()
        cur = conn.cursor()
        try:
            cur.execute(query, ("MCD",))
        except:
            pass
        row_data = cur.fetchone()
        conn.close()
        return row_data

    def retrieve_rows(self):
        query = '''SELECT * FROM stocks WHERE  stock = "MCD"'''
        conn = self.database_connection()
        cur = conn.cursor()
        try:
            cur.execute(query)
        except:
            pass
        row_datas = cur.fetchall()
        conn.close()
        return row_datas

    def retrieve_some_rows(self, amount):
        """return row in dictionary"""
        query = '''SELECT * FROM stocks WHERE  stock = "MCD"'''
        conn = self.database_connection()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        try:
            cur.execute(query)
        except:
            pass
        row_data = []
        for row in cur.fetchmany(100):
            row_data.append((dict(row)))
        conn.close()
        return row_data

    def retrieve_rows(self, amount):
        """return row in list"""
        query = '''SELECT * FROM stocks WHERE  stock = "MCD"'''
        conn = self.database_connection()

        cur = conn.cursor()
        try:
            cur.execute(query)
        except:
            pass
        return cur.fetchmany(amount)
